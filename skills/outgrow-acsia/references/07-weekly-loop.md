# The Weekly Loop

Five steps, repeating. The loop matters more than any individual part — each step exists to make the next one happen, and removing any one of them collapses the rest within a month.

```
1. ASSIGN  →  2. DO  →  3. LOG  →  4. SCORECARD  →  5. STORIES  →  (back to 1)
```

Most failures are loop failures, not effort failures. People log for two weeks, see no scorecard, and stop. Or the scorecard goes out with no stories attached and becomes a surveillance report. Diagnose at the loop level first.

---

## Step 1 — Assign

Monday. The Outgrow leader assigns **specific quantities of specific actions to specific people against specific named customers**.

Specificity is the whole game. Compare:

> ❌ "Everyone make some proactive calls this week."
> ✅ "**Priya** — call Klaus Berger at Continental about the ADAS V&V proposal from 24 June. Call Rajesh Menon at Bajaj, silent 47 days. Ask Yuki Tanaka the reverse Did You Know about Denso's cybersecurity roadmap. Mention LiLA in your Tuesday Continental sync."

The second version can be executed without thinking. The first requires a decision, and a decision at 9am Monday on a busy week is a decision to skip.

Different roles get different mixes — see the roster table in `03-roles-and-participants.md`. An engineer's assignment should be one or two actions folded into conversations already scheduled. An AE's might be fifteen.

Rotate the list focus weekly so coverage doesn't drift toward whoever is easiest to call.

## Step 2 — Do

Throughout the week, in short bursts, **inside work that's already happening**.

The critical constraint: **five to ten minutes per person per day, including logging.** Not thirty. Not an hour. Outgrow is infused, not blocked out. If a plan requires a dedicated calling block, it's the wrong plan and will be the first thing dropped in a busy week.

Teach **stacking** explicitly — several actions per conversation. Two Did You Knows, a reverse Did You Know and a pivot inside a call that was happening anyway is four logged actions for zero additional time. People don't do this by default; they do one thing per conversation unless told otherwise.

For engineers on site, the action is a single question asked during a meeting they're already in, followed by a text to their manager on the way out.

## Step 3 — Log

Real time, not later. Ninety seconds. Three fields. See `08-logging-and-scorecard.md`.

Logging at the end of the week doesn't happen, and when it does it's fiction. Logging at the end of the day is a compromise. Logging immediately is the standard.

## Step 4 — Scorecard

**Published Friday**, covering Monday–Friday of that week, to everyone. It is then reviewed at Monday's huddle. This is the step most often skipped and it is the one that makes the other four self-sustaining — people log because they can see the result of logging.

Track **leading indicators**: actions logged, by person, this week. Not revenue.

Formats worth using, individually or combined:
- **Stack-ranked total actions by person** — visible, competitive, effective
- **Average actions per week** — fairer to part-time participants
- **Streak** — consecutive weeks with at least one action. Surprisingly motivating; nobody wants to break a streak.
- **Dashboard** — trend over time, opportunities surfaced, estimated value

**Jiji writes personal commentary on it before it goes out.** A scorecard from the analytics admin is a report. A scorecard with two sentences from the CEO naming two people is a signal about what matters here.

Use `scripts/build_scorecard.py` rather than rebuilding chart code weekly.

## Step 5 — Stories

Collect and broadcast the wins — especially the small ones. A dormant account that replied. A customer who said "I didn't know you did that." A referral to another division.

**Peer storytelling changes behavior in a way that private incentives don't.** An engineer hearing that a colleague they respect asked one question and surfaced a functional safety opportunity will try it. The same engineer told to "increase proactive outreach" will not.

Channels: a short internal recognition note, a standing item in the huddle, Jiji forwarding a story with one line of comment.

Include perseverance stories — see `01-mindset-and-perseverance.md`. When something closes, name how many touches and how long it took.

---

## Meeting cadence

Deliberately light. The system's credibility depends on not becoming a meeting.

### Daily — 2 minutes (managers and leaders)
Send one recognition note. Suggest one Did You Know to one person. That's it. The point is that Outgrow is mentioned every single day by someone with authority.

### Weekly huddle — 15 to 20 minutes, Monday
| Time | Item |
|---|---|
| 2 min | Key metrics from last week's scorecard |
| 3 min | One or two success stories — named people, specific wins |
| 10 min | Assign lists and actions for the week; build the call planner. **At the first huddle of each month only**, set that month's Did You Know focus |

Jiji attends. Visibly. Every week.

### Monthly one-on-one — 10 minutes per person
*Look back:* Did they swing enough? Did they hit target actions? What came out of it?
*Look forward:* Top wallet-share opportunity in their accounts. Which of this month's Did You Know and referral focus applies to their specific accounts — the focus itself is set once a month in the huddle, not renegotiated per person.

Ask about long-running pursuits and treat continued effort as the achievement. This is where perseverance either gets reinforced or quietly dies.

### Quarterly planning — 90 minutes, group
*Look back:* Were minimum targets met? Top five performers, bottom five. What did the measured conversion rates turn out to be — feed them into `10-forecast.md`.
*Look forward:* Wallet-share focus, Did You Know focus, referral focus, pre-quote focus, priority accounts for the quarter.

---

## What "good" looks like at week six

- Participation above sixty percent
- Scorecard published six weeks running, unbroken
- At least one story per week that someone outside the program has heard
- Actions specific enough that nobody asks "what should I do?"
- Nobody has yet asked what the revenue impact is — and if they have, someone senior has explained why that's the wrong question this quarter

If participation is below sixty percent at week six, do not add pressure. Go to `09-diagnostics.md` — the cause is almost never the frontline.
