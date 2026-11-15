# Approved claims

This is the only list of numbers, quotes and credentials that may appear in LiLA marketing or sales copy. Each entry says where it came from and how it may be worded. Anything not here gets left out or marked `[VERIFY: source?]`.

**Why this is strict:** the buyers are safety and quality engineers. Their job is to find gaps in evidence. A number that can't be traced back to a real measurement reads as a vendor making things up, and it taints every true claim next to it.

Last reviewed: 30 Oct 2026, against LiLa Pitch Deck v5.1 (14 Oct 2026), Coda "Lila Investor Readiness", Coda "Acsia FY27 Revenue Engine".

---

## Status key

- **CLEARED** - use externally as worded.
- **INTERNAL** - fine for sales conversations and internal docs, not for public pages, ads or posts.
- **INVESTOR-ONLY** - do not use in any marketing or sales output.
- **DO NOT USE** - known to be wrong or contradictory.

---

## Platform-level results

| Claim | Allowed wording | Source | Status |
|---|---|---|---|
| Productivity across the SDLC | "Customers have seen 60-85% productivity gains across the development lifecycle." Always as an observed range, never a promise or guarantee. | Deck v5.1 | CLEARED |
| Engineering time saved | "60%+ engineering time savings" | Deck v5.1 | CLEARED |
| 100-page requirements spec | "On a 100-page requirements document, LiLA cut the effort by 69%." | Deck v5.1, slide 12 | CLEARED |
| Where engineering effort goes | "In regulated programs, 60-70% of engineering effort goes to compliance, QA and documentation. Only 30-40% is coding and architecture." Attribute to Acsia's own delivery experience. | Deck v5.1, slide 4 | CLEARED with attribution |

## Agent-level results

| Agent | Allowed wording | Source | Status |
|---|---|---|---|
| TestFlow - test case generation | "Cuts test case creation time by 98%." The "68x faster" form is equivalent and allowed. | Coda Feature Matrix ("currently") + deck | CLEARED |
| TestFlow - test scripts | "Writes up to 70% of Python test scripts. The remaining 30% is hardware- or environment-specific and stays with your engineers." | Coda TestFlow positioning | CLEARED |
| TestFlow - CI/CD | "Around 60% time savings in CI/CD workflows." | Coda Feature Matrix ("currently") | CLEARED |
| TestFlow - coverage | "Bi-directional traceability between requirements and test cases." Don't say "guarantees 100% coverage" - the Coda positioning says it, but a guarantee is a liability claim. | Coda TestFlow positioning | CLEARED as reworded |
| FixFlow - root cause analysis | "Over 70% RCA accuracy, where tools on the market rarely pass 40%." This comes from a customer quote, so attribute it as "a customer reported". | Deck v5.1 testimonial | INTERNAL until testimonial is cleared |
| ProcureFlow / DocuFlow - RFQ evaluation | "Turns a week-long RFQ evaluation into a few hours." | Deck v5.1 testimonial + Coda Feature Matrix | INTERNAL until testimonial is cleared |
| SpecFlow -40%, CodeFlow -60%, FixFlow -40% triage / -25% support cost, SafeFlow -50% audit prep, DocuFlow +50% | Not cleared. These appear only in the May 2026 project brief with no measurement behind them. | Project brief | DO NOT USE until a source is found |

## ROI

| Claim | Allowed wording | Source | Status |
|---|---|---|---|
| SaaS payback | "Modelled at 15-25x return in the first year." Always say "modelled". It's a projection, not a customer result. | Deck v5.1, slide 19 | INTERNAL (sales conversations, proposals) |
| Business tier ~25x / $270K savings | Superseded by the 15-25x range above. | Project brief | DO NOT USE |

## Industry context (needs a public citation in external copy)

| Claim | Rule |
|---|---|
| "A modern car runs on over 100 million lines of code" / "more than a Boeing 787" | Widely published. Cite a named public source with a date in any public asset. |
| "Vehicle software triples by 2030" / "300M+ lines by 2030" | Cite a named public source with a date, or drop it. |
| ASPICE Level 3 becoming a contractual requirement from OEMs | Fine as a market observation. Don't attach a percentage or date without a source. |
| ISO/SAE 21434 and UNECE R155 cybersecurity requirements | Fine as fact. Don't overstate scope. |

## Customer quotes and logos

All four testimonials in Deck v5.1 are **INVESTOR-ONLY** until Acsia confirms written permission for public and sales use. Named quotes from BMW, ECARX and Panasonic employees can't go into marketing without their consent.

| Quote topic | Name and company as shown in deck | Agent (inferred from deck order - confirm) |
|---|---|---|
| RFQ proposal validation, week to hours | Christina Hein, BMW | ProcureFlow |
| Requirements and document classification | Uwe de Nardi, ECARX | SpecFlow |
| RCA over 70% accuracy | Richard Bogenberger, BMW | FixFlow |
| Test case generation for Ethernet switch testing | Marwan Hage, Panasonic Automotive | TestFlow |

**Until cleared,** use the substance without names: "An OEM's procurement team cut RFQ evaluation from a week to a few hours." Even this is INTERNAL - it's a real result, but an unnamed quote on a public page reads as invented.

**Logos.** Acsia's services logo wall (BMW, VW Group, Mercedes, Nissan, Ford, Visteon, Magna, Panasonic and others) proves Acsia's engineering track record. It does **not** mean those companies use LiLA. Never place these logos next to LiLA claims in a way that implies they're LiLA customers. Logo use in any public asset needs Acsia's approval.

## Acsia credentials

| Claim | Status |
|---|---|
| ASPICE CL3, TISAX AL3, ISO 26262 up to ASIL-D | From the FY27 Revenue Engine plan. The deck origin story says Acsia was "achieving ASPICE Level 2" when they built LiLA. **Confirm the current certification levels with Acsia before first external use**, then mark CLEARED here. |
| "Over a decade delivering safety-critical software for leading automotive OEMs" | CLEARED (Deck v5.1) |
| "Built by automotive engineers, for industries where software failure is not an option" | CLEARED - this is the tagline |

## Claims that need special care

**Offline and on-prem.** LiLA is sold as SaaS *and* as an on-prem perpetual license. Only the on-prem model runs fully offline. Say "Deploy fully on-premise and offline, on your own infrastructure" when talking about on-prem. Never say "LiLA is 100% offline" or "zero data leakage" as a blanket claim.

**Certification and tool qualification.** Do not say LiLA is certified, qualified, assessor-approved or "guarantees compliance." Under ISO 26262 Part 8, software tools used in safety work need their own tool classification and qualification - that's the customer's process, and a vendor claiming it for them is a red flag to any FuSa engineer. Allowed: "Generates artifacts with ASPICE and ISO 26262 attributes attached, for your engineers to review." Human review is a feature here, so say it.

**"Guarantees."** The Coda positioning drafts use "guarantees ISO 26262/ASPICE compliance" and "guarantees 100% coverage." Don't carry these into copy. Replace with what LiLA does: attaches standard attributes, maintains traceability, flags gaps.

**Integrations.** Engineering tools seen in customer stacks: Jira, Polarion, IBM DOORS, Codebeamer, Jenkins, GitLab CI, Azure DevOps, JFrog, VS Code, PyCharm, dSPACE. Say LiLA "works alongside" these. Only name a specific native integration if Acsia confirms it exists. `[VERIFY]` any integration claim in public copy.

**Market sizing and financials.** TAM/SAM/SOM, revenue projections, customer counts, the $5M raise - all INVESTOR-ONLY. They never go into marketing or sales copy.

## Known contradictions - do not use either side

| Issue | Detail |
|---|---|
| 100-page spec proof point | Deck says 69% saving. A July LinkedIn draft says "30 days to 11 hours", which would be ~95%. Use 69% only. |
| Team output multiplier | Deck slide 13 says "100 today, 160-185 with LiLA" and calls it "a team 40% larger." 160-185 is 60-85% larger. Don't use this slide's numbers until Acsia fixes it. |
