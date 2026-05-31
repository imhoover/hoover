from hoover.parser import build_brief, normalize_text, render_markdown, split_sentences


def test_normalize_text_collapses_extra_whitespace():
    assert normalize_text("A   bug\n\n\nneeds   help") == "A bug\n\nneeds help"


def test_split_sentences_handles_markdown_lines():
    source = "Bug report.\nSteps to reproduce:\nRun hoover input.md"
    assert split_sentences(source) == [
        "Bug report.",
        "Steps to reproduce:",
        "Run hoover input.md",
    ]


def test_build_brief_detects_problem_and_action_items():
    source = "The command fails on Python 3.12. Please add a regression test and fix it."
    brief = build_brief(source)

    assert "fails" in brief.summary
    assert brief.problem_statements
    assert brief.action_items


def test_render_markdown_contains_sections():
    brief = build_brief("Production users get an error. Steps: run hoover issue.md")
    markdown = render_markdown(brief)

    assert "# Maintainer Brief" in markdown
    assert "## Summary" in markdown
    assert "## Suggested next actions" in markdown
