from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Iterable


@dataclass(frozen=True)
class MaintainerBrief:
    """Structured summary for a maintainer to review."""

    summary: str
    problem_statements: list[str]
    reproduction_steps: list[str]
    risks: list[str]
    action_items: list[str]


def normalize_text(text: str) -> str:
    """Normalize whitespace while preserving paragraph boundaries."""
    cleaned = text.replace("\r\n", "\n").replace("\r", "\n")
    cleaned = re.sub(r"[ \t]+", " ", cleaned)
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)
    return cleaned.strip()


def split_sentences(text: str) -> list[str]:
    """Split text into readable sentence-like units without heavy dependencies."""
    text = normalize_text(text)
    if not text:
        return []

    parts = re.split(r"(?<=[.!?。！？])\s+|\n+", text)
    return [part.strip(" -\t") for part in parts if part.strip(" -\t")]


def _contains_any(value: str, keywords: Iterable[str]) -> bool:
    lowered = value.lower()
    return any(keyword.lower() in lowered for keyword in keywords)


def _dedupe(items: list[str], limit: int = 5) -> list[str]:
    seen: set[str] = set()
    output: list[str] = []
    for item in items:
        key = item.lower()
        if key in seen:
            continue
        seen.add(key)
        output.append(item)
        if len(output) >= limit:
            break
    return output


def build_brief(text: str) -> MaintainerBrief:
    """Build a deterministic maintainer brief from raw issue text."""
    sentences = split_sentences(text)
    if not sentences:
        return MaintainerBrief(
            summary="No source text was provided.",
            problem_statements=[],
            reproduction_steps=[],
            risks=[],
            action_items=["Ask the reporter to provide the issue details."],
        )

    problem_keywords = [
        "bug",
        "error",
        "fail",
        "failed",
        "failure",
        "broken",
        "crash",
        "unexpected",
        "does not work",
        "cannot",
        "できない",
        "失敗",
        "不具合",
        "エラー",
    ]
    reproduction_keywords = [
        "steps",
        "reproduce",
        "run",
        "command",
        "environment",
        "version",
        "再現",
        "手順",
        "環境",
    ]
    risk_keywords = [
        "security",
        "data loss",
        "regression",
        "breaking",
        "urgent",
        "production",
        "risk",
        "脆弱",
        "本番",
        "影響",
        "リスク",
    ]
    action_keywords = [
        "should",
        "need",
        "please",
        "request",
        "fix",
        "add",
        "update",
        "確認",
        "対応",
        "修正",
        "追加",
    ]

    problems = _dedupe([s for s in sentences if _contains_any(s, problem_keywords)])
    reproduction = _dedupe([s for s in sentences if _contains_any(s, reproduction_keywords)])
    risks = _dedupe([s for s in sentences if _contains_any(s, risk_keywords)])
    actions = _dedupe([s for s in sentences if _contains_any(s, action_keywords)])

    summary_source = problems[0] if problems else sentences[0]
    summary = summary_source[:220] + ("..." if len(summary_source) > 220 else "")

    if not actions:
        actions = [
            "Confirm the expected behavior.",
            "Ask for missing environment details if reproduction is unclear.",
            "Add or update a regression test before closing the issue.",
        ]

    return MaintainerBrief(
        summary=summary,
        problem_statements=problems,
        reproduction_steps=reproduction,
        risks=risks,
        action_items=actions,
    )


def render_markdown(brief: MaintainerBrief) -> str:
    """Render a maintainer brief as Markdown."""
    sections = [
        "# Maintainer Brief",
        "",
        "## Summary",
        brief.summary,
        "",
        "## Problem statements",
        *_render_list(brief.problem_statements),
        "",
        "## Reproduction signals",
        *_render_list(brief.reproduction_steps),
        "",
        "## Risk signals",
        *_render_list(brief.risks),
        "",
        "## Suggested next actions",
        *_render_list(brief.action_items),
    ]
    return "\n".join(sections).strip() + "\n"


def _render_list(items: list[str]) -> list[str]:
    if not items:
        return ["- None detected"]
    return [f"- {item}" for item in items]
