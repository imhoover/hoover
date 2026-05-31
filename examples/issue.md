The hoover command fails when the issue report includes both English and Japanese headings.

Environment:
- Python 3.12
- macOS

Steps to reproduce:
1. Create a Markdown file with Japanese section headings.
2. Run `hoover examples/issue.md`.
3. Review the generated maintainer brief.

Expected behavior:
The generated brief should detect the reproduction details and suggested next actions.

Actual behavior:
Some important lines are not grouped clearly.

Please improve multilingual issue report handling and add a regression test.
