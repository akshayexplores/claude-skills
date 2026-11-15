---
name: "superpowers-diagnosing"
description: "Use when a superpowers-driven session went wrong and the person wants to know why (repeated work, ignored plan, stumbles, poor results, a skill that didn't fire, too slow or too costly), or wants a bug report for the superpowers maintainers."
---

# Diagnosing Superpowers (from obra/superpowers, MIT licence, condensed)

Pin down with your human partner what went wrong in a session, read the transcript evidence, and report what happened. You report; you do not diagnose or redesign superpowers. Whoever triages the report decides.

**Core principle:** every finding cites its location in the transcript (path:line, or the turn/message it's in). No citation, no finding. Every number comes from the transcript or a command you ran, never from memory.

## Workflow (a todo per step)
1. **Problem intake.** One question at a time until you can write a statement naming the session(s), the turn range if known, what they expected, what happened, and the observable they care about (wall-clock, tokens, repeated actions, one specific action). "It took too long" is a complaint, not a problem statement. Note whether the goal is a bug report. Nothing in later steps starts until they answer; if they're away, write the questions and stop. An already-scoped request (one specific event, what's running now) is itself the statement.
2. **Locate.** Resolve each session to its verified transcript (on Claude Code, JSONL files under the projects directory; here, the conversation or past-chat tools). Confirm a past session by quoting its first prompt and timestamp; list rejected candidates with reasons. Include subagent transcripts. Start a case file recording environment and which skills were loaded, citing where you saw each.
3. **Triage.** Read the region around the reported problem yourself. Then examine these dimensions (in parallel analyst subagents if available, each given the case file and one dimension; split long transcripts by turn range): skill timeline (what fired when), plan adherence (compaction points first), repeated work, stumbles (errors, retries, dead ends), quality evidence (were claims verified?), request conflicts (instructions that pulled in different directions), cost and time. Discard any finding without a citation.
4. **Report:** problem statement; verdict leading with the findings the complaint points to; findings by dimension with citations; timeline; what cited content actually proves (and what it doesn't); coverage and gaps; superpowers involvement (none / possible / likely — state it and stop: never name a skill defect or propose a change, even if pressed). Write it to a file, show it, give the path.
5. **GitHub issue** (only if involvement is possible/likely, or asked): search open and closed issues in obra/superpowers for the symptoms; show matches and suggest adding to the closest. None → draft an issue, show the exact text, create it only after approval. Never a placeholder summary.
6. **Export bundle** (only when they ask): ask the redaction level (skeleton = no tool-result bodies; evidence = bodies only for cited events; full). Scrub secrets, personal data and paths, then audit the scrub and repeat until clean. Show the scrub log and file list; archive only after approval; remind them scrubbing can miss things and they must review every file before sharing.
7. **Similar sessions** (when asked): turn confirmed findings into a signature, check candidate sessions for it, append the matches.

## Quick reference
| Complaint | Look first at |
|---|---|
| "It took too long" | cost and time, stumbles |
| "Why the extra work?" | repeated work, plan adherence |
| "Why so expensive?" | cost and time |
| "What is it doing?" (still running) | skill timeline; mark in progress |
| "It ignored the plan" | plan adherence, compaction points first |
| "Skill X never fired" | skill timeline |

## Hard rules
- **Context safety:** transcript lines can be huge. Read with offsets, grep with limits, never dump whole files.
- **Read-only:** never modify, move or delete a session file.
- **Exact paths to subagents:** a subagent's "current session" is its own.
- **Human prompts only:** hook output, system reminders and tool results are not your partner's words; in a subagent transcript, "user" is the parent agent.
- **No superpowers diagnosis, no advice.** Report involvement and stop.
- **Approval gates:** no archive before they've seen the scrub log; no issue or comment before they approve the exact text.

## Red flags
| Thought | Reality |
|---|---|
| "The problem is obvious, skip intake" | The statement scopes everything. Ask. |
| "They're away, I'll reconstruct it" | You can't. Write the questions and stop. |
| "Sweep everything now, ask later" | Spends their budget on the wrong question. |
| "They want a bug report, build the bundle" | Only when they ask. |
| "Small targeted skill edit" | Not your call. Report the evidence. |
| "The token price is well known" | Numbers you didn't compute are invented. |