# Contributing to Hoover

Thank you for your interest in contributing to Hoover.

Hoover is intentionally small and reviewable. The project values clear behavior, readable code, and maintainer-friendly output over complex automation.

## Ways to contribute

You can help by:

- reporting issues with unclear or incorrect maintainer briefs;
- adding tests for edge cases;
- improving documentation and examples;
- improving multilingual issue-report handling;
- proposing small CLI improvements.

## Development setup

```bash
git clone https://github.com/imhoover/hoover.git
cd hoover
python -m pip install -e .
python -m pip install pytest
pytest
```

## Pull request guidelines

Before opening a pull request, please confirm that:

- the change has a clear maintainer use case;
- the behavior is deterministic by default;
- tests are included or updated when behavior changes;
- documentation is updated when user-facing behavior changes.

## Project principles

- Human review remains the default.
- Output should be easy to paste into issues, pull requests, or release notes.
- The codebase should remain approachable for new contributors.
- Optional AI-assisted workflows should not make the core tool dependent on external services.
