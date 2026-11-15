---
name: "superpowers-subagent-driven-development"
description: "Use when executing an implementation plan of mostly independent tasks with a fresh implementer subagent and a reviewer per task, plus a whole-project review at the end."
---

# Subagent-Driven Development (from obra/superpowers, MIT licence, adapted)

Execute a plan by dispatching a fresh implementer subagent per task, a task review (spec compliance + code quality) after each, and a broad whole-project review at the end. Subagents get exactly the context you build for them, never your session history; that also keeps your context for coordination.

**Core principle:** fresh subagent per task + task review + broad final review = high quality, fast iteration.

- **Narration:** one short line between tool calls. **Continuous:** no check-ins between tasks.
- **Rulings, not stalls:** decide conflicts and defects; ledger `Ruling: <what> — <why> — <cost if wrong>`.
- **Only four stops:** irreversible/destructive operation; security-sensitive action; outside side effect norms say to ask about (merge, shared push, publish, deploy, sending); a plan so broken every path is a guess.

Use when you have a plan, tasks are mostly independent, and a subagent tool exists. Tightly coupled tasks → execute manually or brainstorm first. Partner chose inline, or no subagent tool → superpowers-executing-plans.

## Setup
- Isolated workspace (superpowers-git-worktrees); never implement on main without consent.
- Ledger at `.superpowers/sdd/<plan-basename>/progress.md`, first line `# SDD ledger — plan: <plan path>`. Existing ledger for this plan → resume at the first task without `Task <N>: complete`. Trust ledger + `git log` over memory (controllers that lost their place have re-dispatched whole completed sequences, the most expensive failure seen).
- Read the plan and spec once, note Global Constraints, one todo per task.
- Pre-flight conflict scan of producer/consumer interfaces between tasks; rulings in the ledger.

## Model selection (always specify the model; omitted = session's most expensive)
- Plan text contains the complete code (transcription + tests), or single-file mechanical fix → cheapest tier.
- Multi-file integration, prose-only specs, reviewers → mid tier as the floor (cheap models take 2-3x the turns).
- Design judgment, broad codebase understanding, the final whole-project review → most capable.
- Fix-loop rounds 4-5 → one tier above the stuck implementer.

## Task loop
1. **Dispatch the implementer.** Record BASE (`git rev-parse HEAD`). Extract the task's full text to a brief file (`.../task-N-brief.md`). Dispatch with: one line on where the task fits; the brief path ("read this first — your requirements, exact values verbatim"); interfaces and decisions from earlier tasks the brief can't know; your resolution of any ambiguity; a report path (`.../task-N-report.md`). The implementer writes the full report there and returns only status, commits, a one-line test summary and concerns. Never paste prior-task history. Implementers never dispatch subagents or reviewers. Never run implementers in parallel. Record the agent id for fix rounds.
2. **Handle the report.** DONE → review. DONE_WITH_CONCERNS → read the concerns and decide (ruling). NEEDS_CONTEXT → supply it and resume the same agent. BLOCKED → find out why; fix the plan with a ruling or re-dispatch with more context. Answer questions fully.
3. **Review the task.** Write a review package file (`git log --oneline BASE..HEAD`, `git diff --stat`, `git diff -U10`; never `HEAD~1`). Dispatch a reviewer with three paths (brief, report, package) and the binding global constraints copied verbatim. The reviewer must return BOTH verdicts: spec compliance (nothing more, nothing less) and quality; treat the implementer's report as unverified claims; read-only; doesn't re-run the suite or dispatch subagents. Never pre-judge findings ("don't flag", "at most Minor"). For "cannot verify from diff" items, check them yourself before completing.
4. **Fix loop** (spec ❌, any Critical/Important, or a confirmed gap): rounds 1-3 resume the same implementer with the findings, then a scoped re-review of the fix diff; rounds 4-5 escalate the model. Past the cap, stop looping: adjudicate each open finding with a ledgered ruling (park or route) and move on. New findings on untouched code go to the ledger, not the loop.
5. **Complete:** ledger `Task <N>: complete (commits <base7>..<head7>, review clean)` or `..., <K> parked`. Never move on with open Critical/Important that are neither fixed nor parked with a ruling.

**Waiting on subagents:** keep doing local work; when idle, wait in bounded stretches (5-10 min), post one status line, and chase any child that finished without reporting.

## Final review
Whole-project review on the most capable model (brief in superpowers-code-review), with the plan's Review Focus. Re-grade by effect; one fix wave for Critical/Important, each with a test RED→GREEN and a green suite; minors deferred to the ledger. Final message: "Rulings I made" and "Deferred minors", exhaustive. Delete the plan workspace, then superpowers-finishing-branch.

## Rationalizations
| Excuse | Reality |
|---|---|
| "Close enough on spec" | Fix or hit the cap and adjudicate. |
| "I'll fix it myself" | Pollutes your context, skips review. Resume the implementer. |
| "One more round will converge" | Past the cap it's structural. Adjudicate. |
| "This finding is obviously wrong, drop it" | Adjudicate only at the cap, always ledgered. |
| "Small fix, skip re-review" | Unreviewed fixes are how regressions land. |
| "Ledger is overhead" | It's what survives compaction. |
| "Implementer spawned its own reviewer, bonus" | Duplicate seat; flag it as a defect. |