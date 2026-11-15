---
name: "superpowers-using-superpowers"
description: "Use at the start of any task or conversation to check whether a superpowers skill applies, and invoke it before responding, exploring or asking clarifying questions."
---

# Using Superpowers (from obra/superpowers, MIT licence, adapted)

If there's even a 1% chance a skill applies to what you're doing, invoke it. If it applies, you don't have a choice.

## The rule
Invoke relevant or requested skills BEFORE any response or action, including clarifying questions, exploring files or checking anything. If it turns out wrong for the situation, you don't have to use it. Announce "Using [skill] to [purpose]" and follow it exactly. If it has a checklist, create a todo per item.

## Which skill when
- Building anything new ("let's build X", a feature, site, plan, talk) → **superpowers-brainstorming** first, then implementation skills.
- Approved design, multi-step work → **superpowers-writing-plans**.
- Running a plan yourself → **superpowers-executing-plans**; with a fresh agent per task → **superpowers-subagent-driven-development**.
- Bug, failing test, odd behaviour → **superpowers-systematic-debugging** first.
- Writing implementation code → **superpowers-test-driven-development**.
- Several independent problems → **superpowers-parallel-agents**.
- Need an isolated workspace → **superpowers-git-worktrees**.
- Task or feature done, before merge, or feedback arrives → **superpowers-code-review**.
- About to say "done", "fixed", "passing" → **superpowers-verification**.
- Branch complete → **superpowers-finishing-branch**.
- Creating or editing a skill → **superpowers-writing-skills**.
- A superpowers session went wrong and they want to know why → **superpowers-diagnosing**.

Process skills come first (they set the approach), implementation skills carry it out.

## Red flags (you're rationalizing)
| Thought | Reality |
|---|---|
| "Just a simple question" | Questions are tasks. Check for skills. |
| "I need more context first" | The skill check comes before clarifying questions. |
| "Let me explore first" / "check files quickly" | Skills tell you how to explore. |
| "Doesn't need a formal skill" / "overkill" | If one exists, use it. |
| "I remember this skill" | Skills evolve. Read the current version. |
| "I'll just do this one thing first" | Check BEFORE doing anything. |

## Precedence
The user's own instructions (their preferences, CLAUDE.md, direct requests) override skills, which override default behaviour. Skip a skill's workflow only when the user explicitly says so.