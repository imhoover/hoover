# Hoover v0.1.0 — Initial public release

Hoover is an open-source maintainer workflow toolkit for turning long, unstructured issue reports, PR notes, release updates, and contributor messages into clear maintainer briefs.

This first release focuses on deterministic, local-first maintainer support.

## What is included

- Markdown and plain-text input support
- Maintainer brief generation
- Extraction of likely problem statements, reproduction details, risks, and action items
- Reviewable output designed for GitHub issues, pull requests, and release planning
- Examples for common maintainer workflows
- Tests for the initial parsing workflow
- MIT license
- Contributing guide
- Code of conduct
- Security policy

## Project status

Hoover is early-stage. The goal of this release is to provide a small, understandable base for future maintainer-focused workflows.

Future work will focus on structured JSON output, GitHub issue template integration, release-note brief generation, multilingual issue reports, and optional AI-assisted workflows while keeping human review as the default.

## Human review

Hoover output should be treated as a draft brief for maintainer review. The tool is intended to reduce repetitive reading and improve handoff quality, not to make final maintainer decisions automatically.
