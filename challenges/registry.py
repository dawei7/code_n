"""Challenge registry backed by canonical LeetCode packages."""

import logging
import threading
import time
from collections.abc import Iterator, Mapping
from typing import Optional

from engine.challenge import Challenge
from .spec import AlgorithmSpec, make_challenge


def _collect_specs() -> list[AlgorithmSpec]:
    """Load the canonical LeetCode corpus."""
    from challenges.algorithms import leetcode
    return [*leetcode.SPECS]



class LazyChallengeRegistry(Mapping[str, type[Challenge]]):
    """Build challenge classes on first use.

    The desktop application deliberately warms this registry during startup so
    all subset views are ready before its window appears. Keeping the mapping
    lazy still avoids loading the full corpus for unrelated command-line tools.
    """

    def __init__(self) -> None:
        self._data: dict[str, type[Challenge]] | None = None
        self._lock = threading.Lock()

    @property
    def is_loaded(self) -> bool:
        return self._data is not None

    def load(self) -> dict[str, type[Challenge]]:
        if self._data is None:
            with self._lock:
                if self._data is None:
                    started = time.perf_counter()
                    self._data = {spec.id: make_challenge(spec) for spec in _collect_specs()}
                    logging.getLogger(__name__).info(
                        "Loaded %d challenges in %.3fs",
                        len(self._data),
                        time.perf_counter() - started,
                    )
        return self._data

    def __getitem__(self, challenge_id: str) -> type[Challenge]:
        return self.load()[challenge_id]

    def __iter__(self) -> Iterator[str]:
        return iter(self.load())

    def __len__(self) -> int:
        return len(self.load())


CHALLENGE_REGISTRY: LazyChallengeRegistry = LazyChallengeRegistry()


def get_challenge(challenge_id: str) -> Optional[Challenge]:
    """Instantiate a challenge by its ID."""
    cls = CHALLENGE_REGISTRY.get(challenge_id)
    if cls:
        return cls()
    return None


def list_challenges() -> list[str]:
    return list(CHALLENGE_REGISTRY.keys())
