"""Challenge registry - maps challenge IDs to their implementations."""

from typing import Optional
from code_n.challenge import Challenge

from challenges.intro import IntroHelloGrid
from challenges.sorting import (
    BubbleSortChallenge,
    SelectionSortChallenge,
    InsertionSortChallenge,
    MergeSortChallenge,
    QuickSortChallenge,
)
from challenges.searching import (
    LinearSearchChallenge,
    BinarySearchChallenge,
    BFSGridChallenge,
    DFSGridChallenge,
)
from challenges.graphs import (
    GraphRepresentationChallenge,
    DijkstraChallenge,
)
from challenges.dynamic import (
    FibonacciChallenge,
    ClimbingStairsChallenge,
    KnapsackChallenge,
    LCSChallenge,
)


CHALLENGE_REGISTRY: dict[str, type[Challenge]] = {
    "intro_01": IntroHelloGrid,
    "sort_01": BubbleSortChallenge,
    "sort_02": SelectionSortChallenge,
    "sort_03": InsertionSortChallenge,
    "sort_04": MergeSortChallenge,
    "sort_05": QuickSortChallenge,
    "search_01": LinearSearchChallenge,
    "search_02": BinarySearchChallenge,
    "search_03": BFSGridChallenge,
    "search_04": DFSGridChallenge,
    "graph_01": GraphRepresentationChallenge,
    "graph_04": DijkstraChallenge,
    "dp_01": FibonacciChallenge,
    "dp_02": ClimbingStairsChallenge,
    "dp_03": KnapsackChallenge,
    "dp_04": LCSChallenge,
}


def get_challenge(challenge_id: str) -> Optional[Challenge]:
    """Instantiate a challenge by its ID."""
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls:
        return cls()
    return None


def list_challenges() -> list[str]:
    return list(CHALLENGE_REGISTRY.keys())
