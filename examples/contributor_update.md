# Contributor update example

A contributor opened a PR that updates parser behavior for issue reports with mixed Markdown sections.

## What changed

- Added detection for reproduction-related headings.
- Updated parser tests for multiline issue reports.
- Improved output wording for missing environment details.

## Open questions

- Should the generated brief include a separate `missing_information` section?
- Should the parser preserve the original heading text?
- Should JSON output be part of this change or a separate milestone?

## Risk

The change may alter current Markdown output snapshots, so regression tests need to be reviewed before merge.

## Maintainer request

Please review the parser behavior, confirm whether output wording is acceptable, and decide whether JSON output should be handled in a follow-up issue.
