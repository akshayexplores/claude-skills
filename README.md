# claude-skills

Akshay's Claude skills, backed up from his Claude account on 2026-11-15. Private: several skills hold client and company material.

Each skill is one folder under `skills/` with a `SKILL.md` inside.

## Install

**Claude Code (any machine)**

```bash
git clone https://github.com/akshayexplores/claude-skills
mkdir -p ~/.claude/skills
cp -r claude-skills/skills/* ~/.claude/skills/
```

Copy only the folders you want if you don't need them all. Then run `./install-community-skills.sh` for the community packs and the listing overrides.

**Another Claude account (claude.ai / desktop app)**

1. Zip one skill folder, e.g. `cd skills && zip -r lila-gtm.zip lila-gtm`
2. In Claude, open the skills settings and upload the zip.
3. Repeat per skill.

Same Claude account on another device needs nothing: skills sync with the account.

## What's here

### Mine (12)

| Skill | Use |
|---|---|
| `fastrbuild-context` | FastrBuild company fundamentals for strategy, positioning, sales |
| `fastrbuild-design-guide` | FastrBuild "Sea glass" visual identity |
| `fastrbuild-legal-docs` | Branded NDAs and agreements as .docx |
| `lila-gtm` | LiLA marketing and sales engine (Acsia) |
| `outgrow-acsia` | Outgrow proactive-sales system for Acsia's existing accounts |
| `secondbrain-brand` | SecondBrain brand: colours, type, voice, claims rules |
| `secondbrain-ui-screens` | Clickable prototype of SecondBrain's real UI |
| `akshay-writes` | Writing in Akshay's voice |
| `saving-akshays-brain` | Littlebird/Notion daily context into Obsidian notes |
| `kallaway-script-writer` | YouTube script writing |
| `hyperframes-video` | HTML-to-MP4 video with HeyGen HyperFrames |
| `skill-security-scan` | Scan a skill for security threats before installing |

### Third-party packs (46)

| Pack | Skills | Use |
|---|---|---|
| Superpowers | 14 x `superpowers-*` | Build discipline: brainstorm, plan, TDD, debug, review, verify |
| Replica | 11 x `replica-*` | Clone an app end to end: recon, architect, design, build, test, launch |
| Founder | 11 x `founder-*` | Test a business before launch: board, competitors, consumer panel, pricing, offer, CFO, marketing, brand, ops, launch, plan ([source](https://github.com/Jakeschincariol/founder-skill), MIT) |
| Taste / design | `design-taste-frontend`, `design-taste-frontend-v1`, `high-end-visual-design`, `minimalist-ui`, `industrial-brutalist-ui`, `stitch-design-taste`, `image-to-code`, `imagegen-frontend-web`, `imagegen-frontend-mobile` | Frontend design direction and image-led UI |
| Impeccable | `impeccable` | Frontend design, critique and polish |

## Which skills Claude sees

Too many skills crowd Claude's skill listing (about 1% of the context window), so most get listed by name only and the wrong one gets picked. `config/skill-overrides.json` keeps about 55 in the listing and makes the rest slash-only (`"user-invocable-only"`: hidden from Claude, still runnable as `/name`).

| Purpose | Claude picks these on its own | Slash-only |
|---|---|---|
| Companies and brands | fastrbuild-*, lila-gtm, outgrow-acsia, secondbrain-* | |
| Writing | akshay-writes, humanizer, kallaway-script-writer | |
| Building software | Superpowers (14) | gstack, GSD, BMAD, Matt Pocock, Agent Skills, karpathy-guidelines, Ponytail |
| UI design | design-taste-frontend, impeccable, `design-kit` | other Taste styles, UI UX Pro Max, frontend-design, theme-factory |
| Diagrams | archify | diagram-design |
| Office files | docx, xlsx, pdf, pptx | ppt-master, doc-coauthoring |
| Video | hyperframes-video | OpenMontage (project folder) |
| Research | deep-research, last30days, agent-reach | reverse-engineer-anything |
| Codebases | graphify | |
| Marketing | `marketing-kit` | Corey Haines' 53 skills, Anthropic marketing plugin |
| Business ideas | `founder-kit` | founder-* (11) |
| Other | saving-akshays-brain, morning, skill-security-scan, skill-creator, mcp-builder | Replica, career-ops, headroom |

`marketing-kit`, `design-kit` and `founder-kit` are router skills: one short entry in the listing and a table that tells Claude which hidden skill's `SKILL.md` to read.

## Community packs (installed by script, not copied here)

`./install-community-skills.sh` installs 20 packs from their GitHub sources and then applies the overrides: Matt Pocock Skills, Ponytail, gstack, GSD, BMAD Method, UI UX Pro Max, Archify, Diagram Design, REA, Graphify, Agent Reach, Career Ops, Headroom, Last 30 Days, OpenMontage, PPT Master, Humanizer, Marketing Skills (Corey Haines), Karpathy Skills, I Have ADHD, Agent Skills (Addy Osmani), plus the Anthropic example skills not in the account.

Notes:
- gstack installs with prefixed names (`/gstack-review`) and without its per-prompt routing and contract hooks. Its destructive-command guard stays on.
- Removed on purpose (2026-11-25): ECC (328 skills, 72 agents, ~30 hooks, overlaps everything), Caveman (your preferences already ask for short answers), Understand Anything (same job as Graphify), Claude-Mem (memory is wiped with each cloud container).
- `last30days` reads browser cookie stores to reach X/Twitter, and `design` (UI UX Pro Max) reads `~/.claude/.env` for image-API keys. Both are by design; know it before using them on your own machine.
- Scanned with SkillSpector (static) on 2026-11-20: no real threats; flags were template comments, test fixtures and docs about `.env` files.

## Not included on purpose

- **Anthropic built-ins** (docx, pdf, pptx, xlsx, skill-creator, canvas-design, etc.): already present wherever Claude runs.
- **Anthropic plugins** (sales, finance, legal, HR, marketing, operations, product-management, data, design, productivity): reinstall from the plugin catalog.

## Updating

Skills edited in Claude do not sync here automatically. Re-export and commit when a skill changes.
