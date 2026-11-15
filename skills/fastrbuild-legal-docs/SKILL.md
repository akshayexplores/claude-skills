---
name: fastrbuild-legal-docs
description: >
  Generate branded legal documents (.docx) for fastrBuild Intelligence (OPC) Pvt. Ltd.
  Use this skill whenever the user asks to create an NDA, contract, agreement, or any
  legal Word document for fastrBuild. Supports company NDAs, individual NDAs, DSC custody
  agreements, and new custom document types. Automatically applies fastrBuild's brand
  identity, highlights all placeholder fields in yellow, and patches OOXML compatibility.
  Triggers on "draft an NDA", "create a contract", "prepare a legal agreement",
  "make a Word doc for fastrBuild", "generate a [document type] for FastrBuild".
---

# fastrBuild Legal Document Generator

Produces professionally branded, editable `.docx` legal documents for **fastrBuild Intelligence (OPC) Pvt. Ltd.** using Node.js (`docx` npm package). All fillable fields are highlighted yellow so the recipient knows exactly what to fill in.

---

## Brand Identity (hardcoded — do not change)

```js
const CHARCOAL  = '111111';   // body text, headings
const ORANGE    = 'FF6A1A';   // accent: numbers, wordmark "Build", rules
const MID_GRAY  = '999999';   // subtitles, metadata
const LIGHT_GRAY = 'DDDDDD';  // horizontal rules, table borders
const OFF_WHITE  = 'FFF8F5';  // callout box fill
const FH = 'Calibri';         // heading font
const FB = 'Calibri';         // body font
```

**Wordmark pattern** — always render as two runs in the same paragraph:
```js
new TextRun({ text: 'fastr', font: FH, size: 48, bold: true, color: CHARCOAL }),
new TextRun({ text: 'Build', font: FH, size: 48, bold: true, color: ORANGE  }),
```

**Page geometry (A4)**:
```js
const PAGE_W  = 11906;                    // DXA (1440 DXA = 1 inch)
const PAGE_H  = 16838;
const MARGIN  = 1134;                     // 20 mm
const CW      = PAGE_W - 2 * MARGIN;     // 9638 — usable content width
const COL_HALF = Math.floor(CW / 2);     // 4819 — half-width column
```

---

## Core Helpers

All shared functions live in `scripts/helpers.js`. **Always require this file** at the top of any generator script:

```js
const H = require('./helpers');
// then use: H.highlightRuns(), H.clauseHead(), H.sub(), H.criticalHead(), H.callout(), H.subSub()
// constants: H.CHARCOAL, H.ORANGE, H.CW, H.COL_HALF, etc.
```

Key functions — read `scripts/helpers.js` for full signatures:

| Function | Purpose |
|---|---|
| `highlightRuns(text, baseOpts)` | Splits text on `[bracket]` and `__` patterns; applies `highlight: 'yellow'` to each placeholder |
| `clauseHead(num, title)` | Orange clause number + charcoal bold title |
| `sub(ref, text)` | Sub-clause paragraph — `ref` in bold charcoal, `text` with yellow highlights, justified, indented |
| `criticalHead(num, title)` | Like clauseHead but with orange left border — use for high-stakes clauses |
| `callout(text)` | Orange left-border callout box with off-white fill — use for critical warnings |
| `subSub(label, text)` | Deeper-indented (a)(b)(c) items |
| `makeSignCell(label, fields)` | Signature table cell: orange Signature line, gray Name/Designation/Date lines |
| `noBorders()` | Returns border config with all sides `NONE` — use on all signature/witness tables |

---

## Workflow for Any Document

### 1. Gather inputs
Ask the user (or infer from context):
- Document type (see Reference: `references/doc_types.md`)
- Party details (names, addresses, CIN/Aadhaar, jurisdiction)
- Any custom clauses or modifications

### 2. Create the generator script

Create `gen_<doctype>.js` in the outputs folder. Structure:

```js
'use strict';
const { Document, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, BorderStyle, ShadingType, WidthType,
        PageOrientation, convertInchesToTwip } = require('docx');
const { Packer } = require('docx');
const fs = require('fs');
const H = require('./helpers');

// --- Build content arrays ---
const children = [
  ...H.buildCover('Non-Disclosure Agreement', 'Company / Corporate Entity'),
  ...buildParties(),
  ...buildClauses(),
  ...buildSignatureBlock(),
];

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size: { width: H.PAGE_W, height: H.PAGE_H },
        margin: { top: H.MARGIN, bottom: H.MARGIN, left: H.MARGIN, right: H.MARGIN },
      }
    },
    children,
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('fastrBuild_<DocName>.docx', buf);
  console.log('Done.');
});
```

### 3. Run and post-process

```bash
cd /path/to/outputs
npm install docx          # if not already installed
node gen_<doctype>.js

# Fix the highlightCs OOXML bug (mandatory — Word/LibreOffice will reject without this)
bash scripts/fix_highlight.sh fastrBuild_<DocName>.docx
```

### 4. Present the file

Use `mcp__cowork__present_files` with the final `.docx` path.

---

## Known OOXML Bug: `<w:highlightCs>`

`docx-js` incorrectly emits `<w:highlightCs w:val="yellow"/>` alongside the valid `<w:highlight w:val="yellow"/>`. This element is not in the OOXML schema and causes validation failures in strict-mode readers.

**Fix is automated** — `scripts/fix_highlight.sh` handles it. Always run it after generation. See the script for details.

---

## Adding a New Document Type

1. Read `references/doc_types.md` — it has the anatomy of each existing type.
2. Create `gen_<newtype>.js` using the pattern above.
3. Reuse helpers from `scripts/helpers.js`. Add new helper functions there if you're building something reusable (e.g., a Schedule table, a RACI matrix).
4. Add an entry to `references/doc_types.md` so future invocations know it exists.
5. The output filename convention: `fastrBuild_<DocName>.docx` (e.g., `fastrBuild_SOW.docx`).

---

## Table Rules (avoid common mistakes)

- Set **both** `columnWidths` on `Table` AND `width` on each `TableCell` in DXA — one alone is not enough.
- Use `ShadingType.CLEAR` (never `SOLID`) for cell fills, or you get black backgrounds.
- Signature/witness tables always use `noBorders()` on both the table and each cell.
- Column widths must sum exactly to `CW` (9638) or a defined sub-width.

---

## Reference Files

- `scripts/helpers.js` — all shared helper functions and brand constants
- `scripts/fix_highlight.sh` — post-processing pipeline for OOXML fix
- `references/doc_types.md` — catalog of existing doc types with key structural notes
