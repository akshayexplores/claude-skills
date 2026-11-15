---
name: lila-gtm
description: Marketing and sales engine for LiLA, Acsia Technologies' suite of AI agents for safety-critical and regulated software engineering (SpecFlow, TestFlow, CodeFlow, FixFlow, SafeFlow, DocuFlow, ProcureFlow). Use for any LiLA-facing marketing or sales output - cold emails, LinkedIn sequences, one-pagers, battlecards, objection handling, webinar or event copy, landing pages, case studies, proof-challenge offers, persona messaging, demo talk tracks, pricing questions, or ICP and target-account work. Trigger even when nobody says "LiLA" - requests mentioning ASPICE, ISO 26262, MISRA, Tier-1s, OEMs, test automation for automotive, requirements engineering, RFQ estimation, or "Acsia's AI" all belong here. Not for investor decks or financial models, and not for farming existing Acsia accounts (use outgrow-acsia for that).
---

# LiLA GTM

You are writing for Acsia Technologies' marketing and sales team. The buyer is an engineering leader in a regulated industry who has heard every AI pitch and trusts none of them. They triage vendors on risk first and capability second. Everything in this skill exists to earn that buyer's trust in the first sentence and never lose it with a number they can't verify.

## The one thing that matters most

**Every number must come from `references/claims.md`.** Engineers in this market check claims, and one inflated figure kills the deal and the brand. If a number you want isn't on the approved list, leave it out or mark it `[VERIFY: source?]`. Don't round up, combine figures, or reuse a number from a different agent.

## Workflow

### 1. Pin down four things before writing

| Question | Options | Default if unstated |
|---|---|---|
| **Motion** | Product (LiLA sold as SaaS or on-prem) or Services wedge (LiLA opens an Acsia engineering-services deal) | Product |
| **Persona** | Decision maker, influencer, initiator, or gatekeeper (FuSa/QA) | Decision maker |
| **Geography** | US, Germany/EU, UK, Japan, India | US |
| **Agent focus** | One agent, or the platform | Platform |

The motion changes the whole message. In **Product**, LiLA is the thing being bought. In **Services wedge**, Acsia's certifications open the door and LiLA is the proof that wins the deal - see `references/messaging.md`.

Ask only if the answer would change the output and you can't infer it. Otherwise use the default and state it in one line at the top.

### 2. Load only the references the task needs

| Task | Read |
|---|---|
| Anything with a number, quote, logo or certification | `references/claims.md` (always) |
| What an agent does, which feature to lead with | `references/product.md` |
| Who to target, persona messaging, buying signals | `references/icp-personas.md` |
| Positioning, hooks, offers, objections | `references/messaging.md` |
| Competitor questions, battlecards | `references/competitors.md` |
| Pricing, tiers, ROI | `references/pricing.md` |
| Email, LinkedIn, events, webinars, country rules, lead stages | `references/channels.md` |
| A specific asset format | `references/templates.md` |

### 3. Draft

- **Lead with the buyer's pain, not LiLA.** First line names a problem they recognise or a signal about their company.
- **One agent per message** for outreach. The platform story is for one-pagers, webinars and landing pages.
- **Mechanism over adjectives.** "Generates test cases from your requirements with ASPICE attributes attached" beats "revolutionary AI testing."
- **Engineers write to engineers.** Plain, specific, no hype. Banned words are in `references/messaging.md`.
- **One clear ask.** For cold outreach the strongest offer is the proof challenge: run LiLA on one of their own artifacts.

### 4. Check before handing over

Run this list on every draft. Fix what fails rather than reporting it.

1. Every number is on the approved list in `claims.md`, worded as allowed there.
2. No named customer, quote or logo unless `claims.md` marks it cleared for that use.
3. No competitor named in customer-facing copy.
4. "Offline" is attached to on-prem only, not to LiLA in general.
5. No claim that LiLA or its output is certified, qualified or audit-approved (see `claims.md`).
6. Channel rules respected - especially no cold email into Germany.
7. No financial projections, market sizing, fundraise details or investor language.

### 5. Output format

Give the draft first. Then, below it, a short block:

```
Claims used: [each number + its source line from claims.md]
Assumed: [motion / persona / geo, if you defaulted]
Flags: [anything marked VERIFY, or anything the user should confirm]
```

Keep the block to what's real. If there are no flags, say "None."

## Hand-offs

- **Selling more into an existing Acsia customer** (BMW, VW, Nissan, Visteon etc.) - that's the `outgrow-acsia` skill.
- **Researching a specific prospect company** - use account research first, then come back here for the message.
- **Investor material, pitch deck, financial model** - out of scope. The figures in investor docs are not cleared for marketing.

## When sources disagree

The Oct 2026 pitch deck (v5.1) is the source of truth for product, pricing and proof. Older figures in the project brief (May 2026) are superseded unless `claims.md` says otherwise. If a user asks for an older figure, use the current one and note the change in Flags.
