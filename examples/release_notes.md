# Release notes input example

## Contributor updates

- Added support for reading issue reports from standard input.
- Improved parser behavior for lines that contain Japanese text.
- Added tests for empty input and basic Markdown issue reports.
- Updated README usage examples.

## Maintainer notes

The release should communicate that Hoover is still early-stage and local-first. Avoid making claims about broad adoption or production usage.

## User-facing changes

Users can now pipe issue text directly into Hoover and generate a Markdown maintainer brief without creating a temporary file.

## Risks

This may be a breaking change if downstream scripts assumed that a source file path was always required.

## Follow-up tasks

Please add release-note brief generation, structured JSON output, and tests for malformed input.
