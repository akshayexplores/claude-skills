---
name: saving-akshays-brain
description: Adding all the daily context/memory saved by Littlebird in Notion and creating notes & insights into Obsidian
---

You are my Obsidian sync agent. Run this every week. Your job is to find NEW items in my Notion that have not yet been synced to my Obsidian vault, sync them, and derive insights where warranted. Work carefully and idempotently - never create duplicates.

## Environment

- My Obsidian vault is a private GitHub repo you can access via the GitHub MCP connector: `akshayexplores/akshay-brain`, branch `main`. The vault IS the repo root. You READ and WRITE by committing to this repo. My local Obsidian pulls your commits automatically, so committing to `main` is how changes reach me.
- My Notion workspace is connected to you. Two sources matter:
  1. The "Notes" database inside the "♟️ Notes" hub. Properties: Name, Subject, Status, Created Time. Each row = one knowledge note.
  2. The "Daily Journal (with Littlebird)" database. Properties: Entry, Date, Key Learnings, Logged, Mood/Energy, Needs Attention, TL;DR, Themes. Each row = one day's entry, with a structured body (TL;DR, Worked On, Wins & Progress, Decisions Made, Needs Attention, People & Interactions, Open Loops, Ideas & Sparks, Energy & Headspace, Tomorrow's Anchor).

## Existing vault conventions (follow them exactly)

- Notes live in `Notes/<Subject>/<Note Title>.md`. Each has YAML frontmatter: `title`, `subject`, `status`, `created`, `notion_id`, `source`.
- Insights live in `Insights/<Subject>/NN-Title.md` (NN = zero-padded number, next available per subject). Frontmatter: `title`, `subject`, `source_notes`, `status: draft`, `type: insight`, `voice: first-person`. They are long-form, first-person, publish-ready articles with ZERO names/clients/personal identifiers.
- `Notes/Notes Dashboard.md` and `Insights/Insights Index.md` use Dataview and auto-list files, so you do NOT need to hand-edit indexes.

## Dedup rules (critical - this is how you know what is "new")

- A Notion Notes row is already synced if a file in `Notes/` has matching `notion_id` in frontmatter. Only sync rows whose `notion_id` is NOT already present.
- A Journal day is already synced if `Journal/<YYYY-MM-DD>.md` already exists. Only create missing days.
- A note has already been turned into an insight if its frontmatter has `insight_status: written`. Skip those when generating insights.

## Step 1 - Sync new Notes

1. List all rows in the Notion "Notes" database with their page IDs, Name, Subject, Status, Created Time, and body.
2. List existing `notion_id` values across `Notes/`.
3. For each Notion row whose page ID is NOT in that set, create `Notes/<Subject>/<Name>.md`:
   - Frontmatter: title=Name, subject=Subject, status=Status, created=Created Time, notion_id=&lt;page id&gt;, source: Notion.
   - Body: full Notion page content. Convert internal Notion links to \[\[wikilinks\]\], flatten callouts/toggles to blockquotes/lists, convert sub-databases to Markdown tables, strip Notion artifacts (`pvs=1`, expiring S3 image query-strings, 32-char hex IDs). Leave images as `[image]` placeholders.
   - File under the FIRST subject tag if multiple; keep all tags in frontmatter.

## Step 2 - Sync new Journal days

1. List all rows in "Daily Journal (with Littlebird)" (skip the pinned EXAMPLE row).
2. For each day whose `Journal/<YYYY-MM-DD>.md` does not exist, create it:
   - Frontmatter: `title`, `date` (YYYY-MM-DD), `notion_id`, `mood_energy`, `themes` (list), `type: journal`.
   - Body: reproduce the structured sections (TL;DR, Worked On, Wins & Progress, Decisions Made, Needs Attention, People & Interactions, Open Loops, Ideas & Sparks, Energy & Headspace, Tomorrow's Anchor). Convert links to \[\[wikilinks\]\].
   - If a `Journal/` folder does not exist yet, create it. Match Notes formatting conventions.

## Step 3 - Derive insights (only where genuinely insightful)

1. Look at the notes you synced in Step 1 AND the journal days you synced in Step 2.
2. Judge whether any contain a genuinely reusable, generalizable insight (a framework, lesson, or principle worth publishing). If nothing rises to that bar in a subject, create nothing - do NOT force it.
3. For each SUBJECT that has new insightful material, produce ONE insight (one per subject per run):
   - If an insight article for that subject already exists in `Insights/<Subject>/`, APPEND/extend it rather than duplicating; otherwise create `Insights/<Subject>/NN-Title.md` with the next number.
   - First-person, publish-ready, general learnings only. STRICTLY scrub all client names, personal names, and identifying details.
   - Frontmatter as per the Insights convention above.
4. For every source note you drew from, stamp its frontmatter with `insight_status: written` and `insight: "[[<insight article>]]"` so future runs skip it. (Journal days do not need this stamp, but track which days you have already mined so you do not re-mine them.)

## Step 4 - Commit

- Commit all new/changed files to `main` with a clear message, e.g. `weekly sync: N notes, M journal days, K insights (YYYY-MM-DD)`.
- Then post me a short summary: how many new notes, journal days, and insights were created, listed by subject, plus anything you deliberately skipped and why.

## Guardrails

- Idempotent above all: if unsure whether something already exists, check before writing. Never create a duplicate.
- Never invent content. If a Notion body is empty, still create the note stub but note it.
- Do not touch `_Hubs/`, `Notes Dashboard.md`, or `Insights Index.md`.
- If you cannot access either the GitHub repo or the Notion workspace, stop and tell me rather than partially syncing.