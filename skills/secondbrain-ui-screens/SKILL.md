---
name: "secondbrain-ui-screens"
description: "Build a clickable, shareable HTML prototype or screenshots of SecondBrain's real current UI with sample data, for designers, reviews, decks or mockups."
---

# SecondBrain UI screens

Use this whenever Akshay asks for SecondBrain UI screens: "the latest UI file for my designer", a prototype to share, screenshots of a screen or state, or app screens for a deck, video or site.

The output always comes from the app's REAL interface files (never a redrawn mockup), run against a stand-in engine with invented data.

## Where things are
- **App UI:** `secondbrain/ui/` in the repo.
  - On Akshay's Mac: `/Users/vajra/Downloads/secondbrain/secondbrain/ui`.
  - On GitHub: `akshayexplores/secondbrain`, branch `work-in-progress`.
  - The Mac copy is the newest; use it when the Mac is linked.
- **Build kit:** `tools/ui_prototype/` in the same repo.
  - `build.py`: inlines all CSS, JS, fonts and images into one HTML file.
  - `mock-data.js`: sample data.
  - `mock-api.js`: fake `/api` that answers every request; it streams `/api/chat` as SSE like the real engine.
  - `reviewer.js`: the top-middle "Screens · PROTOTYPE" menu, plus the Data and Look toggles.
  - `verify.js`: a Playwright click-through of every menu item.
  - `README.md`: how to add a screen or a fake route.
- **Last shared prototype:** `SecondBrain UI Prototype` artifact (5 Nov 2026, 108 screens). Project doc: `claude/secondbrain-ui-prototype-20261028.md`.

## Steps
1. **Get the current UI.**
   - If the Mac is linked, work from the Mac repo, with git status checked first.
   - Otherwise clone or read `work-in-progress` from GitHub and say the file reflects the last pushed code.
2. **Rebuild** from the repo root:
   `python3 tools/ui_prototype/build.py --ui secondbrain/ui --out ~/Downloads/SecondBrain_UI_Prototype_$(date +%Y%m%d).html`
   - Run Python on the Mac itself (`osascript do shell script`) or in the cloud container on staged files. Not the Mac's Linux VM, which has Python 3.10.
3. **Cover new features.** Compare the engine routes (`secondbrain/api*.py`, `chat.py`) and `ui/*.js` with the kit:
   - for every new screen, state, card or dialog, add sample data to `mock-data.js`;
   - add the route to `mock-api.js`, using the same request and response shapes as the real engine;
   - add a menu item in `reviewer.js`, in a sensible group.
   - Keep every old menu item working.
4. **Verify:** run `node tools/ui_prototype/verify.js <file> <screenshot-folder>` (Chromium and Playwright are preinstalled in the cloud container).
   - Required: 0 script errors, 0 failed requests, 0 requests leaving the page, no blank screens, and no sideways scroll at 420 px.
   - Look at the key screenshots yourself: Home, an Ask answer, a dark-mode screen, phone width, and whatever is new.
5. **Scrub check before sharing.** The build refuses to finish on these, but confirm with a grep of the final file:
   - no supplier or model names (AI vendors, the database host, the connection service, speech providers);
   - no real people's names or real email addresses (only example.com and placeholders);
   - no code comments with personal notes.
   - Sample people are invented: Kavya Raman of Tidewell, Lumen Ventures, Harbor Capital, Coastline Logistics, Meera Pillai, Karthik Rao, Asha Menon.
6. **Deliver:**
   - Send the HTML file (SendUserFile, display attach).
   - Publish it as a private Artifact titled "SecondBrain UI Prototype", updating the existing one when possible.
   - Write a short CHANGES list: which screens are new since the last version, and what is canned (Ask answers are picked by keywords; Confirm, Send and Merge only change the page until reload; no real recording or audio; app logos are letter tiles).
   - For single screens, send the relevant PNGs from the verify run instead of the whole file.
7. **Persist kit changes.** Copy kit changes into `tools/ui_prototype/` in the repo.
   - Commit and push only when Akshay has asked to push.
   - If you do push, run the repo's scan for real names and keys first.

## Rules
- Never open or copy `~/SecondBrain` (real data) and never touch the installed app.
- Never invent features. If a screen doesn't exist in `secondbrain/ui`, say so, and offer a design mockup in the Design artifact type instead (using the `secondbrain-brand` skill).
- Report app bugs you notice while building (layout glitches, wrong classes) as a short list. Don't fix app code inside this task.
- Keep the report to Akshay short: the file, the artifact, the screen count, what's new, and anything broken.