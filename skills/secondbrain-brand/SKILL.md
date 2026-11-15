---
name: "secondbrain-brand"
description: "Apply SecondBrain's brand (colours, type, lake painting, voice, claims rules) to any SecondBrain app screen, website, deck, video, social post or document, or review one for brand fit."
---

# SecondBrain brand

Use this for anything that carries the SecondBrain name or look: app UI, the website, pitch decks, launch video, social posts, share images, emails and documents. It does not apply to fastrBuild, Vajra, LiLA or Akshay's personal brand.

## Source of truth

The full guide is the Design System artifact "SecondBrain": https://claude.ai/artifact/M8QML332NQYVHgNt5zsyY6

- Read it with the Artifact tool (`action: read`), never by web fetch: `project/README.md` (brand book) first, then `project/voice.md` before writing words and `project/channels.md` before making something for a specific surface. Tokens are in `project/tokens.json`, component styles in `project/components/bundle.css`.
- Assets (logo, the four painting panels, app screens) are listed in the guide's Assets view; reuse them, never redraw them.
- If the artifact can't be read, use the summary below and say so.
- The guide wins over this summary if they differ.

## Summary

**Name.** "SecondBrain", one word. It is a placeholder until the new name is chosen: keep it in one swappable place (a BRAND constant, one text style, one master slide). Not a Vajra product; never put the Vajra name or mark beside it.

**Logo.** Slate (#46647D) rounded tile, white concentric rings, gold (#E3A03A) dot. Use the file as is. Lockup: icon left, name in Creato Display 500 right.

**Colour (light / dark).**
- canvas #EBE2D6 / #120E0C, paper #FFFCF8 / #1B1613, paper-sunk #F7F1E8 / #2A231E
- ink #2A211B / #F4ECE2, ink-2 #5E5148 / #CDBFB1, ink-3 #6C5E53 / #B0A193
- plum (brand dark, primary buttons) #46303F / #F5EEE8, text on it #FFF8F2 / #2A211B; night field #1C1524
- persimmon (accent, links, focus, one emphasised word) #B04A31 / #F3AA8B; as text #9A3B23 / #F7BCA2; wash peach #F8E6DB / #4B3433
- ember #E8643F: Record and the new-items dot only; text on it #2A1008, never white
- gold #E0A030 = owed / today / warnings; live green #5F9A6B = recording only; red #B5362A = errors and overdue only (always with a word)

**Type.** Creato Display (500, tight tracking) for headlines and marketing only. Inter (cv11, ss01, tabular figures for numbers) for the app, body and anything read at length. Sentence case. No uppercase labels, no eyebrow labels above headings. Headline pattern: two short sentences, the second in persimmon.

**Background.** The app's pastel lake painting (hills, a cottage, still water, wildflowers), four panels: morning, day, evening, night. Text sits on frosted glass or paper, never straight on the painting (except the Home greeting). No glass inside glass. Never swap the painting for photographs, gradients or stock images. Stories move from morning to night.

**Shape and motion.** Corners: 10 controls, 20 cards, 22 glass, 26 Ask bar only, pill 999. One card per moment, no card inside a card. One authored motion per screen; honour reduced motion.

**Voice.** Plain, calm, warm, exact. Short sentences, no hype words, no exclamation marks. The app speaks in warm first person about its own work ("I've kept them safe for you"); privacy text stays literal. Main line: "AI meeting notes. No bot in your call." Closing line: "Meetings in. Work done." CTA: "Join the launch list". Promises are the payoff, never the headline.

**Never.** AI model or vendor names anywhere users see them. Testimonials, logos, user counts, ratings, accuracy claims or competitor comparisons. Real public figures' quotes. "100% offline", "end-to-end encrypted", "SOC 2", "HIPAA". Calling it a clone. Unapproved privacy or data claims (mark drafts as draft). Emoji in UI, slides or the site.

## How to work

1. Read the guide (or this summary) before designing or writing.
2. Build from the tokens by name; don't introduce new colours or fonts. If something truly needs a new token, ask Akshay first.
3. Check text contrast at 4.5:1 (3:1 for 24px+ and for marks) in light and dark.
4. When reviewing, list each break of the rules with the rule it breaks and the fix, shortest first.
5. If the request conflicts with the guide, say so in one line and ask before going ahead.