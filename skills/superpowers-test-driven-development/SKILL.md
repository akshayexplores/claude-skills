---
name: "superpowers-test-driven-development"
description: "Use when implementing any feature, bug fix, refactor or behaviour change, before writing implementation code: write the failing test first."
---

# Test-Driven Development (from obra/superpowers, MIT licence)

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing. Violating the letter of the rules is violating the spirit.

**Always** for new features, bug fixes, refactoring, behaviour changes. **Exceptions only with your partner's OK:** throwaway prototypes, generated code, config files.

## The Iron Law
```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```
Wrote code before the test? Delete it and start over. Don't keep it as reference, don't adapt it, don't look at it.

## Red-Green-Refactor
1. **RED:** write one minimal test showing what should happen. One behaviour, clear name, real code (mocks only if unavoidable).
2. **Verify RED (mandatory):** run it. It must fail (not error), with the expected message, because the feature is missing (not a typo). Passes already? You're testing existing behaviour; fix the test.
3. **GREEN:** the simplest code that passes. No extra options, no YAGNI features, no refactoring elsewhere.
4. **Verify GREEN (mandatory):** it passes, other tests pass, output is clean. Fails? Fix the code, not the test. "Other tests" means the project's whole suite: run the project's test command even if your task named one file, and report any failure by name, including ones you didn't cause.
5. **REFACTOR:** only when green. Remove duplication, improve names, extract helpers. Stay green; add no behaviour.
6. Repeat with the next failing test.

Example:
```typescript
// GOOD: clear name, real behaviour, one thing
test('retries failed operations 3 times', async () => {
  let attempts = 0;
  const op = () => { attempts++; if (attempts < 3) throw new Error('fail'); return 'success'; };
  expect(await retryOperation(op)).toBe('success');
  expect(attempts).toBe(3);
});
// BAD: test('retry works') that only asserts a mock was called 3 times
```

## Good tests
| Quality | Good | Bad |
|---|---|---|
| Minimal | One thing. "and" in the name? Split it. | `validates email and domain and whitespace` |
| Clear | Name describes behaviour | `test1` |
| Shows intent | Demonstrates the desired API | Obscures what code should do |

Rules that keep tests honest: name the production change that would make the test fail before writing it; assert on real behaviour, never on mock behaviour; keep test-only code in test utilities, out of production classes; understand a dependency's side effects before mocking it.

## Rationalizations
| Excuse | Reality |
|---|---|
| "Too simple to test" | Simple code breaks. 30 seconds. |
| "I'll test after" | Tests written after pass immediately, which proves nothing. |
| "Already manually tested" | Ad hoc, unrecorded, can't re-run. |
| "Deleting hours of work is wasteful" | Sunk cost. Untrusted code is the waste. |
| "Keep as reference" | You'll adapt it. That's testing after. |
| "Need to explore first" | Fine. Throw the exploration away, then TDD. |
| "Hard to test" | Hard to test = hard to use. Simplify the design. |
| "TDD slows me down" | Debugging in production is slower. |
| "Existing code has no tests" | Add tests for what you touch. |

## Red Flags: delete and start over
Code before test; test passes immediately; can't explain why it failed; tests "later"; "just this once"; "spirit not ritual"; "this is different because...".

## Bug fixes
Bug found? Write a failing test reproducing it, then follow the cycle. Never fix a bug without a test.

## When stuck
| Problem | Solution |
|---|---|
| Don't know how to test | Write the wished-for API; write the assertion first; ask. |
| Test too complicated | Design too complicated. Simplify the interface. |
| Must mock everything | Too coupled. Use dependency injection. |
| Huge setup | Extract helpers; still huge, simplify the design. |

## Checklist before marking work complete
- [ ] Every new function has a test
- [ ] Watched each test fail, for the expected reason
- [ ] Minimal code to pass each
- [ ] Whole suite passes, output clean
- [ ] Real code, mocks only if unavoidable
- [ ] Edge cases and errors covered
Can't tick all of them? You skipped TDD. Start over.