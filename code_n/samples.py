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
    if challenge_id.startswith("cc_"):
        return _codechef_sample_lines(challenge_id)

    doc_examples = _examples_from_markdown_doc(challenge_id)
    if doc_examples:
        return _format_example_blocks(doc_examples)

    examples = [
        (_format_sample_repr(sample.input_repr), _format_sample_repr(sample.output_repr))
        for sample in samples_for(challenge_id)
    ]
    return _format_example_blocks(examples)


def _codechef_sample_lines(challenge_id: str) -> list[str]:
    samples = samples_for(challenge_id)
    if not samples:
        return []

    lines: list[str] = []
    for index, sample in enumerate(samples, start=1):
        if index > 1:
            lines.append("")
        lines.append(f"Example {index} (official combined stdin/stdout):")
        lines.append("Input:")
        lines.extend(_indent_code_block(sample.input_repr))
        lines.append("Output:")
        lines.extend(_indent_code_block(sample.output_repr))

        separated = _split_codechef_sample_cases(sample.input_repr, sample.output_repr)
        if separated:
            lines.append("Separated test cases:")
            for case_index, (case_input, case_output) in enumerate(separated, start=1):
                lines.append(f"  Test case {case_index}:")
                lines.append("    Input:")
                lines.extend(_indent_code_block(case_input, indent="      "))
                lines.append("    Output:")
                lines.extend(_indent_code_block(case_output, indent="      "))
    return lines


def _indent_code_block(value: str, indent: str = "  ") -> list[str]:
    text = str(value or "").strip()
    if not text:
        return [f"{indent}<empty>"]
    return [f"{indent}{line.rstrip()}" for line in text.splitlines()]


def _split_codechef_sample_cases(input_text: str, output_text: str) -> list[tuple[str, str]]:
    input_lines = [line.rstrip() for line in input_text.strip().splitlines() if line.strip()]
    output_lines = [line.rstrip() for line in output_text.strip().splitlines() if line.strip()]
    if len(input_lines) < 3:
        return []
    try:
        test_count = int(input_lines[0].strip())
    except ValueError:
        return []
    if test_count <= 1:
        return []

    payload_lines = input_lines[1:]
    if len(payload_lines) % test_count != 0:
        return []
    block_size = len(payload_lines) // test_count
    if block_size <= 0 or len(output_lines) != test_count:
        return []

    cases: list[tuple[str, str]] = []
    for index in range(test_count):
        start = index * block_size
        case_input = "\n".join(payload_lines[start:start + block_size]).strip()
        case_output = output_lines[index].strip()
        if not case_input or not case_output:
            return []
        cases.append((case_input, case_output))
    return cases


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
