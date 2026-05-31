# Hoover

Hoover is a small, dependency-light toolkit for open source maintainers who need to turn issue reports, release notes, and contributor updates into clear maintainer briefs.

The goal is practical maintenance support: reduce the time spent re-reading long issue threads, standardize triage notes, and make handoff between contributors easier.

## What it does

Hoover currently provides a local command-line tool that:

- reads a Markdown or plain-text issue report;
- extracts likely problem statements, reproduction steps, risks, and action items;
- creates a concise maintainer brief;
- keeps output deterministic and reviewable;
- works without requiring external services.

## Why this project exists

Open source maintainers often lose time converting unstructured reports into actionable work. Hoover is designed as a simple first layer before deeper automation: it produces a readable brief that a maintainer can review, edit, and paste into an issue, pull request, or release plan.

This repository is intentionally small so that contributors can understand the codebase quickly.

## Installation

```bash
python -m pip install -e .
```

## Usage

```bash
hoover examples/issue.md
```

Output example:

```markdown
# Maintainer Brief

## Summary
A concise summary generated from the source issue text.

## Signals
- Potential reproduction detail detected
- Potential action item detected

## Suggested next actions
- Confirm expected behavior
- Request missing environment details
- Add or update a regression test
```

## Project status

Early-stage OSS project. The current version focuses on deterministic text parsing and maintainer-friendly output. Future work may add optional AI-assisted workflows, while keeping human review as the default.

## Roadmap

- Add structured JSON output
- Add GitHub issue template integration
- Add release-note brief generation
- Add optional provider interface for AI-assisted summarization
- Improve tests for edge cases and multilingual issue reports

## Contributing

Contributions are welcome. Please see [CONTRIBUTING.md](CONTRIBUTING.md).

## License

MIT License. See [LICENSE](LICENSE).
