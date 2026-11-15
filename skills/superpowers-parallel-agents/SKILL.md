---
name: "superpowers-parallel-agents"
description: "Use when facing two or more independent tasks or failures that can be worked on without shared state or ordering, to dispatch one focused agent per problem in parallel."
---

# Dispatching Parallel Agents (from obra/superpowers, MIT licence)

Delegate tasks to agents with isolated context. Craft exactly what each needs; they never inherit your session history. This keeps them focused and preserves your context for coordination.

**Core principle:** one agent per independent problem domain, running concurrently.

## When to use
- Multiple failures? Are they independent? Can they run in parallel without shared state? → parallel dispatch.
- Related failures (fixing one may fix others), need for full-system understanding, exploratory debugging where you don't yet know what's broken, or agents that would edit the same files/resources → don't. Investigate together, or run sequentially.

## The pattern
1. **Identify independent domains.** Group by what's broken (file A: approval flow; file B: batch completion; file C: abort).
2. **Create focused tasks.** Each gets a specific scope (one file or subsystem), a clear goal, constraints ("don't change other code"), and an expected output (summary of root cause and changes).
3. **Dispatch in parallel:** all dispatch calls in the same response. One per response = sequential.
4. **Review and integrate:** read every summary, check for conflicting edits, run the full suite, spot-check (agents make systematic errors).

## A good agent prompt
Focused (one domain), self-contained (all context, error messages, test names), specific about output.

```markdown
Fix the 3 failing tests in src/agents/agent-tool-abort.test.ts:
1. "should abort tool with partial output capture" - expects 'interrupted at' in message
2. "should handle mixed completed and aborted tools" - fast tool aborted instead of completed
3. "should properly track pendingToolCount" - expects 3 results but gets 0
Likely timing/race issues. Read the tests, find the root cause (timing or real bug), fix by replacing arbitrary timeouts with event-based waiting or fixing the abort bug. Do NOT just increase timeouts.
Return: summary of what you found and what you fixed.
```

## Common mistakes
| Bad | Good |
|---|---|
| "Fix all the tests" (agent gets lost) | "Fix agent-tool-abort.test.ts" |
| "Fix the race condition" (no context) | Paste the errors and test names |
| No constraints (refactors everything) | "Fix tests only" / "don't change production code" |
| "Fix it" (unknown changes) | "Return root cause and changes" |

## Verification after agents return
Review each summary, check whether agents edited the same code, run the full suite, spot-check. An agent's "success" is a claim; verify it (superpowers-verification).