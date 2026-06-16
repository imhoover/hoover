# Bug report example

The Hoover CLI fails when the input issue report contains mixed English and Japanese headings.

## Environment

- Python 3.12
- macOS 14
- Terminal: zsh

## Steps to reproduce

1. Create a Markdown issue report with English and Japanese section headings.
2. Add reproduction steps under a Japanese heading.
3. Run `hoover examples/bug_report.md`.
4. Review the generated maintainer brief.

## Expected behavior

The generated brief should identify the problem statement, reproduction signals, risk signals, and suggested next actions.

## Actual behavior

Important reproduction details are not always grouped clearly.

## Impact

This may affect maintainers who receive multilingual issue reports from contributors.

## Requested maintainer action

Please improve multilingual issue handling and add a regression test for mixed-language issue reports.
