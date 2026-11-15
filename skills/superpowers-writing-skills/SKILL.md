---
name: "superpowers-writing-skills"
description: "Use when creating a new skill, editing an existing one, or checking a skill works before relying on it: apply test-first discipline to process documentation."
---

# Writing Skills (from obra/superpowers, MIT licence, adapted)

**Writing skills IS test-driven development applied to process documentation.** Write test cases (pressure scenarios run by subagents), watch them fail (baseline behaviour without the skill), write the skill, watch them pass, then refactor to close loopholes. Background: superpowers-test-driven-development.

**Core principle:** if you didn't watch an agent fail without the skill, you don't know if the skill teaches the right thing.

In this app, save skills through the skill proposal card; skill files on disk are a read-only cache.

## What a skill is
A reusable reference for a proven technique, pattern, or tool. Not a narrative of how you solved something once.

**Create when** it wasn't intuitively obvious, you'd use it across projects, it applies broadly, others benefit. **Don't** for one-offs, well-documented standard practice, project-specific conventions (put those in instructions), or anything enforceable by regex/validation (automate it).

**Types:** technique (steps), pattern (way of thinking), reference (API/syntax docs).

## SKILL.md essentials
- Name: letters, numbers, hyphens only.
- `description` says only WHEN to use it: triggers and symptoms, starting "Use when...", third person, under 1024 chars. Never summarize the workflow in it (agents follow the summary instead of reading the skill).
- Clear overview with the core principle; keywords early (errors, symptoms, tools) for discovery.
- Inline principles and code under ~50 lines; separate files only for heavy reference (100+ lines) or reusable scripts. Invoke scripts via their interpreter (`bash scripts/x.sh`).
- One excellent, runnable, real example in the most relevant language. No multi-language dilution, no fill-in templates, no code inside flowcharts, no generic labels.
- Small flowchart only when a decision is non-obvious. Quick-reference table. Common mistakes.

## The Iron Law
```
NO SKILL WITHOUT A FAILING TEST FIRST
```
Applies to new skills AND edits. No exceptions for "simple additions" or "documentation updates".

## Testing by type
- **Discipline skills** (rules): academic questions, pressure scenarios, combined pressures (time + sunk cost + exhaustion + authority). Success = complies under maximum pressure.
- **Technique skills:** application and variation scenarios, missing-information tests.
- **Pattern skills:** recognition, application, counter-examples (when NOT to apply).
- **Reference skills:** retrieval and application scenarios, gap tests.

## Match the form to the failure
| Baseline failure | Right form | Wrong form |
|---|---|---|
| Breaks a rule under pressure | Prohibition + rationalization table + red flags | Soft "prefer/consider" |
| Complies but output has the wrong shape | Positive recipe: state what the output IS, its parts in order | Prohibition list |
| Omits a required element | REQUIRED field/slot in the template | Prose reminders |
| Behaviour depends on a condition | Conditional on an observable predicate | Rule + exemption clauses |
No nuance clauses ("don't X unless it matters") — they reopen negotiation. Exemption clauses don't scope; restructure instead.

## RED-GREEN-REFACTOR
- **RED:** run the scenario with a subagent WITHOUT the skill. Record choices and rationalizations verbatim.
- **GREEN:** write the minimal skill addressing those exact failures. Re-run with the skill; it should comply.
- **REFACTOR:** new rationalization? Add an explicit counter. Re-test until bulletproof.
- **Micro-test wording first:** one fresh-context sample per call with realistic surrounding context; always a no-guidance control (if the control doesn't fail, there's nothing to fix); 5+ reps per variant; read every flagged match yourself; converging outputs mean the wording binds.

## Rationalizations for skipping tests
"Obviously clear", "just a reference", "overkill", "I'll test if problems emerge", "I'm confident", "academic review is enough" — all mean: test before deploying.

## Checklist (one todo each, per skill; never batch untested skills)
- RED: pressure scenarios (3+ combined for discipline skills); run without the skill; note patterns.
- GREEN: valid name; frontmatter; "Use when..." description; keywords; core principle; addresses observed failures; form matches failure; wording micro-tested vs control; one example; re-run with the skill.
- REFACTOR: new rationalizations countered; rationalization table; red flags; re-test.
- Quality: flowchart only if needed; quick reference; common mistakes; no storytelling.
- Deploy: save it (proposal card or commit); consider contributing back.