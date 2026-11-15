# Wallet Share Expansion

## The problem underneath everything

**Salespeople dramatically overestimate their share of a customer's spend.** This is the belief that makes everything else unnecessary — if someone thinks they already have most of an account, they won't try for more, and no amount of assignment will change that.

At Acsia the overestimation is likely severe. Acsia's own ICP work found roughly **thirty buying-committee contacts per qualified account**, spread across V&V, functional safety, software architecture, and cockpit teams. An account owner with a strong relationship with three of them, delivering in one domain, may genuinely believe they "have" the account while holding a small single-digit share of its external engineering spend.

Three ways to break the belief, in order of effectiveness:

1. **Ask the customer directly** — the percentage-of-business question. The answer is usually startling.
2. **Show the gap on paper** — put `Engineering Services Budget (USD)` next to Acsia's actual annual billing for that account. The ratio ends the argument.
3. **Show the domain gap** — list Acsia's service lines against the `Domain` values Acsia actually delivers in that account. Most accounts buy one or two of eleven.

The second belief to break: **people don't know everything Acsia sells.** Delivery engineers know their own domain deeply and the adjacent ones vaguely. They cannot offer what they can't name. That's what the cross-sell map is for.

---

## The three expansion levers

### Lever 1 — More service lines per account

The Did You Know surface. Acsia's service lines: AUTOSAR · Functional Safety (ISO 26262) · Cybersecurity (ISO 21434) · ADAS/AD · Embedded · EV & e-Mobility · Telematics · Digital Cockpit & Display / IVI · V&V and Test · ASPICE process consulting · **LiLA**.

Build the cross-sell map from Acsia's existing `Domain` field so it plugs into the CRM rather than sitting beside it:

| If the account already buys… | Did You Know candidates | Why it's a natural adjacency |
|---|---|---|
| **Digital Cockpit / IVI** | V&V and Test · Functional Safety · Cybersecurity · LiLA | Cockpit programs generate enormous validation load; that load is usually outsourced separately |
| **AUTOSAR** | ASPICE consulting · Functional Safety · V&V · LiLA | Classic/Adaptive migrations trigger process and safety work |
| **ADAS/AD** | Functional Safety (ASIL D) · V&V · Cybersecurity · LiLA | Safety case work is mandatory and rarely done in-house |
| **EV / e-Mobility** | Functional Safety · Embedded · Telematics | Battery and drivetrain control pull safety and connectivity |
| **Telematics** | Cybersecurity (ISO 21434) · Embedded · LiLA | Connected implies attack surface implies mandated compliance |
| **V&V and Test** | **LiLA above all** · ASPICE · Functional Safety | LiLA automates exactly this work — the strongest single pairing Acsia has |
| **Anything at all** | **LiLA** | Requirements engineering, compliance, code verification and defect management span every program |

**The V&V → LiLA pairing deserves special attention.** Acsia's ICP research found the V&V, test and quality audience is roughly twenty times larger than the cockpit audience inside qualified accounts — and V&V is precisely what LiLA automates. Any account where Acsia already touches validation is a LiLA conversation waiting to happen.

Give each participant a short list — three or four DYK candidates for *their* accounts, not the full matrix. Eleven options produces paralysis; three produces a question.

### Lever 2 — More volume of what they already buy

Less glamorous, often faster. In a services business this means:

- More engineers on an existing program
- Extending an engagement's duration before it lapses
- Moving from a T&M pool to a committed capacity model
- Adding a second site or shift to an existing scope

The action is simply asking: *"Would it help to have two more people on this from January?"* Most account growth of this kind is lost by never asking.

### Lever 3 — More buyers inside the same customer

Highest leverage at Acsia, because OEMs are federations. One delivery relationship inside a passenger-car program says nothing about commercial vehicle, powertrain, or the Bangalore engineering centre — and the trusted engineer is two sentences from an introduction.

Adapted for automotive:

> "Which other programs inside [OEM] have the same validation problem?"
> "Who runs functional safety for the commercial vehicle platform?"
> "Is there an equivalent team in your [other country] engineering centre?"
> "Who else sits on the tool-chain decision besides you?"

Use Acsia's existing contact fields to target: `Decision Making Level`, `Buying Role (Miller-Heiman)`, `Degree of Influence`, `Relationship Level`. An account with two mapped contacts and thirty in the buying committee is not a covered account — it's a single-threaded one, and single-threaded accounts are how incumbents get displaced quietly.

---

## The wallet-share expansion kit

Prepare this before week one. Per participant, one page:

1. **Their accounts** — named
2. **What each buys today** — from `Domain`
3. **Three DYK candidates per account** — from the table above
4. **Who else they should be talking to** — internal referral targets
5. **Which competitors are already inside** — from `Current ESP Vendors`
6. **The gap number** — engineering services budget vs. Acsia's annual billing, where known

Point six is the one that changes behavior. Everything else is instruction; that is evidence.
