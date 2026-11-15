---
name: "superpowers-code-review"
description: "Use when finishing a task or feature, before merging, or when receiving review feedback: request a fresh reviewer with the right brief, and evaluate feedback with rigour instead of performative agreement."
---

# Code Review: requesting and receiving (from obra/superpowers, MIT licence; merges requesting-code-review and receiving-code-review)

## Part 1: Requesting review
**Core principle:** review early, review often. The reviewer gets precisely crafted context, never your session history.

**Mandatory:** after each task in subagent-driven development, after a major feature, before merge to main. **Valuable:** when stuck, before refactoring, after a complex bug fix.

1. Get the range: `BASE_SHA=$(git merge-base origin/main HEAD)` (or the task's recorded BASE), `HEAD_SHA=$(git rev-parse HEAD)`.
2. Dispatch a general-purpose reviewer subagent with this brief:

```
You are a Senior Code Reviewer. Review completed work against its plan or requirements and find issues before they cascade.
What was implemented: [DESCRIPTION]
Requirements / plan: [PLAN_OR_REQUIREMENTS]
Range: base [BASE_SHA], head [HEAD_SHA] — git diff --stat and git diff for the range.
The spec is a vision document: for behaviour it is silent on, judge by what a reasonable person using this software would expect. Grade findings by their effect on that person, not by whether the spec mentions the trigger.
Before your verdict, list under "Declined to judge" every behaviour you considered and set aside as out of scope, one line each with the reason.
Read-only: never change the working tree, index, HEAD or branch; use git show/diff/log, or a separate temporary worktree for other revisions.
Do all the review yourself; never dispatch subagents.
Report: Strengths; Issues grouped Critical / Important / Minor, each with file:line, what's wrong, why it matters, how to fix; Declined to judge; Assessment (ready to proceed / needs fixes).
```

3. Act: fix Critical immediately, Important before proceeding, note Minor for later, push back with reasoning if the reviewer is wrong.

Never skip review because "it's simple", ignore Critical, or proceed with unfixed Important. Don't review the diff inline yourself instead: it burns the context you need to drive the work.

## Part 2: Receiving review
**Core principle:** verify before implementing, ask before assuming, technical correctness over social comfort.

**Pattern:** READ all of it without reacting → UNDERSTAND (restate or ask) → VERIFY against the codebase → EVALUATE for THIS codebase → RESPOND (technical acknowledgement or reasoned pushback) → IMPLEMENT one item at a time, testing each.

**Never:** "You're absolutely right!", "Great point!", "Excellent feedback!", "Thanks for...", or "Let me implement that now" before verifying. Instead restate the requirement, ask, push back, or just start working. When feedback is correct: "Fixed. [what changed]" or "Good catch - [issue]. Fixed in [location]."

**Unclear items:** if any item is unclear, implement nothing yet; ask about the unclear ones first ("Understand 1, 2, 3, 6. Need clarification on 4 and 5."). Items may be related.

**By source:** your human partner is trusted (implement after understanding; still ask if scope is unclear). External reviewers: check it's correct for this codebase, doesn't break things, respects the reason for the current code, works on all platforms, and that they have full context. Can't verify → say so and ask. Conflicts with your partner's earlier decisions → stop and discuss.

**YAGNI check:** reviewer asks to "implement properly"? Grep for real usage. Unused → "Nothing calls this. Remove it (YAGNI)?"

**Order:** clarify first; then blocking issues (breaks, security), simple fixes, complex fixes; test each; check for regressions.

**Push back when** it breaks functionality, the reviewer lacks context, it's YAGNI, it's wrong for this stack, legacy/compat reasons exist, or it conflicts with your partner's architecture. Use technical reasoning, specific questions, working tests. If you were wrong: "You were right - I checked X and it does Y. Implementing now." No long apology.

**GitHub:** reply to inline comments in their thread, not as a top-level PR comment.