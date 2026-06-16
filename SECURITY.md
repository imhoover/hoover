# Security Policy

## Supported versions

Hoover is currently in early development. Security-related fixes will be applied to the latest version on the default branch.

## Reporting a security issue

Please do not publish sensitive details in a public issue. Instead, open a minimal public issue stating that a security concern exists, without including exploit details or private information.

The maintainer will follow up to coordinate the next step.

## Project security principles

- Hoover is local-first by default.
- The core parser does not require external services.
- User-provided issue text should not be sent to external services unless the user intentionally enables that workflow.
- Optional provider integrations should be explicit, disabled by default, and reviewable.
- Generated output should be treated as a draft for human maintainer review.

## Current security scope

The current version processes local Markdown or plain-text input and generates local Markdown output. It does not require network access, external APIs, credentials, or background services.

## Security roadmap

Planned security and reliability work includes:

- safer handling for very long input files;
- tests for malformed input;
- tests for unusual Unicode and multilingual reports;
- CI checks for parser and CLI behavior;
- review of file-read and file-write boundaries;
- a security review checklist for future provider integrations;
- prompt-injection review if optional AI-assisted workflows are added;
- clear documentation for any future external-service configuration.

## Codex Security interest

As Hoover grows, Codex Security support would be useful for reviewing parser behavior, CLI boundaries, dependency changes, file-handling assumptions, and future optional AI-assisted integrations.
