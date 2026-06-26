"""Utilities for the player's saved solution scripts."""

from __future__ import annotations

import os
import re
import sys
from dataclasses import dataclass
from typing import Optional

from .samples import sample_doc


def _app_root() -> str:
    if getattr(sys, "frozen", False):
        return os.path.dirname(os.path.abspath(sys.executable))
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


PROJECT_ROOT = _app_root()
SOLUTIONS_DIR = os.path.join(PROJECT_ROOT, "solutions")


@dataclass(frozen=True)
class SolutionPath:
    challenge_id: str
    path: str
    exists: bool


def ensure_solutions_dir() -> str:
    os.makedirs(SOLUTIONS_DIR, exist_ok=True)
    return SOLUTIONS_DIR


def default_solution_path(challenge_id: str) -> str:
    return os.path.join(ensure_solutions_dir(), f"{challenge_id}.py")


def resolve_solution_path(challenge_id: str, explicit_path: Optional[str] = None) -> SolutionPath:
    path = explicit_path or default_solution_path(challenge_id)
    return SolutionPath(challenge_id=challenge_id, path=path, exists=os.path.exists(path))


def solution_hint(challenge_id: str) -> str:
    path = default_solution_path(challenge_id)
    rel_path = os.path.relpath(path, PROJECT_ROOT)
    return (
        f"Create your solution at {rel_path}. "
        f"Then run: python run_challenge.py {challenge_id}"
    )


def _build_templates() -> dict[str, dict]:
    """Build the per-challenge template metadata from the registry.

    Each registered :class:`~challenges.spec.AlgorithmSpec` exposes
    ``params``, ``inputs``, and ``returns``; the template generator
    in :func:`_solution_template` consumes those three keys.
    """
    from challenges.registry import get_challenge

    templates: dict[str, dict] = {}
    for challenge_id, _cls in _iter_registered_ids():
        challenge = get_challenge(challenge_id)
        if challenge is None:
            continue
        spec = getattr(challenge, "_spec", None)
        if spec is None:
            continue
        templates[spec.id] = {
            "params": list(spec.params),
            "inputs": dict(spec.inputs),
            "returns": spec.returns,
        }
    return templates


def _iter_registered_ids():
    """Yield ``(id, class)`` pairs in registry-insertion order."""
    from challenges.registry import CHALLENGE_REGISTRY
    for cid, cls in CHALLENGE_REGISTRY.items():
        yield cid, cls


# Backwards-compatible public name. The same dict used to be
# hand-maintained; it's now derived from the spec at import time
# so every new entry in a ``challenges/algorithms/<cat>.py`` file
# shows up here automatically.
_CHALLENGE_TEMPLATES: dict[str, dict] = _build_templates()


def _clean_template_description(description: str) -> str:
    """Remove embedded markdown sections from imported challenge text."""
    text = re.sub(
        r"\n+##\s+GeeksforGeeks Reference\s*\n[\s\S]*?(?=\n+##\s+|$)",
        "",
        description,
        flags=re.IGNORECASE,
    )
    text = re.sub(
        r"\n+##\s+Example\s*\n[\s\S]*?(?=\n+##\s+|$)",
        "",
        text,
        flags=re.IGNORECASE,
    )
    text = re.sub(r"```[\s\S]*?```", "", text)
    text = re.sub(r"^#{1,6}\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("`", "").replace("**", "")
    return text.strip()


def _section_block(title: str, body: str) -> str:
    lines = [title, "-" * len(title)]
    if body:
        lines.extend(body.splitlines())
    return "\n".join(lines)


def _solution_header(challenge_id: str, description: str) -> str:
    clean_description = _clean_template_description(description)
    samples = sample_doc(challenge_id)
    blocks = [_section_block("Description", clean_description)]
    if samples:
        blocks.append(_section_block("Examples", samples))
    body = "\n\n".join(blocks).rstrip()
    return f'"""\n{body}\n"""\n\n'


def _solution_template(challenge_id: str, heading: str, description: str) -> str:
    """Build a starter file for the player.

    Every challenge now has a template with EXPLICIT parameter
    names (no more ``def solve(**kwargs):``). The data comes from
    the registered ``AlgorithmSpec`` while the docstring contains
    only the challenge description and examples.
    """
    header = _solution_header(challenge_id, description)

    info = _CHALLENGE_TEMPLATES.get(challenge_id)
    if info is None:
        # Unknown challenge - fall back to a generic stub. Shouldn't
        # happen in practice; registry.py enumerates the supported
        # IDs.
        return (
            header +
            'def solve():\n'
            '    # Write your code here.\n'
            '    return None\n'
        )

    params = info["params"]
    sig = "def solve(" + ", ".join(params) + "):"

    return (
        header +
        f'{sig}\n'
        f'    # Write your code here.\n'
        f'    return None\n'
    )


def create_solution_file(challenge_id: str, title: str = "", description: str = "") -> str:
    """Create the saved solution script for a challenge if it does not exist."""
    path = default_solution_path(challenge_id)
    if os.path.exists(path):
        return path

    heading = f"{challenge_id}: {title}" if title else challenge_id
    content = _solution_template(challenge_id, heading, description)
    with open(path, "w", encoding="utf-8") as file:
        file.write(content)
    return path
