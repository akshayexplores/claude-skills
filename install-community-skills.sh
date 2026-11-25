#!/usr/bin/env bash
# Installs the community skill packs that are not in skills/ (Claude Code, user scope),
# then applies config/skill-overrides.json so only ~55 skills stay in the model's listing.
# Run after copying skills/ into ~/.claude/skills (see README).
# Each pack is installed the way its own README says to. Safe to re-run.
# Needs: git, node/npx, bun (gstack), uv (graphify, agent-reach), python3.
set -euo pipefail

SK="$HOME/.claude/skills"
WORK="$(mktemp -d)"
mkdir -p "$SK"
trap 'rm -rf "$WORK"' EXIT

clone() { git clone -q --depth 1 "https://github.com/$1" "$WORK/${1//\//_}"; echo "$WORK/${1//\//_}"; }

# copy <repo> <glob relative to repo>...  : copy skill folders that hold a SKILL.md
copy() {
  local repo="$1"; shift
  local dir; dir="$(clone "$repo")"
  for pat in "$@"; do
    for d in $dir/$pat; do
      [ -f "$d/SKILL.md" ] || continue
      local name; name="$(sed -n 's/^name:[[:space:]]*["'\'']\{0,1\}\([^"'\'']*\).*/\1/p' "$d/SKILL.md" | head -1)"
      name="${name:-$(basename "$d")}"
      [ -e "$SK/$name" ] && { echo "skip (exists): $name"; continue; }
      cp -aL "$d" "$SK/$name"   # -L: some packs ship SKILL.md as a symlink
    done
  done
}

echo "== Plain skill folders"
copy mattpocock/skills 'skills/productivity/*' 'skills/misc/*' 'skills/engineering/*'
copy DietrichGebert/ponytail 'skills/*'
copy bmad-code-org/BMAD-METHOD 'skills/core-tools/*' 'skills/method/*'
copy nextlevelbuilder/ui-ux-pro-max-skill '.claude/skills/*'
copy tt-a1i/archify 'archify'
copy cathrynlavery/diagram-design 'skills/diagram-design'
copy morluto/rea '.agents/skills/reverse-engineer-anything'
copy career-ops-hq/career-ops '.claude/skills/career-ops'
copy headroomlabs-ai/headroom 'skills/headroom'
copy mvanhorn/last30days-skill 'skills/last30days'
copy hugohe3/ppt-master 'skills/ppt-master'
copy blader/humanizer '.'
copy coreyhaines31/marketingskills 'skills/*'
copy multica-ai/andrej-karpathy-skills 'skills/karpathy-guidelines'
copy ayghri/i-have-adhd 'skills/i-have-adhd'
copy addyosmani/agent-skills 'skills/*'
copy anthropics/skills 'skills/frontend-design' 'skills/algorithmic-art' 'skills/theme-factory' \
  'skills/slack-gif-creator' 'skills/webapp-testing' 'skills/internal-comms' 'skills/doc-coauthoring'

echo "== gstack (prefixed names: /gstack-review etc.)"
if [ ! -d "$SK/gstack" ]; then
  git clone -q --single-branch --depth 1 https://github.com/garrytan/gstack.git "$SK/gstack"
fi
(cd "$SK/gstack" && ./setup --host claude --prefix --no-browser --no-skill-routing --no-skill-contracts </dev/null)

echo "== GSD (from GitHub source; the npm package is marked deprecated)"
gsd="$(clone gsd-build/get-shit-done)"
(cd "$gsd" && npm ci --ignore-scripts --silent && (cd sdk && npm ci --silent && npm run build --silent) \
  && node bin/install.js --claude --global </dev/null)

echo "== Graphify"
uv tool install -q graphifyy && graphify install </dev/null

echo "== Agent Reach (GitHub release only; the PyPI 'agent-reach' is a different project)"
uv tool install -q --force https://github.com/Panniantong/Agent-Reach/releases/latest/download/agent-reach.zip
agent-reach setup </dev/null >/dev/null

echo "== OpenMontage (a project you work inside, not a global skill)"
[ -d "$HOME/OpenMontage" ] || git clone -q --depth 1 https://github.com/OpenMontageInc/OpenMontage.git "$HOME/OpenMontage"

echo "== Skill overrides (slash-only packs, routers cover the rest)"
REPO="$(cd "$(dirname "$0")" && pwd)"
python3 - "$REPO/config/skill-overrides.json" "$HOME/.claude/settings.json" <<'PY'
import json, os, sys
ov = json.load(open(sys.argv[1])); p = sys.argv[2]
s = json.load(open(p)) if os.path.exists(p) else {}
s.setdefault("skillOverrides", {}).update(ov)
json.dump(s, open(p, "w"), indent=2)
print(len(ov), "overrides applied")
PY

echo "Done. Restart Claude Code so the overrides take effect."
