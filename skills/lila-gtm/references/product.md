# LiLA product facts

## One-line description

LiLA is a suite of AI agents built for regulated engineering. It produces the requirements, test cases, safety analyses, traceability and compliance artifacts that safety standards demand, so engineers can spend their time on design.

Tagline: **"Built by automotive engineers. For the industries where software failure is not an option."**

## How to explain it simply

Every safety-critical program follows the V-model, which ASPICE and ISO 26262 require. Down the left side you write requirements and design. Up the right side you test and prove each requirement was met. Only 30-40% of the effort is actual coding and architecture. The rest is paperwork the regulations demand, written by hand. LiLA's agents each take one stretch of that paperwork.

It is not a chatbot and not a code assistant. ChatGPT writes text and Copilot writes code - neither produces ASPICE artifacts with traceability that an assessor would look at.

## Design principles

1. **Domain-native.** Understands ASPICE, ISO 26262 and MISRA C/C++ out of the box.
2. **Full SDLC coverage.** Agents span requirements through to defect management, so outputs connect.
3. **Compliance by design.** Standard attributes and traceability are attached as artifacts are created, not bolted on before the audit.
4. **Secure deployment.** Available on-premise and fully offline, on the customer's own infrastructure.
5. **Human-in-the-loop.** LiLA does the heavy lifting. A domain engineer reviews and signs off. This is what makes the output usable in a regulated process - say it with pride, not as a caveat.

## The seven agents

Lead with the four that have the most proof: **TestFlow, SpecFlow, FixFlow, ProcureFlow.** These are the four with customer testimonials in the deck.

### TestFlow - Integration and test engineering
Strongest proof. Best first agent for outreach.
- **Test case generation.** Reads requirements and generates test cases with ASPICE or ISO 26262 attributes attached, with bi-directional traceability. Engineers typically need at least 3 scenarios per requirement - this is where the 98% time saving comes from.
- **Test script generation.** Writes up to 70% of Python test scripts following the team's coding guidelines. The 30% tied to specific hardware or test benches stays with engineers.
- **Test report generation.** Builds standardised release reports from execution status. No more collating results into Excel or HTML by hand.
- **CI/CD pipeline support.** AI-assisted merge conflict resolution, scenario-based suggestions, and automatic notifications when tasks complete. Targets the problem where a single PR change can take 1-3 months to land because dev and integration teams are out of sync.
- Seen alongside: Jenkins, GitLab CI, Azure DevOps, JFrog, Polarion, DOORS, Jira, VS Code, PyCharm, dSPACE.

### SpecFlow - Requirements engineering
- **Document classification.** Sorts large volumes of unstructured specs by domain or feature.
- **Section-wise classification.** Maps document sections to features (CAN, network, diagnostics etc.) so function owners can start feature analysis.
- **Requirement extraction.** Pulls requirements out of structured and unstructured documents, so nothing gets missed.
- **Requirement classification.** Tags each requirement - business/system/hardware/software, functional/non-functional.
- Handles multi-lingual specs (e.g. German OEM specs).
- Who feels the pain: system engineers, system architects, requirement leads.

### FixFlow - Defect management
- **DLT log analysis.** Finds errors, anomalies and sequence breaks in large DLT log files.
- **Defect clustering.** Identifies the most error-prone modules before defects cascade.
- **Root cause analysis.** Matches failures against the knowledge base of known issues. Gets harder as software-defined vehicles produce bigger logs - that's the hook.
- **Duplicate detection.** Catches the same defect reported multiple times across teams.

### ProcureFlow - RFQ cost engineering
For Tier-1s and engineering service providers responding to OEM RFQs.
- **The problem:** RFQ responses are a relay race with no baton. Technical estimates effort, pre-sales estimates cost, sales estimates margin - each from scratch, each based on who's in the room. A near-identical project from 18 months ago gets ignored. Knowledge leaves when people leave.
- **What it does:** analyses incoming OEM RFQs, compares against the company's past projects, and produces consistent technical, effort and cost estimates. Includes delta calculation from existing projects and a human feedback loop.
- Who: sales, pre-sales, bid managers, system and technical architects.

### DocuFlow - Document intelligence
- Search and summarise across large document sets.
- Interpret diagrams in documents.
- RFQ/RFI proposal validation - scoring vendor responses.
- Document comparison, specification lookup bots.
- **Offline translation** - confidential specs can't go to online translation tools, and outsourced HMI translation is slow and expensive.

### SafeFlow - Standards and compliance
- MISRA C/C++ checking - static analysis licences are expensive (a team of 5-10 may share one) and guidelines change often.
- ASPICE - documentation and traceability across SYS, SWE, MAN and SUP process groups.
- ISO 26262 functional safety artifacts.

### CodeFlow - Code verification and documentation
- Unit test generation (developers avoid writing them).
- Code coverage - reaching 80%+ coverage is slow and often fudged.
- Context-aware code commenting.
- Design-aware documentation that stays in line with the actual system design.

## Industries

Automotive first. Then, in order of compliance pressure: aerospace and defence, railway and transit, industrial automation and robotics. Medical devices appear in the market sizing but are not an active target.

## Deployment models

- **SaaS** - credit-based subscription. Fastest start, good for pilots and smaller teams.
- **On-prem perpetual** - runs fully offline on the customer's infrastructure, unlimited usage for the purchased workflow.

Pricing detail is in `pricing.md`.

## Origin story

Acsia spent over a decade building safety-critical software for leading automotive OEMs - digital cockpits, e-mobility, AUTOSAR, functional safety, cybersecurity. While working through ASPICE compliance they hit the manual verification bottleneck themselves. They built LiLA to fix their own problem.

The line: **"We used to charge millions to do this manually for OEMs. Now we've packaged that expertise into software."**

Team named in the deck: Jijimon Chandran (Founder & CEO), Vasantharaj G (VP Technology & Innovation), Nibil P M (AVP & Head, Advanced Technology Group), Shajmaan S (Architect, AI/ML), Mohammed M R Ramees (Product Manager).
