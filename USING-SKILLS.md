# How to use your skills

**TL;DR:** Ask for what you want in plain words. Claude picks from about 60 skills it can see, and for specialist work it opens one of 5 kits that point it at the right hidden skill. When you already know the exact skill, type `/name`. Keep it that way: add new skills to a kit, not to the visible list.

## How it's set up

| Tier | What it means | How you use it |
|---|---|---|
| **Visible** (~60) | Claude sees the name and description every turn and picks it on its own | Just describe the task |
| **Kits** (5 routers) | One visible entry that lists many hidden skills and tells Claude which file to read | Just describe the task; or name the kit ("use the video kit") |
| **Slash-only** (~420) | Hidden from Claude to save context, still installed | Type `/name`, e.g. `/gstack-ship`, `/cut-silences` |

Why: Claude's skill list gets about 1% of the context window. With ~930 skills, most showed as bare names and the wrong one got picked. Hiding the rest keeps the visible ones fully described.

The hidden list lives in `config/skill-overrides.json`. Run `/skills` in Claude Code to see or toggle any skill.

Some backed-up skills declare a different name inside the file than their folder (folder `tob-semgrep`, name `semgrep`). The kit tables show both, e.g. `tob-semgrep` (`/semgrep`). If one form of a slash command doesn't work, try the other.

## What to ask for

| You want to… | Say something like | Claude uses | Power-user command |
|---|---|---|---|
| Work on FastrBuild, LiLA, Outgrow, SecondBrain | "Draft the LiLA outbound sequence" | Your company skills | |
| Write in your voice | "Write this post in my voice" | `akshay-writes`, then `humanizer` | |
| Write a YouTube script | "Script a video about X" | `kallaway-script-writer` | |
| Build or fix software | "Plan and build X", "this test fails" | **Superpowers** | `/gstack-ship`, `/gstack-qa`, `/gstack-office-hours` |
| Design a UI | "Make this page look premium" | `design-taste-frontend`, `impeccable`, `design-kit` | `/minimalist-ui`, `/ui-ux-pro-max` |
| Make a video or animation | "Make a 30s launch video", "cut the silences" | `hyperframes-video`, `video-kit` | `/make-a-video`, `/edit-video`, `/cut-silences` |
| Security review or test strategy | "Security-review this PR", "add E2E tests" | `security-kit` | `/ecc-security-review`, `/playwright-cli` |
| Marketing or growth | "Fix this landing page's conversion" | `marketing-kit` | `/copywriting`, `/seo-audit` |
| Test a business idea | "Pressure-test this business idea" | `founder-kit` | `/founder-board`, `/founder-cfo` |
| Draw a diagram | "Diagram this architecture" | `archify` | `/diagram-design` |
| Word, Excel, PDF, PowerPoint | "Turn this into a deck" | `docx`, `xlsx`, `pdf`, `pptx` | `/ppt-master` |
| Research | "What are people saying about X this month" | `last30days`, `agent-reach`, `deep-research` | `/reverse-engineer-anything` |
| Understand a codebase | "Map how this repo fits together" | `graphify` | `/graphify` |
| Clone an app | | | `/replica-recon` and the other `replica-*` |
| Job hunt | | | `/career-ops` |
| Daily notes | "Save today's context" | `saving-akshays-brain`, `morning` | |

## Building software: one process only

Use **Superpowers** end to end. Typical flow: brainstorming, then writing-plans, then executing-plans (or subagent-driven-development), with test-driven-development, systematic-debugging, code-review, verification and finishing-branch along the way. Claude picks these up from plain requests.

GSD, BMAD, Matt Pocock and Agent Skills are installed but hidden. Don't mix them with Superpowers in one project: each one tries to run the whole process its own way. Reach for a single command only when you want that specific tool, e.g. `/grill-me` to stress-test a plan.

## Setting up a new session or machine

1. `git clone https://github.com/akshayexplores/claude-skills`
2. `cp -r claude-skills/skills/* ~/.claude/skills/`
3. `cd claude-skills && ./install-community-skills.sh` (installs the community packs and applies the overrides)
4. Restart Claude Code.

Cloud sessions start from a fresh container, so steps 1 to 3 have to run again there. Ask Claude to save them as the environment's setup script so it happens automatically.

## Adding a new skill

1. **Scan it first:** "scan this skill" runs `skill-security-scan`.
2. **Decide the tier:**
   - You'll use it most days, or it's about your own companies or voice: make it visible.
   - It's specialist: add it to the matching kit's table (`skills/<kit>/SKILL.md`) and add its name to `config/skill-overrides.json` as `"user-invocable-only"`.
   - It doesn't fit any kit and you rarely need it: slash-only, no kit.
3. **Keep the visible list under about 60.** If you add one, consider hiding another.
4. **Commit it** to this repo so it's backed up.

## Rules that keep it lean

- **One skill per job.** Before adding a pack, check that nothing you have already does it.
- **Avoid packs that add hooks or agents.** ECC added 72 agents and about 30 hooks that ran on every prompt and tool call. Plugins like that cost tokens even when you never use them.
- **One style rule.** Your preferences already ask for answer-first replies, so skip tools like Caveman that inject the same instruction on every prompt.
- **Check now and then:** ask "how many skills are visible and what do the hooks cost?" and trim if it has grown.

## Still to do in claude.ai

- **Turn off the account plugins you don't use in coding** (sales, pm-toolkit, lmty, legal, finance, HR, operations). They add about 180 skills to every session and only you can switch them off.
- **Delete `design-taste-frontend-v1`.** It's an older copy; it's hidden here but still syncs from your account.
- **Upload the `founder-*` skills** if you want them in claude.ai too (zip each folder, upload in skills settings).

## What was removed and why (2026-11-25)

| Removed | Why |
|---|---|
| ECC plugin | 328 skills, 72 agents, ~30 hooks; overlapped almost everything. The 10 ECC skills you backed up from your Mac stay, inside `security-kit`. |
| Caveman | Repeats your answer-first preference on every prompt |
| Understand Anything | Same job as Graphify, plus 2 hooks |
| Claude-Mem | Its memory is wiped with every cloud container; 10 hooks |
| gstack routing and contract hooks | Suggested gstack skills on every prompt; gstack itself is still installed |
