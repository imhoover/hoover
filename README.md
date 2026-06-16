# Hoover

Hoover is an open-source maintainer workflow toolkit. It helps OSS maintainers turn long, unstructured issue reports, PR notes, release updates, and contributor messages into clear, actionable maintainer briefs.

The project is intentionally small, local-first, and reviewable. The current version focuses on deterministic text parsing and maintainer-friendly output. Optional AI-assisted workflows may be added later, but human review will remain the default.

## Who this is for

Hoover is for maintainers of open-source projects who need a faster way to prepare triage notes, review handoffs, release communication, and contributor follow-up from messy written input.

It is especially useful when maintainers receive:

- long issue reports with missing context;
- PR notes that need to be converted into review tasks;
- contributor updates that need action items;
- release notes that need to be rewritten into maintainer-facing and user-facing summaries;
- multilingual or inconsistent reports that still need structured follow-up.

## Why maintainers need it

Open-source maintenance is often blocked by unstructured communication rather than code alone. Maintainers spend time rereading long threads, identifying missing information, separating user impact from implementation detail, and turning informal reports into next actions.

Hoover is designed as a practical first layer for that work. It does not replace maintainer judgment. It creates a brief that a maintainer can review, edit, and paste into a GitHub issue, pull request, release plan, or contributor handoff.

## Current capabilities

Hoover currently provides a local command-line tool that:

- reads Markdown or plain-text input;
- extracts likely problem statements;
- identifies reproduction signals;
- identifies risk signals;
- suggests next actions;
- renders a concise maintainer brief in Markdown;
- works without requiring external services;
- keeps output deterministic and reviewable.

## Installation

```bash
python -m pip install -e .
```

## Usage

```bash
hoover examples/bug_report.md
```

You can also read from standard input:

```bash
cat examples/bug_report.md | hoover
```

Write the generated brief to a file:

```bash
hoover examples/bug_report.md --output brief.md
```

## Example input

```markdown
The CLI fails on Python 3.12 when the issue body contains Japanese text.

Steps to reproduce:
1. Create a Markdown issue report with Japanese text.
2. Run `hoover issue.md`.
3. The command exits with an error.

This may affect maintainers triaging international bug reports.
Please add a regression test and confirm UTF-8 handling.
```

## Example output

```markdown
# Maintainer Brief

## Summary
The CLI fails on Python 3.12 when the issue body contains Japanese text.

## Problem statements
- The CLI fails on Python 3.12 when the issue body contains Japanese text.

## Reproduction signals
- Steps to reproduce:
- Run `hoover issue.md`.

## Risk signals
- This may affect maintainers triaging international bug reports.

## Suggested next actions
- Please add a regression test and confirm UTF-8 handling.
```

## Human-review-first principle

Hoover is not designed to make final maintainer decisions automatically. Its output is a draft brief for human review.

Project principles:

- maintainers remain responsible for decisions;
- generated briefs should be easy to audit;
- external services are not required by default;
- optional AI-assisted workflows must be explicit and reviewable;
- private or sensitive issue text should not be sent anywhere unless a maintainer intentionally enables that behavior.

## Roadmap

See [ROADMAP.md](ROADMAP.md) for the full roadmap.

Near-term priorities:

- structured JSON output;
- GitHub issue template integration;
- release-note brief generation;
- improved test coverage for malformed and long inputs;
- multilingual issue report examples;
- optional AI provider interface with human review as the default.

## Codex for OSS alignment

Hoover is directly focused on OSS maintainer work: issue triage, review preparation, contributor handoff, release communication, testing follow-up, and security-conscious workflow design.

If selected for Codex for Open Source support, the project would use the support for core maintainer workflows only:

- issue summarization;
- reproduction-step extraction;
- PR triage briefs;
- release-note drafting;
- regression-test suggestions;
- structured JSON output;
- security review for future optional AI-assisted integrations.

The project is early-stage and does not claim broad adoption. Its value proposition is narrower and practical: reduce repetitive maintainer reading and make OSS maintenance work more structured, auditable, and easier to hand off.

## Project status

Hoover is an early-stage OSS project. The repository is public, MIT-licensed, and structured for contributor review. The current implementation is intentionally small so that contributors can understand and improve it quickly.

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md).

Good first contribution areas include examples, tests, output formatting, JSON output, issue-template integration, and multilingual issue reports.

## Security

Please see [SECURITY.md](SECURITY.md). Hoover is local-first by default and does not require external services in the current version.

## License

MIT License. See [LICENSE](LICENSE).
