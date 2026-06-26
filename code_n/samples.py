"""Sample input/output for each challenge.

Sourced from the :class:`~challenges.spec.AlgorithmSpec` registered
for each challenge. The :func:`sample_lines` / :func:`sample_doc`
API stays the same so the templates and the Explore view don't
need to know where the data comes from.
"""

from __future__ import annotations

from pathlib import Path

from challenges.registry import get_challenge
from challenges.spec import Sample


_PARAM_ALIASES = {
    "subRoot": "sub_root",
}

PROJECT_ROOT = Path(__file__).resolve().parents[1]


def samples_for(challenge_id: str) -> list[Sample]:
    """Return the registered :class:`Sample` objects for this id.

    Falls back to ``[]`` for unknown ids so the templater can build
    a starter file with no Samples section rather than crashing.
    """
    challenge = get_challenge(challenge_id)
    if challenge is None:
        return []
    spec = getattr(challenge, "_spec", None)
    if spec is None:
        return []
    return list(spec.samples)


def _format_sample_repr(value: str) -> str:
    """Normalize compact sample strings for docs and starter templates."""
    for old, new in _PARAM_ALIASES.items():
        value = value.replace(old, new)

    chars: list[str] = []
    quote: str | None = None
    escape = False
    index = 0
    while index < len(value):
        char = value[index]

        if quote:
            chars.append(char)
            if escape:
                escape = False
            elif char == "\\":
                escape = True
            elif char == quote:
                quote = None
            index += 1
            continue

        if char in {'"', "'"}:
            quote = char
            chars.append(char)
        elif char == "=":
            while chars and chars[-1] == " ":
                chars.pop()
            chars.append(" = ")
            while index + 1 < len(value) and value[index + 1] == " ":
                index += 1
        elif char == ",":
            chars.append(",")
            while index + 1 < len(value) and value[index + 1] == " ":
                index += 1
            if index + 1 < len(value):
                chars.append(" ")
        else:
            chars.append(char)
        index += 1

    return "".join(chars)


def sample_lines(challenge_id: str) -> list[str]:
    """Format samples as plain ``Example N`` blocks.

    Returns an empty list when no samples are registered.
    """
    doc_examples = _examples_from_markdown_doc(challenge_id)
    if doc_examples:
        return _format_example_blocks(doc_examples)

    examples = [
        (_format_sample_repr(sample.input_repr), _format_sample_repr(sample.output_repr))
        for sample in samples_for(challenge_id)
    ]
    return _format_example_blocks(examples)


def _format_example_blocks(examples: list[tuple[str, str]]) -> list[str]:
    lines: list[str] = []
    for index, (input_repr, output_repr) in enumerate(examples, start=1):
        lines.append(f"Example {index}:")
        lines.append(f"Input:  {input_repr}")
        lines.append(f"Output: {output_repr}")
        if index < len(examples):
            lines.append("")
    return lines


def _examples_from_markdown_doc(challenge_id: str) -> list[tuple[str, str]]:
    if not challenge_id.startswith("nc_"):
        return []

    docs_root = PROJECT_ROOT / "docs" / "algorithms"
    matches = sorted(docs_root.glob(f"neetcode_*/{challenge_id}_*.md"))
    if not matches:
        return []

    text = matches[0].read_text(encoding="utf-8")
    examples: list[tuple[str, str]] = []
    pending_input: str | None = None
    in_examples = False

    for raw_line in text.splitlines():
        line = raw_line.strip()
        if line == "### Examples":
            in_examples = True
            continue
        if in_examples and line == "---":
            break
        if not in_examples:
            continue

        if line.startswith("- Input: `") and line.endswith("`"):
            pending_input = _format_sample_repr(line.removeprefix("- Input: `")[:-1])
        elif line.startswith("- Output: `") and line.endswith("`") and pending_input is not None:
            output = _format_sample_repr(line.removeprefix("- Output: `")[:-1])
            examples.append((pending_input, output))
            pending_input = None

    return examples


def sample_doc(challenge_id: str, indent: str = "") -> str:
    """Format the samples as a plain comment-ready block."""
    lines = sample_lines(challenge_id)
    if not lines:
        return ""
    return "\n".join(f"{indent}{line}" if line else "" for line in lines)
