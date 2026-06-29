"""Resolve optional reference implementations by dataset-aware paths."""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from challenges.spec import AlgorithmSpec
from server.app.config import DOCS_ROOT, OPTIMAL_SOLUTIONS_ROOT


DATASET_PREFIXES = (
    ("cc_", "codechef"),
    ("nc_", "neetcode"),
    ("lc_", "leetcode"),
    ("leetcode_", "leetcode"),
)
EMBEDDED_SOURCE_DATASETS = {"geeksforgeeks"}


def dataset_for_challenge(challenge_id: str) -> str:
    for prefix, dataset in DATASET_PREFIXES:
        if challenge_id.startswith(prefix):
            return dataset
    return "geeksforgeeks"


def _doc_candidates(dataset: str, challenge_id: str) -> list[Path]:
    dataset_root = DOCS_ROOT / "algorithms" / dataset
    if not dataset_root.exists():
        return []
    candidates = []
    for path in dataset_root.rglob("*.md"):
        if path.stem.endswith("_de"):
            continue
        if path.stem == challenge_id or path.stem.startswith(f"{challenge_id}_"):
            candidates.append(path)
    return sorted(candidates)


@lru_cache(maxsize=2048)
def organized_solution_path(challenge_id: str) -> Path | None:
    """Return the preferred organized optimal-solution path for a challenge."""
    dataset = dataset_for_challenge(challenge_id)
    docs = _doc_candidates(dataset, challenge_id)
    if not docs:
        return None
    relative_doc = docs[0].relative_to(DOCS_ROOT / "algorithms")
    return (OPTIMAL_SOLUTIONS_ROOT / relative_doc).with_suffix(".py")


def _legacy_solution_path(challenge_id: str) -> Path:
    return OPTIMAL_SOLUTIONS_ROOT / f"{challenge_id}.py"


def load_optimal_source(challenge_id: str, spec: AlgorithmSpec) -> str:
    """Load the best available reference source for a challenge.

    Organized files are preferred for every dataset. For legacy local
    GeeksforGeeks-style challenges, fall back to ``spec.source`` so old
    challenge registrations continue to work even before a file exists.
    """
    # CodeChef reference programs are an internal complexity baseline only.
    # They must never be exposed through ChallengeDetail/"optimal source".
    if challenge_id.startswith("cc_"):
        return ""

    organized_path = organized_solution_path(challenge_id)
    if organized_path is not None and organized_path.exists():
        return organized_path.read_text(encoding="utf-8")

    legacy_path = _legacy_solution_path(challenge_id)
    if legacy_path.exists():
        return legacy_path.read_text(encoding="utf-8")

    if dataset_for_challenge(challenge_id) in EMBEDDED_SOURCE_DATASETS:
        return spec.source or ""
    return ""
