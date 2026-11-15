#!/usr/bin/env python3
"""
Build the weekly Outgrow scorecard from a CSV of logged actions.

The scorecard deliberately shows LEADING indicators only: how many proactive
actions happened, by whom. It does not show closed revenue. In a business with
9-18 month sales cycles, putting outcomes on a swings scorecard teaches people
that swings were never really the point -- and it teaches them that long before
any swing has had time to convert.

Usage:
    python build_scorecard.py actions.csv --out scorecard.html
    python build_scorecard.py actions.csv --week 2026-08-10 --out scorecard.html \
        --commentary "Great week. Priya's referral into Continental CV is exactly it." \
        --target 10

Expected CSV columns (see assets/tracking-form-schema.csv):
    date, person, account, action_code, service_discussed, estimated_value
Anything else is ignored, so a fuller export works fine.
"""

import argparse
import csv
import html
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta

# Brand-neutral, colourblind-safe categorical palette.
PALETTE = ["#4C6EF5", "#12B886", "#F59F00", "#E8590C", "#7048E8",
           "#1098AD", "#D6336C", "#5C940D"]
INK = "#1A1A1A"
MUTED = "#6B7280"
RULE = "#E5E7EB"
BG = "#FFFFFF"


def parse_date(value):
    value = (value or "").strip()
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%d-%m-%Y", "%Y/%m/%d"):
        try:
            return datetime.strptime(value[:10], fmt).date()
        except ValueError:
            continue
    return None


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8-sig") as fh:
        for raw in csv.DictReader(fh):
            row = { (k or "").strip().lower(): (v or "").strip()
                    for k, v in raw.items() if k }
            if not row.get("person"):
                continue
            row["_date"] = parse_date(row.get("date", ""))
            try:
                row["_value"] = float(str(row.get("estimated_value", "0"))
                                      .replace(",", "").replace("₹", "")
                                      .replace("$", "") or 0)
            except ValueError:
                row["_value"] = 0.0
            row["_opp"] = str(row.get("opportunity_created", "")).strip().lower() \
                in ("1", "true", "yes", "y")
            rows.append(row)
    return rows


def load_roster(spec):
    """Roster may be a comma-separated list of names or a path to a file of names.

    This matters more than it looks. Without an explicit roster the only people
    who can appear in the participation denominator are people who have logged
    at least once -- so a roster member who never engages is invisible, and
    participation reads 100% in exactly the situation it exists to detect.
    """
    if not spec:
        return None
    try:
        with open(spec, encoding="utf-8") as fh:
            names = [ln.strip() for ln in fh if ln.strip()]
    except OSError:
        names = [n.strip() for n in spec.split(",") if n.strip()]
    return names or None


def week_start(d):
    return d - timedelta(days=d.weekday())


def build(rows, week, target, roster=None):
    """Split rows into the focus week and everything before it."""
    dated = [r for r in rows if r["_date"]]
    if week:
        focus = week
    elif dated:
        focus = week_start(max(r["_date"] for r in dated))
    else:
        focus = week_start(datetime.today().date())

    this_week = [r for r in dated if week_start(r["_date"]) == focus]
    if not dated:                      # undated CSV -- treat everything as current
        this_week = rows

    per_person = Counter(r["person"] for r in this_week)
    per_action = Counter(r.get("action_code", "Unspecified") for r in this_week)
    per_service = Counter(r.get("service_discussed", "Unspecified")
                          for r in this_week if r.get("service_discussed"))

    # Streaks: consecutive weeks, ending at the focus week, with >=1 action.
    weeks_by_person = defaultdict(set)
    for r in dated:
        weeks_by_person[r["person"]].add(week_start(r["_date"]))
    streaks = {}
    for person, weeks in weeks_by_person.items():
        n, cursor = 0, focus
        while cursor in weeks:
            n += 1
            cursor -= timedelta(days=7)
        streaks[person] = n

    # Trend across the last 8 weeks.
    trend = []
    for i in range(7, -1, -1):
        w = focus - timedelta(days=7 * i)
        trend.append((w, sum(1 for r in dated if week_start(r["_date"]) == w)))

    # The denominator is the roster if we were given one. Falling back to
    # "everyone who has ever logged" silently flatters the number -- someone who
    # never participates never enters the denominator -- so say so in the output.
    if roster:
        everyone = sorted(set(roster) | set(per_person))
        roster_known = True
    else:
        everyone = sorted(set(list(per_person) + list(weeks_by_person)))
        roster_known = False

    return {
        "focus": focus,
        "total": len(this_week),
        "people": everyone,
        "per_person": per_person,
        "per_action": per_action,
        "per_service": per_service,
        "streaks": streaks,
        "trend": trend,
        "value": sum(r["_value"] for r in this_week),
        "opps": sum(1 for r in this_week if r.get("_opp")),
        "roster_known": roster_known,
        "participation": (sum(1 for p in everyone if per_person[p] > 0)
                          / len(everyone) * 100) if everyone else 0.0,
        "target": target,
    }


def bar_chart(trend):
    if not trend:
        return ""
    peak = max(v for _, v in trend) or 1
    w, h, pad = 620, 150, 28
    step = (w - pad * 2) / max(len(trend), 1)
    bars = []
    for i, (wk, v) in enumerate(trend):
        bh = (v / peak) * (h - pad * 2)
        x = pad + i * step + step * 0.18
        y = h - pad - bh
        bw = step * 0.64
        last = i == len(trend) - 1
        bars.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh:.1f}" '
            f'rx="3" fill="{PALETTE[0]}" opacity="{1 if last else 0.42}"/>'
            f'<text x="{x + bw/2:.1f}" y="{y - 6:.1f}" text-anchor="middle" '
            f'font-size="11" fill="{MUTED}">{v}</text>'
            f'<text x="{x + bw/2:.1f}" y="{h - 9:.1f}" text-anchor="middle" '
            f'font-size="10" fill="{MUTED}">{wk.strftime("%d %b")}</text>')
    return (f'<svg viewBox="0 0 {w} {h}" width="100%" role="img" '
            f'aria-label="Proactive actions per week, last 8 weeks">'
            + "".join(bars) + "</svg>")


def render(d, commentary):
    rank_rows = []
    ranked = sorted(d["people"], key=lambda p: -d["per_person"][p])
    for i, person in enumerate(ranked, 1):
        n = d["per_person"][person]
        pct = f'{n / d["target"] * 100:.0f}%' if d["target"] else "&mdash;"
        streak = d["streaks"].get(person, 0)
        flag = "" if n else ' style="opacity:.5"'
        rank_rows.append(
            f'<tr{flag}><td class="rank">{i}</td><td>{html.escape(person)}</td>'
            f'<td class="num"><strong>{n}</strong></td><td class="num">{pct}</td>'
            f'<td class="num">{streak}w</td></tr>')

    def mix(counter):
        if not counter:
            return '<p class="muted">Nothing logged.</p>'
        top = counter.most_common(8)
        peak = top[0][1]
        out = []
        for i, (label, n) in enumerate(top):
            pct = n / peak * 100
            out.append(
                f'<div class="mixrow"><span class="mixlabel">{html.escape(label)}</span>'
                f'<span class="mixbar"><i style="width:{pct:.0f}%;'
                f'background:{PALETTE[i % len(PALETTE)]}"></i></span>'
                f'<span class="mixnum">{n}</span></div>')
        return "".join(out)

    note = ""
    if commentary:
        note = (f'<div class="ceo"><div class="ceo-label">From Jiji</div>'
                f'<p>{html.escape(commentary)}</p></div>')

    if d["value"] >= 1e7:
        value_txt, value_key = f'{d["value"]/1e7:.1f}Cr', "Est. value surfaced"
    elif d["value"] >= 1e5:
        value_txt, value_key = f'{d["value"]/1e5:.1f}L', "Est. value surfaced"
    else:
        value_txt, value_key = f'{d["value"]:,.0f}', "Est. value surfaced"

    caveat = ("" if d["roster_known"] else
              '<p class="muted" style="margin-top:10px">Participation is measured '
              'against people who have logged at least once, not the full roster &mdash; '
              'pass <code>--roster</code> for the real denominator. Without it this '
              'number reads high exactly when adoption is worst.</p>')

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Outgrow Scorecard &middot; week of {d['focus'].strftime('%d %B %Y')}</title>
<style>
*{{box-sizing:border-box}}
body{{margin:0;padding:32px 20px 64px;background:{BG};color:{INK};
 font:15px/1.55 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif}}
.wrap{{max-width:760px;margin:0 auto}}
h1{{font-size:24px;margin:0 0 4px;letter-spacing:-.01em}}
h2{{font-size:13px;text-transform:uppercase;letter-spacing:.07em;color:{MUTED};
 margin:38px 0 12px;font-weight:600}}
.sub{{color:{MUTED};margin:0 0 28px;font-size:14px}}
.tiles{{display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px}}
.tile{{border:1px solid {RULE};border-radius:10px;padding:14px 16px}}
.tile .v{{font-size:27px;font-weight:650;letter-spacing:-.02em;line-height:1.15}}
.tile .k{{font-size:12px;color:{MUTED};margin-top:3px}}
table{{width:100%;border-collapse:collapse;font-size:14px}}
th{{text-align:left;font-size:11px;text-transform:uppercase;letter-spacing:.05em;
 color:{MUTED};font-weight:600;padding:0 8px 8px;border-bottom:1px solid {RULE}}}
td{{padding:9px 8px;border-bottom:1px solid {RULE}}}
td.num,th.num{{text-align:right}}
td.rank{{color:{MUTED};width:34px}}
.mixrow{{display:flex;align-items:center;gap:10px;margin-bottom:7px;font-size:13px}}
.mixlabel{{flex:0 0 210px;color:{INK}}}
.mixbar{{flex:1;background:#F3F4F6;border-radius:3px;height:9px;overflow:hidden}}
.mixbar i{{display:block;height:100%;border-radius:3px}}
.mixnum{{flex:0 0 30px;text-align:right;color:{MUTED}}}
.ceo{{border-left:3px solid {PALETTE[0]};padding:12px 0 12px 16px;margin:30px 0 0}}
.ceo-label{{font-size:11px;text-transform:uppercase;letter-spacing:.07em;
 color:{MUTED};font-weight:600;margin-bottom:4px}}
.ceo p{{margin:0;font-size:15px}}
.muted{{color:{MUTED};font-size:13px}}
.foot{{margin-top:44px;padding-top:16px;border-top:1px solid {RULE};
 color:{MUTED};font-size:12.5px}}
@media(max-width:520px){{.mixlabel{{flex:0 0 130px}}}}
</style></head><body><div class="wrap">

<h1>Outgrow Scorecard</h1>
<p class="sub">Week of {d['focus'].strftime('%d %B %Y')} &middot; Acsia Technologies</p>

<div class="tiles">
  <div class="tile"><div class="v">{d['total']}</div><div class="k">Proactive actions</div></div>
  <div class="tile"><div class="v">{d['participation']:.0f}%</div><div class="k">Participation</div></div>
  <div class="tile"><div class="v">{len([p for p in d['people'] if d['per_person'][p]])}<span style="font-size:16px;color:{MUTED}">/{len(d['people'])}</span></div><div class="k">People swinging</div></div>
  <div class="tile"><div class="v">{d['opps']}</div><div class="k">Opportunities surfaced</div></div>
  <div class="tile"><div class="v">{value_txt}</div><div class="k">{value_key} <span title="self-reported estimates">*</span></div></div>
  <div class="tile"><div class="v">{max(d['streaks'].values()) if d['streaks'] else 0}w</div><div class="k">Longest streak</div></div>
</div>
{caveat}

{note}

<h2>Actions per week</h2>
{bar_chart(d['trend'])}

<h2>By person</h2>
<table><thead><tr><th></th><th>Name</th><th class="num">Actions</th>
<th class="num">vs target</th><th class="num">Streak</th></tr></thead>
<tbody>{''.join(rank_rows)}</tbody></table>

<h2>Action mix</h2>
{mix(d['per_action'])}

<h2>Service discussed</h2>
{mix(d['per_service'])}

<div class="foot">
* Estimated value is self-reported by the person logging and is not a forecast.<br>
Leading indicators only. Closed revenue is deliberately absent &mdash; Acsia's cycles run
9&ndash;18 months, and measuring Outgrow on hits before the swings have had time to convert
is the fastest way to kill it. First conversion read at week 12; reliable at week 26.
</div>
</div></body></html>"""


def main():
    ap = argparse.ArgumentParser(description="Build the weekly Outgrow scorecard.")
    ap.add_argument("csv", help="CSV of logged actions")
    ap.add_argument("--out", default="scorecard.html")
    ap.add_argument("--week", help="Monday of the focus week, YYYY-MM-DD")
    ap.add_argument("--target", type=int, default=0, help="Per-person weekly action target")
    ap.add_argument("--commentary", default="", help="Jiji's two sentences")
    ap.add_argument("--roster", default="",
                    help="Comma-separated participant names, or a path to a file "
                         "with one name per line. Strongly recommended: without it, "
                         "participation is measured only against people who have "
                         "already logged something.")
    a = ap.parse_args()

    rows = load(a.csv)
    if not rows:
        sys.exit("No usable rows found — check the CSV has a 'person' column.")

    week = parse_date(a.week) if a.week else None
    if week:
        week = week_start(week)

    data = build(rows, week, a.target, load_roster(a.roster))
    with open(a.out, "w", encoding="utf-8") as fh:
        fh.write(render(data, a.commentary))

    print(f"Wrote {a.out} — {data['total']} actions, "
          f"{data['participation']:.0f}% participation, "
          f"week of {data['focus']}")


if __name__ == "__main__":
    main()
