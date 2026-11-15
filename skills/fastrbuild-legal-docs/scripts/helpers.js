'use strict';
/**
 * fastrBuild Legal Docs — Shared Helpers
 * Require this from any generator script:
 *   const H = require('./helpers');
 */

const {
  Paragraph, TextRun, Table, TableRow, TableCell,
  AlignmentType, BorderStyle, ShadingType, WidthType,
} = require('docx');

// ─── Brand Constants ────────────────────────────────────────────────────────
const CHARCOAL   = '111111';
const ORANGE     = 'FF6A1A';
const MID_GRAY   = '999999';
const LIGHT_GRAY = 'DDDDDD';
const OFF_WHITE  = 'FFF8F5';
const FH = 'Calibri';   // heading font
const FB = 'Calibri';   // body font

// ─── Page Geometry (A4) ─────────────────────────────────────────────────────
const PAGE_W    = 11906;
const PAGE_H    = 16838;
const MARGIN    = 1134;              // 20 mm in DXA
const CW        = PAGE_W - 2 * MARGIN;   // 9638 — usable content width
const COL_HALF  = Math.floor(CW / 2);   // 4819

// ─── Core Text Helpers ──────────────────────────────────────────────────────

/**
 * Splits text at [bracket] and __ placeholder patterns.
 * Applies highlight:'yellow' to each placeholder run.
 * @param {string} text
 * @param {object} baseOpts  TextRun options to apply to all runs (font, size, color, bold…)
 * @returns {TextRun[]}
 */
function highlightRuns(text, baseOpts) {
  var parts = text.split(/(\[.*?\]|_+)/g);
  return parts.filter(function(p) { return p.length > 0; }).map(function(part) {
    var isPlaceholder = /^\[.*\]$/.test(part) || /^_+$/.test(part);
    var opts = Object.assign({}, baseOpts, { text: part });
    if (isPlaceholder) opts.highlight = 'yellow';
    return new TextRun(opts);
  });
}

// ─── Structural Paragraph Helpers ───────────────────────────────────────────

/**
 * Orange clause number + charcoal bold title.
 * Standard use: top-level clause headings.
 */
function clauseHead(num, title) {
  return new Paragraph({
    children: [
      new TextRun({ text: String(num) + '.', font: FH, size: 24, bold: true, color: ORANGE }),
      new TextRun({ text: ' ' + title,       font: FH, size: 24, bold: true, color: CHARCOAL }),
    ],
    spacing: { before: 300, after: 100 },
  });
}

/**
 * Like clauseHead but with an orange left border — use for high-stakes clauses
 * (e.g., DSC custody, liability, unauthorized use).
 */
function criticalHead(num, title) {
  return new Paragraph({
    children: [
      new TextRun({ text: String(num) + '.', font: FH, size: 24, bold: true, color: ORANGE }),
      new TextRun({ text: '  ' + title,      font: FH, size: 24, bold: true, color: CHARCOAL }),
    ],
    spacing: { before: 320, after: 100 },
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 4,  color: LIGHT_GRAY, space: 4 },
      left:   { style: BorderStyle.SINGLE, size: 24, color: ORANGE,     space: 8 },
    },
    indent: { left: 180 },
  });
}

/**
 * Sub-clause paragraph.
 * ref    — e.g. "1.1" or "(a)" — rendered bold charcoal
 * text   — clause body with [placeholder] patterns highlighted yellow
 */
function sub(ref, text) {
  return new Paragraph({
    children: [
      new TextRun({ text: ref, font: FB, size: 21, bold: true, color: CHARCOAL }),
      new TextRun({ text: ' ', font: FB, size: 21 }),
    ].concat(highlightRuns(text, { font: FB, size: 21, color: CHARCOAL })),
    indent:    { left: 440, hanging: 440 },
    alignment: AlignmentType.JUSTIFIED,
    spacing:   { before: 60, after: 80, line: 340, lineRule: 'auto' },
  });
}

/**
 * Deeper-indented sub-item — e.g. (a)(b)(c) inside a numbered sub-clause.
 */
function subSub(label, text) {
  return new Paragraph({
    children: [
      new TextRun({ text: label, font: FB, size: 21, bold: true, color: CHARCOAL }),
      new TextRun({ text: ' ',   font: FB, size: 21 }),
    ].concat(highlightRuns(text, { font: FB, size: 21, color: CHARCOAL })),
    indent:    { left: 880, hanging: 440 },
    alignment: AlignmentType.JUSTIFIED,
    spacing:   { before: 60, after: 80, line: 340, lineRule: 'auto' },
  });
}

/**
 * Orange left-border callout box with off-white fill.
 * Use for critical warnings or important notes.
 */
function callout(text) {
  return new Paragraph({
    children: highlightRuns(text, { font: FB, size: 20, color: CHARCOAL, bold: true }),
    border: {
      left: { style: BorderStyle.SINGLE, size: 24, color: ORANGE, space: 10 },
    },
    shading:   { type: ShadingType.CLEAR, fill: OFF_WHITE },
    indent:    { left: 360 },
    spacing:   { before: 160, after: 160 },
  });
}

/**
 * Plain body paragraph with optional yellow-highlighted placeholders.
 */
function body(text) {
  return new Paragraph({
    children:  highlightRuns(text, { font: FB, size: 21, color: CHARCOAL }),
    alignment: AlignmentType.JUSTIFIED,
    spacing:   { before: 60, after: 80, line: 340, lineRule: 'auto' },
  });
}

/**
 * Thin horizontal rule — LIGHT_GRAY bottom border on an empty paragraph.
 * Use between major sections.
 */
function rule() {
  return new Paragraph({
    children: [],
    border: {
      bottom: { style: BorderStyle.SINGLE, size: 6, color: LIGHT_GRAY, space: 1 },
    },
    spacing: { before: 200, after: 200 },
  });
}

// ─── Cover Page Builder ─────────────────────────────────────────────────────

/**
 * Returns an array of paragraphs for a standard cover page.
 * @param {string} docTitle      e.g. "Non-Disclosure Agreement"
 * @param {string} docSubtitle   e.g. "Company / Corporate Entity" (shown in orange)
 */
function buildCover(docTitle, docSubtitle) {
  return [
    // Wordmark
    new Paragraph({
      children: [
        new TextRun({ text: 'fastr', font: FH, size: 48, bold: true, color: CHARCOAL }),
        new TextRun({ text: 'Build', font: FH, size: 48, bold: true, color: ORANGE  }),
      ],
      spacing: { before: 400, after: 80 },
    }),
    // Orange underline rule
    new Paragraph({
      children: [],
      border: { bottom: { style: BorderStyle.SINGLE, size: 12, color: ORANGE, space: 1 } },
      spacing: { before: 0, after: 240 },
    }),
    // Company name
    new Paragraph({
      children: [
        new TextRun({ text: 'fastrBuild Intelligence (OPC) Pvt. Ltd.', font: FH, size: 22, color: MID_GRAY }),
      ],
      spacing: { before: 0, after: 800 },
    }),
    // Document title
    new Paragraph({
      children: [
        new TextRun({ text: docTitle, font: FH, size: 52, bold: true, color: CHARCOAL }),
      ],
      spacing: { before: 0, after: 160 },
    }),
    // Subtitle (orange)
    new Paragraph({
      children: [
        new TextRun({ text: docSubtitle, font: FH, size: 26, bold: true, color: ORANGE }),
      ],
      spacing: { before: 0, after: 600 },
    }),
    // Gray rule
    rule(),
  ];
}

// ─── Table Helpers ──────────────────────────────────────────────────────────

/** Returns border config with all sides set to NONE — use on signature/witness tables. */
function noBorders() {
  var none = { style: BorderStyle.NONE, size: 0, color: 'auto' };
  return { top: none, bottom: none, left: none, right: none, insideH: none, insideV: none };
}

/**
 * Single TableCell border config — all sides NONE.
 * Apply to each TableCell.borders when using noBorders() on the table.
 */
function cellNoBorders() {
  var none = { style: BorderStyle.NONE, size: 0, color: 'auto' };
  return { top: none, bottom: none, left: none, right: none };
}

/**
 * Builds a signature cell for a party.
 * @param {string} label     e.g. "For and on behalf of Party A"
 * @param {string[]} fields  e.g. ['Signature', 'Name', 'Designation', 'Date']
 *                           Fields after 'Signature' rendered as gray underlines.
 * @param {number} width     Cell width in DXA
 */
function makeSignCell(label, fields, width) {
  var children = [
    new Paragraph({
      children: [new TextRun({ text: label, font: FB, size: 18, bold: true, color: CHARCOAL })],
      spacing: { before: 0, after: 160 },
    }),
  ];

  fields.forEach(function(field, i) {
    var isSignature = i === 0;
    children.push(new Paragraph({
      children: [
        new TextRun({ text: field + ':  ', font: FB, size: 19, bold: true,
                      color: isSignature ? ORANGE : CHARCOAL }),
        new TextRun({ text: '_'.repeat(30), font: FB, size: 19,
                      color: isSignature ? ORANGE : LIGHT_GRAY }),
      ],
      spacing: { before: isSignature ? 200 : 120, after: isSignature ? 200 : 80 },
    }));
  });

  return new TableCell({
    children: children,
    width:    { size: width, type: WidthType.DXA },
    borders:  cellNoBorders(),
    margins:  { top: 200, bottom: 200, left: 0, right: 200 },
  });
}

// ─── Exports ─────────────────────────────────────────────────────────────────
module.exports = {
  // Constants
  CHARCOAL, ORANGE, MID_GRAY, LIGHT_GRAY, OFF_WHITE, FH, FB,
  PAGE_W, PAGE_H, MARGIN, CW, COL_HALF,
  // Paragraph helpers
  highlightRuns, clauseHead, criticalHead, sub, subSub, callout, body, rule,
  // Cover
  buildCover,
  // Table helpers
  noBorders, cellNoBorders, makeSignCell,
};
