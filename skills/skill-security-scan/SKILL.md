---
name: "skill-security-scan"
description: "Scan an AI agent skill (or a folder of skills) for security threats with NVIDIA SkillSpector before installing or trusting it, then triage false positives in plain words."
---

# Skill security scan (NVIDIA SkillSpector)

SkillSpector (https://github.com/NVIDIA/skillspector) checks agent skills (SKILL.md plus any scripts) for prompt injection, data exfiltration, credential access, privilege escalation and risky dependencies. It reads files only; it never runs the skill.

**What it is good for:** skills, plugins, MCP tool packs, anything an agent loads as instructions.
**What it is not:** an app security review. Pointed at app code it flags normal things (database queries, key storage). Say so if asked to scan an app, and offer a targeted review instead.

## 1. Install (once per workspace)
```bash
which skillspector || uv tool install git+https://github.com/NVIDIA/skillspector.git
```
Needs Python 3.12+. Works in the cloud workspace (GitHub is reachable). Do not install it into the user's own folders.

## 2. Scan
- Default to static only: `--no-llm`. LLM mode sends the skill's file contents to an outside model provider; only use it when the user says yes and names the provider (`SKILLSPECTOR_PROVIDER`, plus that provider's key).
- Static mode still sends dependency names and versions to OSV.dev to check for known CVEs. Mention that once.
- **Scan each skill on its own.** `--recursive` on a big folder hits an aggregate limit and silently skips skills (shows as `<unscanned>`).

```bash
OUT=<scratchpad>/skillspector; mkdir -p $OUT
for d in <skills-folder>/*/; do n=$(basename "$d"); \
  timeout 300 skillspector scan "$d" --no-llm --format json --output $OUT/$n.json >/dev/null 2>$OUT/$n.err; done
```
Single skill: `skillspector scan ./my-skill/ --no-llm`. A GitHub URL or .zip also works.
Where skills live: account skills are synced read-only under `~/.claude/skills/synced/*/`. Files on the user's Mac must be reached through the linked computer (and copied into the workspace before scanning).

## 3. Summarise
Each JSON has `risk_assessment` (score 0-100, severity, recommendation SAFE / CAUTION / DO_NOT_INSTALL) and `issues` (id, pattern, severity, file, line, code_snippet). Print one row per skill: score, recommendation, count of HIGH/CRITICAL, top patterns. Then read every HIGH/CRITICAL snippet yourself before calling anything a threat.

## 4. Triage (do not pass the score through raw)
The score is noisy. Known false-positive patterns:
- **AE1 Incomplete referenced artifact analysis**: the scanner could not fully read a referenced file. A coverage gap, not a threat. It alone can push a score to 100.
- **AR2 Anti-refusal**: fires on ordinary "Never do X" style rules.
- **TM1 Tool parameter abuse** on SQL with `$1, $2` placeholders: those are safe parameterised queries.
- **E2 Env variable harvesting** on `os.environ.copy()` passed to a subprocess: normal.
- **P6 Prompt extraction** on words like "prompt" or "CRITICAL OUTPUT RULE": usually style text.
- **YARA hits** on store-listing or schema keywords: check the snippet.

Real threats look like: instructions to ignore the user or system, hidden text, sending files or env/keys to a URL, reading `~/.ssh`, `.env`, keychains or other agents' config, downloading and running code, obfuscated or base64 blobs, or tool descriptions that tell the agent to do things the user did not ask.

## 5. Report to the user
Short, non-technical, scannable:
- Bottom line first (safe to keep using / remove / check one thing).
- Real issues: what it is, where, why it matters, what to do.
- "Flagged but fine": one line per skill explaining the false positive.
- What was not scanned and why.
Never edit or delete a skill without the user's explicit yes.