---
name: "superpowers-finishing-branch"
description: "Use when implementation on a branch is complete and tests pass, to verify, then offer merge, pull request or keep, and clean up the worktree safely."
---

# Finishing a Development Branch (from obra/superpowers, MIT licence)

**Core principle:** verify tests → detect environment → present options → execute choice → clean up.

**Announce:** "I'm using the finishing-branch skill to complete this work."

## Step 1: Verify tests
Run the full suite. Failing → report `Tests failing (<N> failures). Must fix before completing:` with the failures, and stop.

## Step 2: Detect environment (capture now, before any cd)
```bash
GIT_DIR=$(cd "$(git rev-parse --git-dir)" 2>/dev/null && pwd -P)
GIT_COMMON=$(cd "$(git rev-parse --git-common-dir)" 2>/dev/null && pwd -P)
WORKTREE_PATH=$(git rev-parse --show-toplevel)
```
| State | Menu | Cleanup |
|---|---|---|
| Normal repo | 3 options | None |
| Worktree, named branch | 3 options | Provenance-based |
| Worktree, detached HEAD | 2 options (no merge) | Externally managed, leave it |

## Step 3: Base branch
Whatever this forked from (plan, conversation, upstream). Not known → ask "This branch split from <guess> - is that correct?" Merging into the wrong base is expensive.

## Step 4: Present exactly these options
```
Implementation complete. What would you like to do?
1. Merge back to <base-branch> locally
2. Push and create a Pull Request
3. Keep the branch as-is (I'll handle it later)
Which option?
```
Detached HEAD: `1. Push as new branch and create a Pull Request  2. Keep as-is`. Never offer discarding. Wait for the answer.

## Step 5: Execute
- **Merge:** `MAIN_ROOT=$(git -C "$(git rev-parse --git-common-dir)/.." rev-parse --show-toplevel); cd "$MAIN_ROOT"; git checkout <base>; git pull; git merge <feature>;` run tests on the merged result. Failing → stop, leave branch and worktree. Green → cleanup (Step 6), `git branch -d <feature>`.
- **PR:** `git push -u origin <feature>` (detached: `git push origin HEAD:refs/heads/<new>`), create the PR with the forge CLI following the repo's template, report the URL. Keep the worktree for feedback.
- **Keep:** "Keeping branch <name>. Worktree preserved at <path>."
- **Discard (only if explicitly asked):** show what will be permanently deleted (branch, commits, worktree) and require the typed word `discard`. Then cd to main root, cleanup, `git branch -D`.

## Step 6: Cleanup (merge and confirmed discard only)
- Normal repo → nothing to do.
- `WORKTREE_PATH` under `.worktrees/` or `worktrees/` → `git worktree remove "$WORKTREE_PATH"; git worktree prune`.
- Removal refused (modified/untracked files) → never `--force` on your own. Show `git -C "$WORKTREE_PATH" status --porcelain -uall` and ask: commit them, move them to the main repo, or delete them (unrecoverable).
- Otherwise the host owns it: leave it; use the platform's exit tool if any.

## Rationalizations
| Excuse | Reality |
|---|---|
| "Tests passed earlier" | Run them on the tree you're integrating. |
| "They obviously want it merged" | Their decision. Present the menu. |
| "'Get rid of it' counts" | Only the typed word `discard`. |
| "PR is up, worktree is clutter" | Feedback gets fixed there. |
| "`--force` finishes cleanup" | It destroys files that exist nowhere else. |
| "Push rejected, force-push" | The remote moved. Investigate; force only on explicit request. |