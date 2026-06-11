"""Challenge registry - maps challenge IDs to their implementations.

Built once at import time from the :data:`SPECS` lists exported by
each module in :mod:`challenges.algorithms`. Adding a new challenge
is one entry in one of those modules - no edit to this file needed.
"""

from typing import Optional

from code_n.challenge import Challenge
from .spec import AlgorithmSpec, make_challenge


def _collect_specs() -> list[AlgorithmSpec]:
    """Import every per-category module and concatenate its SPECS.

    Done at import time so the registry is fixed for the life of
    the process - the player can rely on ``list_challenges()`` being
    stable.
    """
    from challenges.algorithms import intro, sorting, searching, graphs, dynamic, greedy, strings, trees
    return [
        *intro.SPECS,
        *sorting.SPECS,
        *searching.SPECS,
        *graphs.SPECS,
        *dynamic.SPECS,
        *greedy.SPECS,
        *strings.SPECS,
        *trees.SPECS,
    ]


# Pre-build the registry. Each spec becomes a Challenge subclass.
CHALLENGE_REGISTRY: dict[str, type[Challenge]] = {
    spec.id: make_challenge(spec) for spec in _collect_specs()
}


def get_challenge(challenge_id: str) -> Optional[Challenge]:
    """Instantiate a challenge by its ID."""
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls:
        return cls()
    return None


def list_challenges() -> list[str]:
    return list(CHALLENGE_REGISTRY.keys())
