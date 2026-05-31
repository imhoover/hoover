# Codex for OSS application draft

This document contains draft answers for the Codex for Open Source application form.

## GitHub username

```text
imhoover
```

## Repository URL

```text
https://github.com/imhoover/hoover
```

## Project name

```text
Hoover
```

## Project description

```text
Hoover is an open source maintainer toolkit that turns unstructured issue reports into concise maintainer briefs. It helps maintainers identify problem statements, reproduction signals, risk signals, and suggested next actions from Markdown or plain-text reports. The project is intentionally small, dependency-light, and reviewable so contributors can understand and improve it quickly.
```

## Why does this repository qualify?

```text
Hoover qualifies as an open source maintenance project because it is designed to reduce the manual workload involved in issue triage, contributor handoff, and release preparation. Many maintainers spend significant time converting unclear reports into actionable tasks. Hoover provides a deterministic, local-first workflow for creating structured maintainer briefs from raw issue text.

The repository includes an MIT license, contribution guide, test suite, CLI implementation, GitHub Actions workflow, and issue template. As maintainer, I am responsible for project direction, code review, documentation, issue handling, and release planning. OpenAI support would help accelerate the project from an early-stage maintainer utility into a more useful workflow for OSS maintainers.
```

## How will you use API credits?

```text
API credits would be used to build optional AI-assisted maintainer workflows on top of Hoover's deterministic core. Planned uses include issue triage assistance, pull request review summaries, release-note draft generation, documentation improvement suggestions, and multilingual issue report analysis.

The credits would also help test provider interfaces, compare deterministic and AI-assisted outputs, and build examples that keep human review as the default. The goal is not to replace maintainers, but to reduce repetitive maintenance work while preserving transparent, reviewable outputs.
```

## Role in the project

```text
I am the project creator and primary maintainer. I manage the repository, define the roadmap, write the code and documentation, maintain tests, review issues, and plan future releases.
```

## Maintenance plan

```text
The short-term maintenance plan is to stabilize the CLI, improve parsing quality, add structured JSON output, expand tests for multilingual reports, and document practical maintainer workflows. The next phase is to add optional AI-assisted workflows for issue triage, PR summaries, and release-note generation while keeping the core tool local-first and deterministic.
```
