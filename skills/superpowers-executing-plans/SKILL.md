---
name: "superpowers-executing-plans"
description: "Use when executing an approved implementation plan yourself in this session, task by task, with a progress ledger, tests per task and one fresh review at the end."
---

# Executing Plans (from obra/superpowers, MIT licence, adapted)

Execute the plan yourself, task by task, in this session: no implementer subagent per task, no reviewer per task, one fresh-context review of the whole result at the end.

**Why inline:** it pays for one context plus one final reviewer. What a fresh context per task bought is kept by other means: the task text is the spec, the ledger is your memory, TDD is the per-task gate, the final reviewer is the second pair of eyes.

**Core principle:** The plan already did the thinking. Execute it exactly, prove each step with a test you watched fail then pass, and leave a record that survives your own forgetting.

- **Narration:** at most one short line between tool calls.
- **Continuous execution:** don't pause to check in between tasks.
- **Rulings, not stalls.** Decide conflicts, ambiguities and plan defects. The spec is binding, the plan is its argument, your judgment settles the rest. Ledger every decision as `Ruling: <what> — <why> — <cost if wrong>`. Deviating without a ledgered ruling is a decision made in secret.
- **Only four things stop you:** an irreversible or destructive operation; a security-sensitive action; a side effect outside this workspace that norms say to ask about (merge, push to a shared branch, publish, deploy, sending anything); a plan so broken every path is a guess. For those, stop and ask.

Prefer superpowers-subagent-driven-development when your partner wants a review gate on every task, or the plan is long enough that later tasks would run on a compacted context.

## Setup
1. Work in an isolated workspace (superpowers-git-worktrees). Never implement on main/master without explicit consent.
2. **Ledger:** create `.superpowers/sdd/<plan-basename>/progress.md` (git-ignored) with first line `# SDD ledger — plan: <plan path>`. If one already exists naming this plan, tasks with `Task <N>: complete` are DONE: resume at the first task without one. After compaction, trust the ledger and `git log` over memory. A ledger naming a different plan isn't yours.
3. Read the plan once and its Spec if named (no reachable spec: note it; rulings are provisional). Note Global Constraints. One todo per task.
4. Load superpowers-test-driven-development now; it governs every step.
5. **Pre-flight scan:** for every task that consumes what an earlier task produces (see Interfaces blocks), one ledger row: the two tasks, produced vs consumed, what you found. Rule on conflicts against the spec. No shared interfaces → `Pre-flight: no shared interfaces`.

## Task loop
Keep long output out of context: redirect test output to a file in the workspace and read its tail.
1. **Take the task:** record BASE (`git rev-parse HEAD`). Re-read the task's own text from the plan even if you remember it; memory is a summary, the text has exact values. Mark todo in progress.
2. **Work the steps** in RED-GREEN order. Every command step has an `Expected:` line: run, read, compare.
   - Matches → next step.
   - Code wrong → superpowers-systematic-debugging; never patch the symptom to match.
   - Plan wrong (contradicts the spec, interface mismatch, impossible command) → smallest change that satisfies the spec, ledger `Task <N>: Ruling: ...`, continue.
   Commit as the plan says. Bookkeeping rides with work: ledger append in the same call as the commit.
3. **Completion contract** (evidence in this session, not inferred): every named test exists and ran and you read the output; the final test run passed; every `Expected:` was compared to real output; every deviation has a Ruling line. Governed by superpowers-verification.
4. **Complete:** run the task's test command, save full output to the workspace, read the tail; only if it passes append `Task <N>: complete (commits <base7>..<head7>, tests: <command> → <result>)`. Mark todo complete.

## Final review
- Build a review package: `git log --oneline BASE..HEAD`, `git diff --stat`, `git diff -U10` for the whole range, into one file.
- **With a subagent tool:** dispatch a reviewer on the most capable model, with the package path, plan and spec paths, the plan's Review Focus verbatim, and a pointer to the ledger's Ruling lines. Use the code-reviewer brief in superpowers-code-review. Don't skip it or replace it with your own read.
- **Without one:** do that review yourself as a separate pass; ledger `Final review: self-review (no subagent tool)` and say so.
- **Re-grade findings by effect** on a reasonable person using the software (spec silence is not permission). Every "declined to judge" line is a ruling you make and ledger.
- **Critical/Important:** fix in ONE pass, each fix TDD (reproducing test RED → GREEN), then whole suite. Ledger `Final: fixed <finding> — <test> RED→GREEN, suite N/N`. Not fixing = a ruling.
- **Minor:** ledger `Final: minor (deferred): ...`; never fix unasked.

## Finish
Final message lists every `Ruling:` under "Rulings I made" (with cost if wrong) and every deferred minor under "Deferred minors". Then delete this plan's workspace dir and use superpowers-finishing-branch.

## Rationalizations
| Excuse | Reality |
|---|---|
| "I remember what Task N says" | Re-read it. Exact values live there. |
| "Skip watching the test fail" | A test never seen failing proves nothing. |
| "I'll write ledger lines later" | Compaction doesn't wait. One line per task. |
| "Check in before the next task" | Only the four stops stop you. |
| "My own read replaces the final reviewer" | Same author, same blind spots. |
| "Reviewer said Minor" | Re-grade by effect, then gate. |
| "Obvious fix, no failing test" | The failing test is the only proof. |
| "Fix the minors too" | Your partner decides. Ledger them. |