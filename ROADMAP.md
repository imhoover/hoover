# Hoover Roadmap

Hoover is an early-stage open-source maintainer workflow toolkit. The roadmap is focused on practical OSS maintenance work: issue triage, PR review preparation, release communication, contributor handoff, and security-conscious workflow design.

The project will remain human-review-first. Automation should prepare maintainer briefs, not make final maintainer decisions.

## v0.1.0 — Deterministic maintainer brief generation

Status: current initial release.

Scope:

- Read Markdown and plain-text input.
- Generate a local maintainer brief.
- Extract likely problem statements.
- Extract reproduction signals.
- Extract risk signals.
- Suggest next actions.
- Render reviewable Markdown output.
- Keep the tool dependency-light and local-first.

## v0.2.0 — Structured JSON output

Goal: make Hoover easier to integrate with GitHub Actions, issue templates, dashboards, and maintainer tooling.

Planned fields:

- summary;
- problem_statement;
- reproduction_steps;
- risk_signals;
- missing_information;
- suggested_next_actions;
- confidence_notes.

## v0.3.0 — GitHub issue template integration

Goal: help maintainers convert structured or semi-structured issue reports into concise triage briefs.

Planned work:

- examples based on common GitHub issue templates;
- support for expected behavior / actual behavior / environment sections;
- detection of missing reproduction details;
- output designed for issue comments.

## v0.4.0 — Release-note brief generation

Goal: help maintainers convert PR notes, contributor updates, and changelog drafts into release communication.

Planned sections:

- user-facing changes;
- maintainer-facing changes;
- breaking changes;
- migration notes;
- known risks;
- follow-up tasks.

## v0.5.0 — Optional AI provider interface

Goal: allow optional AI-assisted maintainer workflows without making the core tool dependent on external services.

Principles:

- disabled by default;
- explicit configuration only;
- human review remains the default;
- generated output must be auditable;
- sensitive issue text should not be sent externally unless intentionally configured.

Potential use cases:

- issue summarization;
- reproduction-step extraction;
- PR triage briefs;
- risk detection;
- release-note drafting;
- regression-test suggestions.

## v0.6.0 — Multilingual issue report support

Goal: improve support for maintainers who receive issue reports from contributors in multiple languages.

Planned work:

- multilingual examples;
- preservation of important technical terms;
- better detection of environment details;
- clearer missing-information prompts;
- tests for Unicode and mixed-language input.

## Security and reliability roadmap

Planned work:

- add tests for malformed inputs;
- add tests for empty and very long files;
- add CI checks;
- review file-read and file-write boundaries;
- add security review checklist;
- review prompt-injection risks before any AI-assisted workflow is merged;
- document external-service behavior clearly if provider integrations are added.

## Six-month direction

The six-month goal is to make Hoover a lightweight, auditable maintainer assistant that can support real OSS workflows without hiding uncertainty or bypassing maintainer judgment.
