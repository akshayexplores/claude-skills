# Behavioral Forecast

## Read this before producing any number

The forecast converts logged behavior into expected revenue. It is genuinely useful **once Acsia has its own measured conversion rates** — and actively harmful before then, because a confident wrong forecast destroys trust in the whole program the first time reality diverges.

**Widely circulated figures — 20% for Did You Know, 80% for reverse Did You Know, 25% for pivot-to-sale — must not be used.** They come from distribution businesses where a counter conversation converts the same day, and they did not appear in the source material Akshay actually read. Acsia sells engineering services into OEMs on 9–18 month cycles through procurement gates. There is no reason to think the rates transfer, and strong reason to think they don't.

**If asked to forecast before the rates exist, say so plainly and explain how they'll be obtained.** "We don't know yet, and here's the date we will" is a better answer than a number nobody should act on.

## The model

```
R(t+δ) = C × Σᵢ ( μᵢ × Aᵢ(t) × Vᵢ )
```

| Term | Meaning | Source |
|---|---|---|
| `Aᵢ(t)` | Actions of type *i* logged in week *t* | Scorecard — available immediately |
| `μᵢ` | Conversion rate of action type *i* into a real opportunity | **Must be measured** |
| `Vᵢ` | Average value of opportunities from action type *i* | **Must be measured** |
| `C` | Acsia's close-won rate | Acsia's documented target is >25% — validate against actuals |
| `δ` | Pipeline lead time | Acsia's stage durations sum to roughly 4–7 months from QUALIFY to CLOSE; add procurement and vendor-registration lag |

## How to get the rates

Every logged action carries an action type and an account. Every opportunity carries a source. Connect them and the rates fall out — no special instrumentation needed.

**Timeline:**
- **Weeks 1–12** — log actions. No forecast. Publish leading indicators only.
- **Week 12** — first measurement of μ for high-volume action types. Expect wide error bars and say so.
- **Week 26** — μ stabilizes for common actions. Rare actions (external referral) may never reach useful volume — leave them out rather than guessing.
- **Month 9–12** — first meaningful `C` and `δ` from opportunities that have actually closed.

Until week 26, express forecasts as ranges with explicit assumptions, or don't express them.

## What to publish in the meantime

Leading indicators carry real information without pretending to precision:

- Total actions per week, trend
- Opportunities surfaced (count) and estimated value, marked as **self-reported estimates**
- Participation rate
- Actions per opportunity surfaced — this becomes μ once opportunities mature

Acsia has documented funnel numbers — discovery-to-SQL >40%, proposal close rate >70%, win rate >25%. Two cautions before using them for anything:

**They are targets, not measured actuals.** Check them against what actually happened before treating them as data.

**They describe the cold-acquisition motion, not this one.** An opportunity surfaced by a trusted delivery engineer inside an account Acsia already serves should convert *better* than one sourced from a cold sequence — but "should" is a hypothesis, not a rate. Transferring them across motions is the same error as importing distribution benchmarks, just less obviously. Use them as a **sanity check on magnitude** ("is our number wildly off from the rest of the business?") and never as an input to a forecast.

None of them say anything about μ, which is the unknown that actually matters.

## The honest framing for leadership

> "We can tell you exactly how many proactive customer contacts happened last week, by whom, and which opportunities came out of them. What we can't tell you yet is the conversion rate, because we've never measured it here and the published numbers come from businesses with two-week sales cycles. We'll have a first read at week twelve and a reliable one at week twenty-six. Until then, actions are the number — and they're the number we actually control."

This is a stronger position than a fabricated forecast, and it survives contact with the first quarter's results.
