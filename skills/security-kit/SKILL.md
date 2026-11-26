---
name: security-kit
description: "Security and testing toolkit: security review and hardening, OWASP checks, Semgrep and CodeQL, supply-chain and GitHub Actions audits, false-positive checks, variant analysis, property-based, mutation and E2E (Playwright) testing, AI regression tests. Use for security audits or test strategy beyond Superpowers' TDD and review skills."
---

# security-kit

Router skill. The skills below are hidden from automatic listing to save context. Pick the one that fits the task, **Read its SKILL.md at the path shown and follow it**. Do not invoke them with the Skill tool: they are user-invocable only, so that call is refused. The user can also run any of them directly as `/name`.

If two fit, read the narrower one first. If none fit, say so and do the task without a sub-skill.

| Skill | Use for | Path |
|---|---|---|
| `ecc-agent-security-hardening` (`/agent-security-hardening`) | Security hardening guidance for AI agent frameworks that process untrusted content, invoke tools, write worksp… | `~/.claude/skills/ecc-agent-security-hardening/SKILL.md` |
| `ecc-ai-regression-testing` (`/ai-regression-testing`) | Regression testing strategies for AI-assisted development | `~/.claude/skills/ecc-ai-regression-testing/SKILL.md` |
| `ecc-browser-qa` (`/browser-qa`) | Run automated post-deploy UI verification with a browser automation MCP (claude-in-chrome, Playwright, or Pupp… | `~/.claude/skills/ecc-browser-qa/SKILL.md` |
| `ecc-e2e-testing` (`/e2e-testing`) | Playwright E2E testing patterns, Page Object Model, configuration, CI/CD integration, artifact management, and… | `~/.claude/skills/ecc-e2e-testing/SKILL.md` |
| `ecc-mcp-dependency-review` (`/mcp-dependency-review`) | Statically review MCP configuration for mutable package references before approval or CI, without executing di… | `~/.claude/skills/ecc-mcp-dependency-review/SKILL.md` |
| `ecc-react-testing` (`/react-testing`) | React component testing with React Testing Library, Vitest/Jest, MSW for network mocking, accessibility assert… | `~/.claude/skills/ecc-react-testing/SKILL.md` |
| `ecc-security-review` | Security review checklist and patterns for adding authentication, handling user input, managing secrets, creat… | `~/.claude/skills/ecc-security-review/SKILL.md` |
| `ecc-security-scan` (`/security-scan`) | Scan your Claude Code configuration (.claude/ directory) for security vulnerabilities, misconfigurations, and … | `~/.claude/skills/ecc-security-scan/SKILL.md` |
| `ecc-verification-loop` (`/verification-loop`) | Run a six-phase verification of a Claude Code session's work — build, type check, lint, tests with coverage, s… | `~/.claude/skills/ecc-verification-loop/SKILL.md` |
| `ecc-web-perimeter-owasp-2025-audit` (`/web-perimeter-owasp-2025-audit`) | Passive, non-destructive web perimeter security auditing mapped to OWASP Top 10:2025 surface leads, CDN Unkeye… | `~/.claude/skills/ecc-web-perimeter-owasp-2025-audit/SKILL.md` |
| `jeff-playwright-expert` (`/playwright-expert`) | writing E2E tests with Playwright, setting up test infrastructure, or debugging flaky browser tests | `~/.claude/skills/jeff-playwright-expert/SKILL.md` |
| `jeff-secure-code-guardian` (`/secure-code-guardian`) | implementing authentication/authorization, securing user input, or preventing OWASP Top 10 vulnerabilities — i… | `~/.claude/skills/jeff-secure-code-guardian/SKILL.md` |
| `jeff-security-reviewer` (`/security-reviewer`) | Identifies security vulnerabilities, generates structured audit reports with severity ratings, and provides ac… | `~/.claude/skills/jeff-security-reviewer/SKILL.md` |
| `jeff-test-master` (`/test-master`) | Generates test files, creates mocking strategies, analyzes code coverage, designs test architectures, and prod… | `~/.claude/skills/jeff-test-master/SKILL.md` |
| `playwright-cli` | Automate browser interactions, test web pages and work with Playwright tests | `~/.claude/skills/playwright-cli/SKILL.md` |
| `tob-agentic-actions-auditor` (`/agentic-actions-auditor`) | Audits GitHub Actions workflows for security vulnerabilities in AI agent integrations including Claude Code Ac… | `~/.claude/skills/tob-agentic-actions-auditor/SKILL.md` |
| `tob-codeql` (`/codeql`) | Scans a codebase for security vulnerabilities using CodeQL's interprocedural data flow and taint tracking anal… | `~/.claude/skills/tob-codeql/SKILL.md` |
| `tob-coverage-analysis` (`/coverage-analysis`) | Measures and interprets what a fuzzing campaign actually reaches, using llvm-cov, lcov, or a fuzzer's own cove… | `~/.claude/skills/tob-coverage-analysis/SKILL.md` |
| `tob-differential-review` (`/differential-review`) | Performs security-focused differential review of code changes | `~/.claude/skills/tob-differential-review/SKILL.md` |
| `tob-entry-point-analyzer` (`/entry-point-analyzer`) | Analyzes smart contract codebases to identify state-changing entry points for security auditing | `~/.claude/skills/tob-entry-point-analyzer/SKILL.md` |
| `tob-fp-check` (`/fp-check`) | Systematically verifies suspected security bugs to eliminate false positives, producing a TRUE POSITIVE or FAL… | `~/.claude/skills/tob-fp-check/SKILL.md` |
| `tob-mutation-testing` (`/mutation-testing`) | Configures mewt or muton campaigns, analyzes surviving mutants, and investigates bugs exposed by testing gaps | `~/.claude/skills/tob-mutation-testing/SKILL.md` |
| `tob-post-patch-validation` (`/post-patch-validation`) | Validates security patches with reproducible baseline-versus-patched evidence, including original exploits, ro… | `~/.claude/skills/tob-post-patch-validation/SKILL.md` |
| `tob-property-based-testing` (`/property-based-testing`) | Writes, reviews, and debugs property-based tests — Hypothesis, fast-check, proptest, jqwik, rapid, and Echidna… | `~/.claude/skills/tob-property-based-testing/SKILL.md` |
| `tob-sarif-parsing` (`/sarif-parsing`) | Parses and processes SARIF files from static analysis tools like CodeQL, Semgrep, or other scanners | `~/.claude/skills/tob-sarif-parsing/SKILL.md` |
| `tob-second-opinion` (`/second-opinion`) | Gets independent code reviews from Codex or Antigravity for uncommitted changes, branch diffs, and commits | `~/.claude/skills/tob-second-opinion/SKILL.md` |
| `tob-semgrep` (`/semgrep`) | Runs a Semgrep security scan over a codebase: detects languages, selects rulesets, presents the plan for expli… | `~/.claude/skills/tob-semgrep/SKILL.md` |
| `tob-sharp-edges` (`/sharp-edges`) | Identifies error-prone APIs, dangerous configurations, and footgun designs that enable security mistakes | `~/.claude/skills/tob-sharp-edges/SKILL.md` |
| `tob-spec-to-code-compliance` (`/spec-to-code-compliance`) | Check code against the documentation that specifies it - which requirements hold, which the code contradicts, … | `~/.claude/skills/tob-spec-to-code-compliance/SKILL.md` |
| `tob-supply-chain-risk-auditor` (`/supply-chain-risk-auditor`) | Audits a project's dependencies for supply-chain risk: version-matched advisories for direct dependencies and … | `~/.claude/skills/tob-supply-chain-risk-auditor/SKILL.md` |
| `tob-variant-analysis` (`/variant-analysis`) | Hunts for the other instances of a bug already found — the variants of one root cause across a codebase | `~/.claude/skills/tob-variant-analysis/SKILL.md` |
| `webapp-testing` | Toolkit for interacting with and testing local web applications using Playwright | `~/.claude/skills/webapp-testing/SKILL.md` |
