---
name: "superpowers-git-worktrees"
description: "Use when starting feature work that needs isolation from the current workspace, or before executing an implementation plan, to detect or create an isolated git worktree safely."
---

# Using Git Worktrees (from obra/superpowers, MIT licence)

Ensure work happens in an isolated workspace. Prefer the platform's native worktree tools; fall back to manual git worktrees only when none exists.

**Core principle:** detect existing isolation first, then native tools, then git. Never fight the harness.

**Announce:** "I'm using the git-worktrees skill to set up an isolated workspace."

## Step 0: Detect existing isolation
```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
BRANCH=$(git branch --show-current)
git rev-parse --show-superproject-working-tree 2>/dev/null  # prints a path = submodule, treat as normal repo
```
- `GIT_DIR != GIT_COMMON` and not a submodule → already in a linked worktree. Skip to Step 2. Report "Already in isolated workspace at <path> on branch <name>" (or "detached HEAD, externally managed; branch needed at finish").
- Otherwise you're in a normal checkout. If the user hasn't stated a preference, ask: "Would you like me to set up an isolated worktree? It protects your current branch from changes." Declined → work in place, go to Step 2.

## Step 1: Create the workspace
**1a. Native tool first.** If you have something like `EnterWorktree`, `WorktreeCreate`, a `/worktree` command or `--worktree` flag, use it. Manual `git worktree add` alongside a native tool creates phantom state the harness can't manage.

**1b. Git fallback (no native tool).** Directory priority: the user's declared preference → existing `.worktrees/` (wins) or `worktrees/` → default `.worktrees/`.
Verify it's ignored before creating:
```bash
git check-ignore -q .worktrees || git check-ignore -q worktrees
```
Not ignored → add to `.gitignore`, commit, then proceed.
```bash
git worktree add "$LOCATION/$BRANCH_NAME" -b "$BRANCH_NAME" && cd "$LOCATION/$BRANCH_NAME"
```
Permission error (sandbox) → tell the user and work in the current directory.

## Step 2: Project setup
Auto-detect: `package.json` → `npm install`; `Cargo.toml` → `cargo build`; `requirements.txt` → `pip install -r requirements.txt`; `pyproject.toml` → `poetry install`; `go.mod` → `go mod download`.

## Step 3: Clean baseline
Run the project's tests. Failing → report and ask whether to proceed or investigate. Passing → report: `Worktree ready at <path> · Tests passing (<N>, 0 failures) · Ready to implement <feature>`.

## Rationalizations
| Excuse | Reality |
|---|---|
| "Obviously not in a worktree" | Run Step 0; harness isolation and submodules fool eyeballing. |
| "`git worktree add` is quicker" | Bypassing a native tool is the #1 mistake. |
| "Surely it's ignored" | Run `git check-ignore`. An unignored dir commits the whole tree. |
| "Baseline tests can wait" | A dirty baseline makes every later failure ambiguous. |