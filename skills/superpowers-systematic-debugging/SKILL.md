---
name: "superpowers-systematic-debugging"
description: "Use when hitting any bug, test failure, build failure or unexpected behaviour, before proposing a fix: find the root cause first."
---

# Systematic Debugging (from obra/superpowers, MIT licence)

**Core principle:** ALWAYS find the root cause before attempting fixes. Symptom fixes are failure. Violating the letter of this process is violating the spirit of debugging.

## The Iron Law
```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```
If you haven't completed Phase 1, you cannot propose fixes.

Use for ANY technical issue: test failures, production bugs, unexpected behaviour, performance, build failures, integration issues. Use it ESPECIALLY under time pressure, when "one quick fix" seems obvious, when you've already tried fixes, or when you don't fully understand the issue.

## Phase 1: Root Cause Investigation
1. **Read error messages carefully.** Full stack traces, line numbers, file paths, codes.
2. **Reproduce consistently.** Exact steps. If not reproducible, gather more data; don't guess.
3. **Check recent changes.** Diffs, commits, new dependencies, config, environment.
4. **Gather evidence across components.** In multi-layer systems (CI → build → signing, API → service → DB), log what enters and exits each boundary and check config propagation. Run once to see WHERE it breaks, then investigate that layer.
5. **Trace data flow backwards.** Where does the bad value originate? What called this with it? Keep tracing up. Fix at the source, not the symptom.

## Phase 2: Pattern Analysis
1. Find similar working code in the same codebase.
2. If implementing a pattern, read the reference implementation COMPLETELY.
3. List every difference between working and broken, however small.
4. Understand dependencies: components, settings, environment, assumptions.

## Phase 3: Hypothesis and Testing
1. State one hypothesis: "I think X is the root cause because Y."
2. Make the SMALLEST change to test it. One variable at a time.
3. Worked → Phase 4. Didn't → form a NEW hypothesis. Don't stack fixes.
4. When you don't know, say "I don't understand X". Research or ask.

## Phase 4: Implementation
1. **Create a failing test case** reproducing the bug (automated if possible, a one-off script if not). Must exist before fixing. Use superpowers-test-driven-development.
2. **Implement a single fix** for the root cause. No "while I'm here" changes.
3. **Verify:** test passes, nothing else broke, issue resolved. Use superpowers-verification before claiming success.
4. **If the fix doesn't work:** STOP. Fewer than 3 attempts → back to Phase 1 with new info. **3 or more → question the architecture.**
5. **3+ failed fixes = wrong architecture**, not a failed hypothesis: each fix reveals new coupling elsewhere, or needs massive refactoring. Discuss with your human partner before attempting more.

## Red Flags: STOP, return to Phase 1
- "Quick fix for now, investigate later"
- "Just try changing X and see"
- "Add multiple changes, run tests"
- "Skip the test, I'll manually verify"
- "It's probably X"
- "I don't fully understand but this might work"
- Proposing solutions before tracing data flow
- "One more fix attempt" after 2+ failures

Your partner's signals you're doing it wrong: "Is that not happening?" (you assumed), "Will it show us...?" (add evidence), "Stop guessing", "We're stuck?". STOP and return to Phase 1.

## Rationalizations
| Excuse | Reality |
|---|---|
| "Issue is simple" | Simple issues have root causes too. The process is fast for them. |
| "Emergency, no time" | Systematic is faster than thrashing. |
| "I'll write the test after" | Untested fixes don't stick. |
| "Multiple fixes at once saves time" | You can't isolate what worked. |
| "Reference too long, I'll adapt" | Partial understanding guarantees bugs. |
| "I see the problem" | Seeing symptoms is not understanding the cause. |

## Quick Reference
| Phase | Activities | Done when |
|---|---|---|
| 1. Root cause | Read errors, reproduce, check changes, gather evidence | You know WHAT and WHY |
| 2. Pattern | Find working examples, compare | Differences identified |
| 3. Hypothesis | One theory, minimal test | Confirmed or replaced |
| 4. Implementation | Failing test, single fix, verify | Bug gone, tests pass |

## Supporting techniques
- **Condition-based waiting:** replace arbitrary sleeps/timeouts with polling for the actual condition.
- **Defence in depth:** after finding the root cause, add validation at the layers the bad value passed through.
- If investigation shows it's truly environmental or timing-dependent: document what you checked, add handling (retry, timeout, clear error) and logging. But 95% of "no root cause" cases are incomplete investigation.