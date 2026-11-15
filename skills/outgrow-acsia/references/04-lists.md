# Customer Lists

Lists exist for one reason: so a manager can be **prescriptive**. "Make some proactive calls" produces nothing. "Call these four named people on the decreasing-revenue list this week" produces swings. Everything below serves that.

## Sizing first — this is adaptive

The book describes eleven categories, which assumes hundreds of customers. Acsia's active delivery base is almost certainly much smaller. **Find out the actual number before building anything**, then collapse accordingly:

| Active accounts | Activate | Shape |
|---|---|---|
| Under 10 | 3 lists | Named-account coverage, not list rotation. Every account gets a weekly owner and a weekly action. |
| 10–30 | 4–5 lists | Weekly rotation works. Each list should have at least three members or it isn't a list. |
| 30–100 | 6 lists | Close to the book's intended shape. |
| Over 100 | Up to 11 | Full model. |

If nobody knows the number, that is itself the first finding — get the count before designing the system. A list with one member is a reminder, not a list, and a set of eleven near-empty lists makes the program look bureaucratic in week one.

## The eleven categories

Organized on four axes: actual revenue activity, future growth potential, pipeline position, and time since last contact.

| # | List | Definition | Why it's there |
|---|---|---|---|
| 1 | **Zero Dark 30** | Averaged meaningful revenue, then ~nothing for 30 days | Silent churn, before anyone notices |
| 2 | **Revenue Autopilot** | Flat, predictable spend | Predictability masks untouched potential |
| 3 | **Decreasing Revenue** | Spending less year over year | A competitor is already inside |
| 4 | **Used to Buy, Stopped** | Was a customer, isn't now | Business moved somewhere |
| 5 | **Quotes/Proposals Outstanding** | Sent, no decision | The fastest revenue in the system |
| 6 | **Pre-Quote** | Opportunity open, nothing sent yet | Stalled before it started |
| 7 | **Large Customers Who Can Buy More** | Biggest accounts | Reverse Did You Know goldmine |
| 8 | **Small/Medium Who Can Buy More** | Everyone else | Hears from Acsia least |
| 9 | **Prospects Who Didn't Buy (warm)** | Evaluated, said no, relationship intact | Program cycles turn |
| 10 | **Prospects Never Contacted (cold)** | — | **Out of scope. This belongs to the outbound engine.** |
| 11 | **Silent 6+ Months** | No meaningful contact in half a year | Easy, and it works |

**List 10 is explicitly excluded.** Cold prospecting is Acsia's existing eight-stage process with its 439-account Apollo ICP. Keep the motions separate or both get muddled.

## Recommended starting set for Acsia

If the base is 10–30 accounts, activate these five. They map to how Acsia's business actually decays and grows:

1. **Quotes & Proposals Outstanding** — start here on day one. Acsia's cycle already includes PROPOSE & NEGOTIATE with a documented 4–8 week duration; anything past that window with no decision is a live follow-up. Competitors rarely chase. This produces the first win, which is what buys the program credibility.
2. **Large Accounts With Wallet-Share Headroom** — the accounts where Acsia delivers today. Target the reverse Did You Know and the percentage-of-business question here.
3. **Silent 6+ Months / Zero Dark 30** — merge these at small scale.
4. **Decreasing Revenue** — accounts where billing is trending down. Early intervention is far cheaper than recovery; by the time an account is gone, a competitor is entrenched.
5. **Warm Prospects Who Didn't Buy** — Acsia's CRM already tags these as `Evaluated & On Hold` under `Nurturing Stage`.

## Building them from Acsia's existing CRM

Acsia's CRM Data Architecture already contains most of the inputs. Do not propose rebuilding it — map to it.

| List | Build from |
|---|---|
| Zero Dark 30 | `Days Since Last Interaction` > 30, filtered to accounts with delivery history |
| Silent 6+ Months | `Days Since Last Interaction` > 180 |
| Quotes Outstanding | Deal stage = PROPOSE & NEGOTIATE, no movement past the documented 4–8 week window |
| Pre-Quote | Deal stage = QUALIFY or RELATE with no proposal raised |
| Warm Didn't Buy | `Nurturing Stage` = `Evaluated & On Hold` |
| Large / Wallet-Share | `Engineering Services Budget (USD)` high, `Domain` coverage narrow relative to Acsia's service lines |
| Decreasing Revenue | **Not derivable from CRM.** Needs revenue-by-account-by-period from finance. Flag this as a gap — it's the one list that requires new plumbing. |

`Current ESP Vendors` (KPIT, Tata Elxsi, LTTS, Capgemini, GlobalLogic) is not a list but should be visible on every list entry — it tells the person making the call exactly whose work they're trying to displace.

### Where these lists touch live outbound deals

Quotes Outstanding, Pre-Quote and Warm-Didn't-Buy are drawn from stages of Acsia's eight-stage process, which means the AE may already be working the same deal. That's fine and intended — Outgrow's contribution there is **follow-up cadence, not ownership**.

Two rules keep it from becoming two systems fighting over one deal:

- **The AE still owns the opportunity.** Deal status, MEDDPICC, and the Blue Sheet stay in the existing process. Outgrow does not create a parallel pipeline record.
- **Outgrow logs the touch, not the deal.** A follow-up on an outstanding proposal is one logged action. Its outcome is tracked where it always was.

If you find yourself updating deal stage inside the Outgrow tracker, stop — that's the two-source-of-truth failure, and it ends with people trusting neither.

## Working rules

- **Lists don't need to be perfect.** An imperfect list acted on beats a perfect list built for three weeks. Start with names on a page.
- **You don't need all of them.** Two good lists beat eleven thin ones.
- **Accounts can sit on several lists.** A large account that's gone quiet belongs on both. That's a feature — it means two different people have a reason to reach out.
- **Build them with the team, not for them.** The delivery engineer knows which account has gone quiet long before the CRM does. Ask.
- **Refresh weekly**, in the Monday huddle, as part of assignment.

## Turning a list into an assignment

The list is raw material. The assignment is the product. Always resolve down to named humans:

> **This week, Priya:** call Klaus Berger (Continental, ADAS V&V proposal sent 24 June, no response) · call Rajesh Menon (Bajaj, silent 47 days) · ask Yuki Tanaka (Denso) the reverse Did You Know about their cybersecurity roadmap · mention LiLA to anyone in your Tuesday Continental sync.

Four actions. Under five minutes. Impossible to misunderstand or defer.
