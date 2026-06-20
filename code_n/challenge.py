"""Challenge definition and execution framework.

Each challenge defines:
- A grid setup (the visual problem)
- Input data generation
- A complexity threshold (max allowed O-class)
- A verification function (did the player solve it correctly?)

The engine has one execution path: :mod:`server.app.engine_runner`.
It loads the player's source, runs it under a tracer, and
applies the AST-based op counter to produce the verdict. The
runtime counter machinery (``TrackedList``, ``OperationCounter``,
``Challenge.run()``) was removed in v0.8.5.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Any, Optional

from .grid import Grid
from .counter import ComplexityClass


@dataclass
class ChallengeInfo:
    id: str
    name: str
    description: str
    category: str
    difficulty: int  # 1-10
    required_complexity: ComplexityClass
    hint: str = ""


class Challenge(ABC):
    """Base class for all challenges."""

    # Default maximum input size. The runner clamps --n to this and the
    # engine sizes the visualizer around it. 1D challenges use this;
    # 2D challenges (BFS/DFS grids) override to MAX_2D_N below because
    # a 50x50 grid is too dense to be useful even at the smallest zoom.
    MAX_N = 50
    MAX_2D_N = 35

    def __init__(self):
        self.grid: Optional[Grid] = None
        self._n: int = 0
        self._seed: Optional[int] = None

    @property
    def max_n(self) -> int:
        """Maximum n this challenge accepts.

        Routes (the server layer) call this before invoking
        :meth:`setup` so a player can't pass ``--n=100`` on a
        35-cap 2D challenge.
        """
        return self.MAX_N

    @property
    def info(self) -> ChallengeInfo:
        """Per-class metadata. Subclasses set :attr:`_info` in ``__init__``."""
        return self._info  # type: ignore[return-value]

    @abstractmethod
    def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
        """Set up the challenge and return the data the player will work with.

        Returns a dict of named arguments that will be passed to the
        player's ``solve`` function. The data the player receives is
        the same reference the engine keeps (so the verifier can
        observe in-place mutations via ``challenge._data``), and
        the values are plain Python lists / dicts / sets / grids —
        not Tracked* wrappers (those were removed in v0.8.5).
        """
        ...

    @abstractmethod
    def verify(self, result: Any) -> bool:
        """Verify the player's solution is correct.

        ``result`` is whatever the player's ``solve`` returned. The
        in-place mutation contract is preserved without the
        ``TrackedList`` indirection: the setup function passes the
        raw list reference, so the verifier can read the player's
        mutations via ``self._data`` (or whatever the canonical
        storage attribute is) when ``result is None``.
        """
        ...
