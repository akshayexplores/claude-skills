# Logging and Scorecard

## The 90-second rule

Logging one action takes **ninety seconds and three fields**. This constraint is not a nicety — it's the difference between a system people use and a system people resent.

Every field added past three trades a real customer behavior for a data point. That trade always loses. When someone proposes adding a field, the question to ask is: "which action are we willing to give up to get this?"

## The three fields

These are the three the human thinks about:

| Field | Type | Notes |
|---|---|---|
| **Action taken** | Picklist | Which of the eight actions (see `05-communications.md`) |
| **Service / domain discussed** | Picklist | Maps to Acsia's `Domain` values plus LiLA |
| **Estimated potential value** | Number | A guess is fine. Precision is not the point; magnitude is. |

Identity fields — who, which account, which contact, when — don't count against the three, because they should never require thought. In a CRM they're captured automatically. In a shared-sheet fallback, pre-fill the person and date columns and give the account column a dropdown, so the only things anyone types are the three above. If someone is typing their own name every time, the fallback has been set up wrong.

An optional free-text note is acceptable if it stays optional. The moment it's required, logging stops being ninety seconds.

## Logging rules

- **Real time, not later.** End-of-week logging doesn't happen, and when it does it's reconstruction.
- **Proactive only.** An inbound request handled well is good work and not an Outgrow action. Protecting this line is what makes the number mean anything.
- **Action count must match the notes.** If someone logs four actions, four should be describable. Inflation is contagious and kills the scorecard's credibility in about three weeks.
- **Estimate values.** "Roughly ₹15 lakh if it lands" beats a blank field.
- **Face-to-face and inbound conversations get logged too — but the conversation is never the action.** This is the distinction people get wrong most often, so state it explicitly when training: a customer calls about a defect, you handle it, and before hanging up you ask "what else are you working on?" — **the rDYK is the logged action; the support call is not.** One log, not two. If someone's log count matches their call volume, they're logging conversations rather than asks. Engineers on site should text their manager on the way out and let the manager log it; asking an engineer to open a CRM at a customer's office is asking them not to bother.

## Where it lives at Acsia

Zoho CRM is the natural home. Acsia already has a documented CRM Data Architecture, a CRM Admin role, and account and contact modules that hold most of what's needed. Standing up a parallel tracker in Coda or Notion is faster on day one and creates a second source of truth that diverges by month two.

### What already exists — reuse, don't rebuild

| Need | Existing field |
|---|---|
| Silent-account detection | `Last Meaningful Interaction Date`, `Days Since Last Interaction` |
| Competitive target for rDYK | `Current ESP Vendors` |
| Wallet-share denominator | `Engineering Services Budget (USD)` |
| Cross-sell surface | `Domain` (multi-select) |
| Warm-prospect list | `Nurturing Stage` = `Evaluated & On Hold` |
| Referral targeting | `Decision Making Level`, `Buying Role (Miller-Heiman)`, `Degree of Influence`, `Relationship Level` |
| Channel hygiene | `Last Interaction Channel`, `Opt-out Flags (per persona)` |

### What to add

A lightweight **Outgrow Action** record — the three fields above, linked to account and contact. Give the actions step codes with an `OG` prefix (OG1.1 Did You Know, OG1.2 reverse Did You Know, OG2.1 pivot to sale, and so on) so they slot into Acsia's existing micro-activity taxonomy rather than sitting outside it.

**Respect `Opt-out Flags` on every action.** Acsia already tracks per-channel opt-outs; Outgrow volume makes honouring them more important, not less — particularly for German contacts.

### If Zoho can't be changed quickly

Don't let CRM admin lead time block the launch. Start with a shared sheet using `assets/tracking-form-schema.csv`, run four weeks, and migrate once the behavior exists. The behavior is the hard part; the plumbing is not.

## The scorecard

Weekly, to everyone. Leading indicators only.

**Layouts:**

*Stack-ranked actions this week* — the workhorse. Visible, mildly competitive, effective.

| Rank | Person | Actions | vs. target |
|---|---|---|---|
| 1 | Priya M. | 14 | 140% |
| 2 | Karthik S. | 11 | 110% |

*Average actions per week* — fairer to people participating part-time, which at Acsia is most delivery staff.

*Streak* — consecutive weeks with at least one action. Cheap to compute and disproportionately motivating.

*Trend dashboard* — total actions over time, opportunities surfaced, estimated value, participation rate.

**What not to put on it:** closed revenue, win rates, conversion percentages. Not for the first two quarters. Putting outcomes on a swings scorecard teaches people that swings weren't the point after all — and in a 9–18 month cycle business, it teaches them that lesson before a single swing has had time to convert.

**Jiji's commentary goes on it before it goes out.** Two sentences. Name two people. This converts a report into a signal.

## Use the script

`scripts/build_scorecard.py` takes a CSV of logged actions and produces the weekly scorecard as a standalone HTML file. Use it rather than rebuilding chart code each week — the consistency matters as much as the content, because a scorecard that looks different every week reads as an experiment rather than an institution.

```bash
python scripts/build_scorecard.py actions.csv \
  --week "2026-08-10" \
  --roster "Priya M.,Karthik S.,Anjali R.,Deepak V.,Sven L.,Yuki T." \
  --target 10 \
  --commentary "Jiji's two sentences" \
  --out scorecard.html
```

**Always pass `--roster`.** Without it, participation is calculated only across people who have already logged something — so anyone who never engages is invisible, and the number reads high in precisely the situation it exists to detect. The script prints a warning on the scorecard when the roster is missing, but the right fix is to pass it.
