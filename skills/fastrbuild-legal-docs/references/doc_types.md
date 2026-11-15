# fastrBuild Legal Document Types

Catalog of existing document types and guidance for adding new ones.

---

## Existing Types

### 1. Company NDA (`gen_nda.js` → `fastrBuild_NDA.docx`)

**Purpose:** Standard mutual NDA between fastrBuild and another company (corporate entity).

**Parties:**
- Party A: fastrBuild Intelligence (OPC) Pvt. Ltd. (Disclosing)
- Party B: `[FULL LEGAL NAME OF RECEIVING COMPANY]` (Receiving)

**Key structure:**
- Cover: "Non-Disclosure Agreement" / "Company / Corporate Entity" (orange subtitle)
- Parties section: registered address, CIN, represented by
- 10 clauses: Definitions → Confidential Information → Obligations → Exclusions → Term → Return/Destruction → Remedies → Governing Law → Dispute Resolution → General
- Signature block: 2-col table — Party A left, Party B right
  - Fields: Signature / Name / Designation / Date / Place
- Governing law: Kerala, India; arbitration under A&C Act 1996

**Pronoun/terminology:** company ("it"), "Representatives" (employees, directors, advisors, contractors)

**Output:** `fastrBuild_NDA.docx`

---

### 2. Individual NDA (`gen_nda_individual.js` → `fastrBuild_NDA_Individual.docx`)

**Purpose:** Unilateral NDA between fastrBuild and a natural person (freelancer, consultant, advisor, individual contractor).

**Parties:**
- Party A: fastrBuild Intelligence (OPC) Pvt. Ltd. (Disclosing)
- Party B: `[FULL NAME OF INDIVIDUAL]`, natural person, residential address, Aadhaar/Passport ID

**Differences from Company NDA:**
- Cover subtitle: "Individual / Natural Person" (orange)
- Pronouns: his/her throughout
- Clause 3.1(d): "Associates" (contractors, sub-contractors, advisors) instead of "Representatives"
- Clause 8.1: additional personal liability sentence
- Note callout: clarifies this is a unilateral NDA
- Right signature cell label: "Received and agreed by (Individual)"
  - Fields: Signature / Full Name / Date (no Designation)
- Document header: "Non-Disclosure Agreement (Individual)"

**Output:** `fastrBuild_NDA_Individual.docx`

---

### 3. DSC Custody Agreement (`gen_dsc_agreement.js` → `fastrBuild_DSC_Custody_Agreement.docx`)

**Purpose:** Non-Disclosure and Digital Signature Custody Agreement between fastrBuild and its legal service provider (Apnalegal). Governs both confidentiality AND strict custody/authorization protocols for fastrBuild Director's Digital Signature Certificate (DSC).

**Parties:**
- Party A: fastrBuild Intelligence (OPC) Pvt. Ltd. (Director: `[NAME]`)
- Party B: Apnalegal (legal service provider)

**Additional helpers used:**
- `criticalHead(num, title)` — for Clauses 4 and 5 (DSC Custody, Unauthorized Use)
- `callout(text)` — orange warning boxes within critical clauses
- `subSub(label, text)` — (a)(b)(c) sub-items
- Schedule A table (6 columns: Sr. / Portal / Filing Type / Document / Auth Email Ref / Remarks)
- `sigTable` (2-col party signatures) + `witnessTable` (2-col witness block, separate)

**Key legal points (do not dilute in any variation):**
- Clause 4 (DSC Custody): Mandatory Authorization Email to akshay@fastrbuild.com before ANY DSC use; must specify exact purpose, document, portal, date/time; only email reply counts (no WhatsApp/verbal); 48-hour non-response = deemed denial; DSC Log maintained; no sub-delegation
- Clause 5 (Unauthorized Use): Material breach + IT Act 2000 offence (Ss. 43, 65, 66, 66C, 66D, 71) + civil wrong; liquidated damages INR 2,00,000 per instance; FastrBuild may report to CERT-In, MCA, law enforcement, Certifying Authority
- Indian law: Indian Contract Act 1872, Companies Act 2013, IT Act 2000, DPDPA 2023, A&C Act 1996
- 14 clauses + Schedule A (DSC Activity Log table with 8 fillable rows)

**Output:** `fastrBuild_DSC_Custody_Agreement.docx`

---

## Adding a New Document Type

Follow this pattern:

### Step 1: Identify the doc

Common additions you might be asked for:
- **Statement of Work (SOW)** — scope, deliverables, milestones, payment schedule
- **Retainer Agreement** — monthly engagement terms, hours, payment
- **Vendor Agreement / MSA** — master services terms for a supplier
- **Employment / Contractor Agreement** — engagement terms for a hire
- **IP Assignment Agreement** — transfer of IP created under engagement
- **Letter of Intent (LOI)** — preliminary agreement for a deal

### Step 2: Create `gen_<type>.js`

```js
'use strict';
const { Document, Paragraph, TextRun, Table, TableRow, TableCell,
        AlignmentType, BorderStyle, ShadingType, WidthType } = require('docx');
const { Packer } = require('docx');
const fs   = require('fs');
const H    = require('./helpers');

const children = [
  ...H.buildCover('Statement of Work', 'Project Engagement'),
  // ... parties, clauses, schedule tables, signature block
];

const doc = new Document({
  sections: [{
    properties: {
      page: {
        size:   { width: H.PAGE_W, height: H.PAGE_H },
        margin: { top: H.MARGIN, bottom: H.MARGIN, left: H.MARGIN, right: H.MARGIN },
      }
    },
    children,
  }]
});

Packer.toBuffer(doc).then(buf => {
  fs.writeFileSync('fastrBuild_SOW.docx', buf);
  console.log('Done.');
});
```

### Step 3: Add to this file

Add an entry above with: purpose, parties, structure, key legal points, output filename.

### Step 4: Run and fix

```bash
node gen_<type>.js
bash scripts/fix_highlight.sh fastrBuild_<Type>.docx
```

---

## Naming Convention

| Doc type            | Generator script           | Output file                            |
|---------------------|----------------------------|----------------------------------------|
| Company NDA         | `gen_nda.js`               | `fastrBuild_NDA.docx`                  |
| Individual NDA      | `gen_nda_individual.js`    | `fastrBuild_NDA_Individual.docx`       |
| DSC Custody         | `gen_dsc_agreement.js`     | `fastrBuild_DSC_Custody_Agreement.docx`|
| SOW (example)       | `gen_sow.js`               | `fastrBuild_SOW.docx`                  |
| Retainer (example)  | `gen_retainer.js`          | `fastrBuild_Retainer_Agreement.docx`   |
