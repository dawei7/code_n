"""Sample input/output for each challenge.

Sourced from the :class:`~challenges.spec.AlgorithmSpec` registered
for each challenge. The :func:`sample_lines` / :func:`sample_doc`
API stays the same so the templates and the Explore view don't
need to know where the data comes from.
"""

from __future__ import annotations

from challenges.registry import get_challenge
from challenges.spec import Sample


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


def sample_lines(challenge_id: str) -> list[str]:
    """Format the samples as ``Sample N input: ... / Sample N output: ...`` lines.

    Returns an empty list when no samples are registered.
    """
    lines: list[str] = []
    for index, sample in enumerate(samples_for(challenge_id), start=1):
        lines.append(f"Sample {index} input:  {sample.input_repr}")
        lines.append(f"Sample {index} output: {sample.output_repr}")
        if index < 3:
            lines.append("")
    return lines


def sample_doc(challenge_id: str, indent: str = "") -> str:
    """Format the samples as a docstring-ready block."""
    lines = sample_lines(challenge_id)
    if not lines:
        return ""
    return "Samples:\n" + "\n".join(f"{indent}{line}" if line else "" for line in lines) + "\n\n"
