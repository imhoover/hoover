from __future__ import annotations

import argparse
from pathlib import Path
import sys

from .parser import build_brief, render_markdown


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="hoover",
        description="Generate a concise maintainer brief from an issue report.",
    )
    parser.add_argument(
        "source",
        nargs="?",
        help="Path to a Markdown or plain-text issue report. Reads stdin when omitted.",
    )
    parser.add_argument(
        "--output",
        "-o",
        help="Optional output path for the generated Markdown brief.",
    )
    return parser.parse_args(argv)


def read_source(path: str | None) -> str:
    if path is None:
        return sys.stdin.read()

    source_path = Path(path)
    if not source_path.exists():
        raise FileNotFoundError(f"Source file not found: {source_path}")
    if not source_path.is_file():
        raise IsADirectoryError(f"Source path is not a file: {source_path}")
    return source_path.read_text(encoding="utf-8")


def write_output(markdown: str, output_path: str | None) -> None:
    if output_path is None:
        print(markdown, end="")
        return

    target = Path(output_path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(markdown, encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        source = read_source(args.source)
        brief = build_brief(source)
        markdown = render_markdown(brief)
        write_output(markdown, args.output)
    except Exception as exc:  # pragma: no cover - defensive CLI boundary
        print(f"hoover: {exc}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
