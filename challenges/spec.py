"""Algorithm spec framework - the single source of truth for one algorithm.

Each algorithm in cOde(n) is described by an :class:`AlgorithmSpec`
dataclass that captures everything the runtime needs: its identity
(id, name, category), its metadata (difficulty, required complexity,
description, GFG source URL), its contract with the player's
``solve()`` function (parameter names, per-parameter docs, return
description), its test scaffolding (setup + verify), the canonical
optimal solution (as Python source), and a few sample I/O pairs.

The :func:`make_challenge` factory turns a spec into a regular
``Challenge`` subclass that plugs into the existing runner. Specs
live in :mod:`challenges.algorithms.<category>` modules; the
registry in :mod:`challenges.registry` collects them.

Why a dataclass + factory rather than per-challenge classes?
------------------------------------------------------------
The old design had 16 hand-written classes plus three parallel
hand-written metadata tables (``_CHALLENGE_TEMPLATES``,
``_arg_hints_for``/``_return_hint_for``/``_example_solution_lines``,
``SAMPLES``). Scaling to GFG's full ~250-algorithm catalog meant
keeping 4-5 files in sync per new entry. With the spec framework,
adding a new algorithm is a single entry in a single file, and
templates, hints, samples, and the tree are auto-derived.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from code_n.challenge import Challenge, ChallengeInfo
from code_n.counter import ComplexityClass


# Setup takes the challenge instance (so it can stash state for
# verify), the engine-provided size, and the optional seed, and
# returns a dict of {param_name: value} that becomes the player's
# solve() kwargs. Same shape as the original Challenge.setup contract.
SetupFn = Callable[[Challenge, int, Optional[int]], dict[str, Any]]

# Verify takes the challenge instance and the player's result, and
# returns True if the answer is correct. The instance is the same
# one that ran setup, so verify can read anything setup stashed.
VerifyFn = Callable[[Challenge, Any], bool]


@dataclass(frozen=True)
class Sample:
    """One input/output example shown in the Explore view and the
    starter-file docstring.

    The strings are already formatted for display (``"data = [4, 9, 2]"``)
    so we don't try to pretty-print Python values at render time -
    it's much easier to get right when the human writes the sample
    than to recover the original list from the setup_fn.
    """

    input_repr: str
    output_repr: str


@dataclass
class AlgorithmSpec:
    """Everything cOde(n) needs to know about one algorithm.

    Required fields are everything the runtime, the templates, the
    hints, and the samples panel need. Optional fields cover
    advanced things: a per-algorithm ``hint`` shown on a failed
    run, a custom ``max_n`` for 2D challenges, the
    ``parents``/``children`` edges for the navigator's learning
    path, and the ``complexity_notes`` (best/average/worst case
    analysis strings) shown in the scientific complexity panel.
    """

    id: str
    name: str
    category: str
    difficulty: int
    required_complexity: ComplexityClass
    description: str
    source_url: str
    params: list[str]
    inputs: dict[str, str]
    returns: str
    source: str
    setup_fn: SetupFn
    verify_fn: VerifyFn

    samples: list[Sample] = field(default_factory=list)
    hint: str = ""
    max_n: Optional[int] = None
    parents: list[str] = field(default_factory=list)
    children: list[str] = field(default_factory=list)
    # Per-algorithm complexity analysis for the scientific panel.
    # Keys are the labels shown to the user (e.g. "best", "average",
    # "worst", "space"); values are short strings describing the
    # behavior. Empty dict → hide the panel for that algorithm.
    complexity_notes: dict[str, str] = field(default_factory=dict)


def make_challenge(spec: AlgorithmSpec) -> type[Challenge]:
    """Build a :class:`Challenge` subclass from an :class:`AlgorithmSpec`.

    The returned class:
    * implements ``info``/``setup``/``verify`` by delegating to the spec
    * has ``__name__ = f"SpecChallenge_{spec.id}"`` so log messages
      and debugger output are still readable
    * stores the spec on the instance as ``self._spec`` so
      downstream consumers (templates, hints, the Solve button)
      can read it without re-deriving anything
    * pre-executes ``spec.source`` once at class-creation time and
      stores the resulting ``solve`` as ``self._reference_solve``,
      so the optimal-solution copy step never has to re-parse the
      source
    """
    # Pre-execute the source in a per-spec namespace. Doing this
    # once (at factory time) instead of per instance is fine: the
    # source is a top-level function definition with no mutable
    # shared state.
    namespace: dict[str, Any] = {"__name__": f"spec.{spec.id}"}
    exec(spec.source, namespace)  # noqa: S102 - intentional dynamic load
    reference_solve = namespace.get("solve", lambda **_: None)

    info_required_complexity = spec.required_complexity

    class _SpecChallenge(Challenge):
        def __init__(self):
            super().__init__()
            self._spec = spec
            self._reference_solve = reference_solve

        @property
        def info(self) -> ChallengeInfo:
            return ChallengeInfo(
                id=spec.id,
                name=spec.name,
                description=spec.description,
                category=spec.category,
                difficulty=spec.difficulty,
                required_complexity=info_required_complexity,
                hint=spec.hint,
            )

        @property
        def max_n(self) -> int:
            # If the spec pins a custom max (e.g. 35 for 2D grids),
            # use it; otherwise fall back to the class default.
            if spec.max_n is not None:
                return spec.max_n
            return super().max_n

        def setup(self, n: int, seed: Optional[int] = None) -> dict[str, Any]:
            return spec.setup_fn(self, n, seed)

        def verify(self, result: Any) -> bool:
            return spec.verify_fn(self, result)

    _SpecChallenge.__name__ = f"SpecChallenge_{spec.id}"
    _SpecChallenge.__qualname__ = _SpecChallenge.__name__
    return _SpecChallenge
