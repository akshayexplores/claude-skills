# The Proactive Communications

Eight actions. Each takes seconds. None requires budget, permission, or a meeting. Their power is entirely in volume and consistency — a single Did You Know is a rounding error, and a few hundred a quarter is a different business. The mechanism is accumulation, not any individual ask.

The defining property: **proactive means the customer isn't expecting it and nothing is wrong.** Responding to an inbound request, however helpful, is not an Outgrow action. Keeping that line clean is what makes the number mean anything.

## The eight actions

### 1. Did You Know (DYK)
**Purpose:** tell a customer about one thing they can buy from Acsia that they don't know about.

One service per ask. Two becomes a pitch.

> "Did you know we also do ISO 21434 cybersecurity assessments?"
> "Did you know we've got a platform now that automates requirements traceability and compliance checking? It's called LiLA."

**LiLA is the standing DYK for every account.** It's Acsia's newest offering and the existing base largely doesn't know it exists.

### 2. Reverse Did You Know (rDYK)
**Purpose:** let the customer tell you what they need and currently buy elsewhere.

The highest-value action in the system, because the customer names the opportunity themselves — no guessing, no pitching.

> "What else are you working on that we might be able to help with?"
> "What are you giving to other vendors right now that we could take off your plate?"
> "Who else are you using for V&V on this program?"

Acsia's CRM already lists the likely answers under `Current ESP Vendors`: KPIT, Tata Elxsi, LTTS, Capgemini, GlobalLogic. The rDYK converts that field from a static note into an active conversation.

### 3. Pivot to Sale
**Purpose:** close what's being discussed right now.

> "Shall we scope that and get you a proposal this week?"
> "When would you want us to start?"
> "Want me to add that to the current SOW?"

### 4. Pivot to Next Conversation
**Purpose:** when there's nothing to close, secure the next contact.

Critical at Acsia specifically — with 9–18 month cycles, most conversations have no close available. This action is what keeps a long pursuit alive instead of letting it drift.

> "Can I come see you when I'm in Munich in March?"
> "Should we set something up after your platform decision in Q1?"

### 5. Percentage of Business Question
**Purpose:** ask for more while learning your actual share.

> "Roughly what share of your external engineering spend comes to us?"
> "Of the V&V work you outsource, how much is ours?"

Acsia has `Engineering Services Budget (USD)` on the account record, which gives you a denominator to sanity-check the answer against. Expect the real number to be far lower than the account owner assumes — see `06-wallet-share.md`.

### 6. Internal Referral Request
**Purpose:** reach more buyers inside the same customer.

Disproportionately valuable at Acsia. OEMs are federations of programs, divisions and geographies; Acsia's own ICP work found roughly **thirty buying-committee contacts per qualified account.** A delivery engineer trusted by one program lead is two sentences away from three more.

> "Which other programs inside Continental have the same problem?"
> "Who runs V&V for the commercial vehicle side?"
> "Is there anyone in your Bangalore centre I should be talking to?"

### 7. External Referral Request
**Purpose:** introductions to people outside the account.

> "Who else do you know dealing with the same AUTOSAR migration headache?"

Lower yield in automotive than in distribution — the industry is smaller and more guarded. Use it, don't lead with it.

**Scope note:** this is the one action that produces a *new logo*, which puts the result outside Outgrow's remit. Log the action, then **hand the referral to the AE and the outbound engine** — don't work it inside Outgrow. The action counts as a swing because asking is the behavior we want; the resulting pursuit belongs to the eight-stage process.

### 8. Communicating a Testimonial
**Purpose:** let a happy customer do the persuading.

Pull directly from the recordings in `02-happy-customer-interviews.md`. Works by phone or message.

> "We just wrapped a functional safety programme at another Tier-1 — their architecture lead said it was the first time an external team understood their toolchain without three months of ramp-up. Thought of you because you're facing the same thing."

---

## The three-part call

**1. Open — human.**
> "Hi Klaus, I was thinking about you. How's the family? How was the summer break?"

*"I was thinking about you"* is doing real work. It signals the call was deliberate and the person mattered enough to plan for.

**2. Shift to business — DYK and rDYK.**
> "What are you working on right now that I could help with?"
> "Anything going to other vendors that we could take?"
> "We've been doing a lot of ISO 21434 work lately — is that on your roadmap?"

**3. Pivot — sale, or next conversation.**
> "When would you want us to start?" / "Can I come see you in March?"

## The rule that carries the whole system

**Every customer interaction gets a "what else" and a "when."**

One reverse Did You Know. One pivot. That's it. It applies to proactive calls, on-site visits, program reviews, and — importantly — **inbound calls too**. When a customer calls about a defect, the conversation still ends with "what else is going on?" and "when should we talk next?"

Simple enough that an engineer can hold it without a card. That's why it's the rule.

## Stacking

A single conversation can carry several actions: two Did You Knows, a reverse Did You Know, a pivot. Four logged actions from one call already happening. Stacking is how volume gets built without adding time — teach it explicitly, because people default to one action per conversation.

## Voicemail protocol

Most calls will not be answered. That's expected — the voicemail *is* the action, not a failed attempt at one.

- **Twelve seconds.** Longer doesn't get listened to.
- **Written to be read as a transcript**, because that's how most people consume it.
- **Include "I was thinking about you."**
- **Offer a premise of value** — market intelligence, something you saw, something relevant to their program.
- **Always follow with a text**, immediately, referencing the voicemail.

> "Klaus, it's Priya from Acsia. I was thinking about you — saw the announcement about your new E/E architecture programme and had a thought that might be useful. Give me a call when you get a chance."

Because most calls end here, three calls take under five minutes.

## Channel substitution by geography

**This is Acsia's most important deviation from the book.**

The book says email is never an Outgrow action, and prescribes call → voicemail → text. That is right in its native context and would be actively counterproductive if applied literally to a German OEM contact.

What the doctrine is actually protecting: **synchronous or near-synchronous, low effort for the sender, unexpected, personal, and hard to ignore.** Preserve those properties; swap the channel.

| Geography | Primary | Follow-up | Avoid |
|---|---|---|---|
| **India** | Phone call | WhatsApp | — |
| **US** | Phone call | SMS | — |
| **Germany** | Call to desk/mobile during business hours; Teams message if an existing working relationship | Teams | Unsolicited SMS to personal mobiles; be careful with personal data generally |
| **Japan** | Existing meeting cadence, in person or scheduled video; introductions through the known contact | Formal follow-up message | Cold calls and unexpected mobile contact |
| **South Korea** | Call within an existing relationship; KakaoTalk where already used | KakaoTalk | Cold mobile contact |
| **France / Italy / Sweden** | Phone call | Email acceptable as follow-up only | — |

Two standing rules regardless of geography:

**On-site beats everything.** When an Acsia engineer is physically at the customer, that conversation is worth more than any call and costs nothing extra. The prompt card exists for exactly this.

**Email is never the action itself.** It can confirm or follow up. If someone's logged actions are all email, the program has quietly reverted to what it was replacing — flag it.

## When to make the calls

First thing in the morning, before the day fills up. The first call is the hardest and it gets easier immediately after — which is the actual reason for the timing rule.
