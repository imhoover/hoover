# Contributing to Hoover

Thank you for your interest in contributing to Hoover.

Hoover is intentionally small and reviewable. The project values clear behavior, readable code, deterministic defaults, and maintainer-friendly output over complex automation.

## Project principles

- Human review remains the default.
- Output should be easy to paste into issues, pull requests, release notes, or maintainer handoffs.
- The codebase should remain approachable for new contributors.
- Optional AI-assisted workflows should not make the core tool dependent on external services.
- Claims in documentation should be accurate and should not overstate adoption, usage, or maturity.

## Development setup

```bash
git clone https://github.com/imhoover/hoover.git
cd hoover
python -m pip install -e .
python -m pip install pytest
pytest
```

## Running the CLI locally

```bash
hoover examples/bug_report.md
```

From standard input:

```bash
cat examples/bug_report.md | hoover
```

Write output to a file:

```bash
hoover examples/bug_report.md --output brief.md
```

## Ways to contribute

You can help by improving:

- parsing behavior;
- output formatting;
- structured JSON output;
- examples;
- documentation;
- tests;
- multilingual issue examples;
- GitHub issue template integration;
- release-note brief generation;
- security and reliability checks.

## Proposing a new maintainer workflow

A good workflow proposal should explain:

1. the maintainer pain point;
2. the input Hoover would receive;
3. the output Hoover should generate;
4. how a maintainer would review the output;
5. what risks or failure modes should be considered.

Examples of maintainer workflows:

- convert a long bug report into a triage brief;
- convert PR notes into review tasks;
- convert contributor updates into handoff notes;
- convert release notes into user-facing and maintainer-facing summaries;
- detect missing reproduction details from an issue report.

## What makes a good first issue

A good first issue should be small, reviewable, and tied to a concrete maintainer use case.

Good first issue areas:

- add a realistic example input;
- add a parser test for a known issue-report pattern;
- improve wording in generated output;
- document one CLI workflow;
- add a multilingual issue example;
- improve handling of empty or malformed input.

## Pull request guidelines

Before opening a pull request, please confirm that:

- the change has a clear maintainer use case;
- behavior remains deterministic by default;
- tests are included or updated when behavior changes;
- documentation is updated when user-facing behavior changes;
- generated output remains easy for a maintainer to audit;
- optional external-service behavior is disabled by default.

## Review expectations

Maintainers will review for:

- clarity;
- predictable behavior;
- test coverage;
- security and privacy impact;
- documentation quality;
- practical usefulness for OSS maintainers.
