---
name: "superpowers-verification"
description: "Use when about to claim work is complete, fixed, passing or ready, before committing, delivering or reporting success: run the proving check fresh and show the evidence first."
---

# Verification Before Completion (from obra/superpowers, MIT licence)

**Core principle:** Evidence before claims, always. Violating the letter of this rule is violating the spirit of this rule.

## The Iron Law

```
NO COMPLETION CLAIMS WITHOUT FRESH VERIFICATION EVIDENCE
```

If you haven't run the verification command in this message, you cannot claim it passes.

## The Gate Function

```
BEFORE claiming any status or expressing satisfaction:
1. IDENTIFY: What command or check proves this claim?
2. RUN: Execute the FULL check (fresh, complete)
3. READ: Full output, exit code, count failures
4. VERIFY: Does the output confirm the claim?
   - If NO: state the actual status with evidence
   - If YES: state the claim WITH evidence
5. ONLY THEN: make the claim
Skip any step = lying, not verifying
```

## Common Failures

| Claim | Requires | Not sufficient |
|---|---|---|
| Tests pass | Test output: 0 failures | Previous run, "should pass" |
| Linter clean | Linter output: 0 errors | Partial check |
| Build succeeds | Build command: exit 0 | Linter passing, logs look good |
| Bug fixed | Original symptom re-tested: passes | Code changed, assumed fixed |
| Regression test works | Red-green cycle verified | Test passes once |
| Agent completed | Diff shows the changes | Agent reports "success" |
| Page works | Opened in a real browser, looked at, console clean | "Code looks right" |
| Requirements met | Line-by-line checklist against the spec | Tests passing |

## Red Flags: STOP
- Using "should", "probably", "seems to"
- Expressing satisfaction before verification ("Great!", "Done!")
- About to commit, push, deliver or publish without verification
- Trusting agent success reports
- Relying on partial verification
- "Just this once"
- Any wording implying success without having run verification

## Rationalization Prevention

| Excuse | Reality |
|---|---|
| "Should work now" | RUN the verification |
| "I'm confident" | Confidence is not evidence |
| "Linter passed" | Linter is not the compiler |
| "Agent said success" | Verify independently |
| "Partial check is enough" | Partial proves nothing |
| "Different words so the rule doesn't apply" | Spirit over letter |

## Key Patterns
- Tests: run, see "34/34 pass", then say "all tests pass". Never "should pass now".
- Regression: write, run (pass), revert the fix, run (MUST fail), restore, run (pass).
- Build: run it, see exit 0, then say "build passes".
- Requirements: re-read the plan, make a checklist, verify each, report gaps or completion.
- Delegation: agent reports success, check the diff, verify, report the actual state.

## When To Apply
ALWAYS before any success or completion claim, any expression of satisfaction, committing, delivering, marking a task done, moving to the next task, or handing off. Applies to exact phrases, paraphrases and implications of success.