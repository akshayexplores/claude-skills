---
name: "superpowers-writing-plans"
description: "Use when you have an approved spec or requirements for a multi-step build, before touching code, to write a bite-sized implementation plan with exact files, interfaces and tests."
---

# Writing Plans (from obra/superpowers, MIT licence, adapted)

Write implementation plans for an engineer who has not seen this codebase or this spec. Assume they write idiomatic code once they know the exact interface and the exact test, and will make a reasonable choice wherever the plan leaves one open. What they cannot know is what you decided: which files, which names and signatures, which values from the spec, which tests prove each task. Document those. Bite-sized tasks. DRY. YAGNI. TDD. Frequent commits.

**Announce at start:** "I'm using the writing-plans skill to create the implementation plan."

**Save plans to:** `docs/superpowers/plans/YYYY-MM-DD-<feature-name>.md` (user preferences for location override this).

## Scope Check
If the spec covers several independent subsystems, suggest one plan per subsystem. Each plan should produce working, testable software on its own.

## File Structure
Before defining tasks, map which files will be created or modified and what each is responsible for.
- Clear boundaries, well-defined interfaces, one responsibility per file.
- Prefer smaller, focused files. Files that change together live together. Split by responsibility, not technical layer.
- In existing codebases, follow established patterns.

## Task Right-Sizing
A task is the smallest unit that carries its own test cycle and is worth a reviewer's gate. Fold setup, config, scaffolding and docs into the task whose deliverable needs them. Split only where a reviewer could reject one task while approving its neighbour. Each task ends with an independently testable deliverable.

## Step Granularity
Each step is one action with a checkable result: write the failing test; run it to see it fail; implement the minimal code; run the tests and see them pass; commit.

## Plan Document Header

```markdown
# [Feature Name] Implementation Plan

**Goal:** [One sentence]
**Architecture:** [2-3 sentences]
**Tech Stack:** [Key technologies]
**Spec:** [path to the design doc this plan implements]

## Global Constraints
[Project-wide requirements from the spec, one line each, exact values verbatim.]

## Review Focus
[The five inputs or failure modes the spec implies but no task's tests exercise that are most likely to bite a real user, one line each with expected behaviour, most likely first. For each, add the test to the task that owns the code.]
```

## Task Structure

````markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file`
- Modify: `exact/path/to/existing:123-145`
- Test: `tests/exact/path/to/test`

**Interfaces:**
- Consumes: [what this uses from earlier tasks, exact signatures]
- Produces: [what later tasks rely on, exact names and types]

- [ ] Step 1: Write the failing test (name + assertions as code, with the spec's exact values)
- [ ] Step 2: Run it. Run: `<command>` Expected: FAIL with "..."
- [ ] Step 3: Implement `name(params) -> Return` in `path` (one line on approach if the test leaves a choice)
- [ ] Step 4: Run it. Expected: PASS
- [ ] Step 5: Commit
````

## What a Step Contains
A step is done when the implementer can write exactly one reasonable thing from it.
- **Test step:** the test's name and assertions, as code, with exact values.
- **Code step:** exact signature, file, and values the spec pins. A body only for an algorithm the signature and tests don't determine, or exact copy the spec fixes.
- **Verification step:** the command and the output that means it passed.
- **Reference to another task:** point at its Interfaces block; don't repeat its code.

A plan longer than the code it describes has written the code instead. Lines that decide nothing ("TBD", "handle edge cases", "add appropriate validation") are the opposite failure.

## Self-Review (run it yourself)
1. **Spec coverage:** every requirement maps to a task. Add tasks for gaps.
2. **Step scan:** no step decides nothing; no step transcribes a body the signature already determines.
3. **Type consistency:** names and signatures match across tasks.
4. **Review Focus:** each implied failure mode has a test in its owning task.
5. **Proportion:** if code blocks dominate, replace bodies with signatures and assertions.
Fix issues inline and move on.

## Execution Handoff
After saving and self-reviewing, link the plan and ask your partner to review it. Offer two ways to run it:
- **With reviewers:** a fresh subagent implements each task and a fresh reviewer checks it before the next starts, then a whole-project review. Most thorough, costs more.
- **Native:** implement every task yourself in this session, then one fresh reviewer checks the whole result. Cheapest and fastest.
Recommend one with a one-sentence reason (how interdependent the tasks are, how many, what a shipped mistake would cost). If they already said how to run it, just ask them to confirm the plan captures what they want. During execution, follow the plan task by task and use superpowers-verification before claiming any task is done.