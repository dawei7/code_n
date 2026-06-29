"""Pydantic schemas for the cOde(n) HTTP API.

All request and response bodies are defined here so the route modules
stay focused on wiring. Pydantic v2 syntax (``BaseModel`` + type
hints); ``model_dump`` produces the JSON-serialisable dict.

Naming convention: outbound models end in ``Out`` (or are themselves
``*Response`` / ``*Summary`` / ``*Detail``); inbound models are
``*Request`` / ``*Update`` / ``*Put``.
"""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field


# ----------------------------------------------------------------------------
# Challenges
# ----------------------------------------------------------------------------


class ParamDoc(BaseModel):
    """One named parameter of the player's ``solve()`` function."""

    name: str
    doc: str
    type_hint: str


class Sample(BaseModel):
    """One input/output example shown in the Explore view."""

    input_repr: str
    output_repr: str


class ChallengeSummary(BaseModel):
    """Card data for the challenge list in the left rail."""

    id: str
    name: str
    category: str
    categories: list[str] = Field(default_factory=list)
    difficulty: int
    difficulty_label: str = ""
    acceptance_rate: float | None = None
    required_complexity: str
    description: str
    hint: str = ""
    source_url: str = ""
    parents: list[str] = Field(default_factory=list)
    children: list[str] = Field(default_factory=list)
    max_n: int
    unlocked: bool = True
    leetcode_title: str = ""
    leetcode_slug: str = ""
    leetcode_url: str = ""


class ChallengeDetail(ChallengeSummary):
    """Full data for the challenge view, including the starter code.

    The player writes their solution in ``solutions/<id>.py`` through
    the in-app editor. Direct file edits also work because the server
    re-reads the file-backed source model when needed.
    """

    params: list[ParamDoc]
    samples: list[Sample]
    starter_source: str
    optimal_source: str
    # Per-algorithm complexity notes (best/average/worst/space/
    # stable/in_place) for the scientific complexity panel.
    # Empty dict → hide the panel for this algorithm.
    complexity_notes: dict[str, str] = {}  # The Solve button writes this verbatim.


# ----------------------------------------------------------------------------
# Run
# ----------------------------------------------------------------------------


class RunRequest(BaseModel):
    """Body for ``POST /api/challenges/{id}/run``.

    The player edits in the cOde(n) tab; the route receives the current
    source, exec's it, and runs it against the engine.

    ``mode`` controls how ``n`` and ``seed`` are interpreted:
      - ``"practice"`` (default): use the player-supplied ``n`` /
        ``seed`` exactly. This is the standard "I want to test my
        code" flow.
      - ``"real_test"``: the server ignores the player's ``n`` /
        ``seed`` and picks a deterministic-feeling but fresh ``n``
        and a random ``seed`` for a fair, surprise test. ``n`` is
        ``min(64, challenge.max_n)`` (so the algorithm has real
        work to do) and ``seed`` is a random 31-bit integer. The
        client UI shows the actual ``n``/``seed`` used in the
        response.
    """

    source: str = Field(
        ...,
        description=(
            "Full Python source. Most challenges define `solve(...)`; "
            "CodeChef challenges may use normal stdin/stdout with input() and print()."
        ),
    )
    n: int = Field(16, ge=2, le=100)
    seed: Optional[int] = None
    mode: Literal["practice", "real_test"] = "practice"


class ScalingPoint(BaseModel):
    n: int
    user_ops: int
    ref_ops: int
    ci_low: int
    ci_high: int


class RunResponse(BaseModel):
    """The result of a single run.

    The verdict (``passed``, ``correct``, ``within_threshold``,
    ``actual_complexity``, ``message``) is derived from the
    AST-based op counter. The four complexity numbers
    (``user_ast_ops``, ``reference_ast_ops``, ``reference_ci_low``,
    ``reference_ci_high``) drive the Complexity tab and the
    ±5% tolerance band comparison.

    ``return_value_repr`` is a short string representation of what
    ``solve()`` returned (capped at a few hundred chars so a
    10,000-element list doesn't blow up the response).

    The runtime op counter and per-step trace are not serialized into
    this REST response. The in-app debugger streams through DAP, while
    the engine still runs the player's source under a tracer for the
    step-limit guard that catches infinite loops.
    """

    passed: bool
    correct: bool
    within_threshold: bool
    actual_complexity: str
    required_complexity: str
    n: int
    seed: Optional[int] = None  # Echoed from the request (or the
                                # server-picked value in real_test mode)
    mode: str = "practice"      # Echoed: "practice" or "real_test"
    too_efficient: bool = False # True if the run was flagged as
                                # too efficient (AST scan or op
                                # count ratio vs reference)
    too_efficient_reason: str = ""
    message: str
    return_value_repr: str
    reference_return_value_repr: Optional[str] = None
    setup_data_repr: Optional[dict[str, str]] = None
    # ---- AST-based op count (the "scientific" metric) -------------
    # Counted by walking the source's AST and summing each
    # operation (Compare, BinOp, Call, Subscript, Attribute,
    # etc.), with loop bodies multiplied by their iteration
    # count. Deterministic — same source, same n, same result.
    # See server/app/ast_ops.py for the full algorithm.
    #
    # This is the SINGLE source of truth for "how many ops
    # does your code do?" — used by the Complexity tab, the
    # verdict (within_threshold), and the progress-best-ops
    # recording.
    user_ast_ops: Optional[int] = None       # User's source, n
    reference_ast_ops: Optional[int] = None  # Reference, same n
    # ±5% tolerance band around the reference's AST op
    # count. The user's AST count should land within this
    # band to be considered "as efficient as the reference".
    # Below the band: likely a cheat. Above the band:
    # correct but slower than optimal.
    reference_ci_low: Optional[int] = None
    reference_ci_high: Optional[int] = None
    reference_coefficient: Optional[float] = None
    scaling_data: list[ScalingPoint] = Field(default_factory=list)


# ----------------------------------------------------------------------------
# Progress
# ----------------------------------------------------------------------------


class LevelRecordOut(BaseModel):
    challenge_id: str
    best_ops: int
    complexity_achieved: str
    attempts: int


class ProgressOut(BaseModel):
    player_name: str
    completed: list[str]
    last_status: dict[str, str]
    records: dict[str, LevelRecordOut]
    career_mode: bool = False
    leetcode_username: str = ""
    leetcode_solved: list[str] = Field(default_factory=list)
    unlocked_leetcode: list[str] = Field(default_factory=list)
    milestones: list[str] = Field(default_factory=list)
    gemini_api_key: str = ""
    active_set: str = "neetcode"
    sidebar_width: int = 256
    sidebar_position: str = "left"
    sidebar_collapsed: bool = False


class ProgressUpdate(BaseModel):
    """Body for ``PUT /api/progress``.

    Exactly one of ``mark`` / ``fail`` / ``reset`` should be set.
    ``player_name`` is a write-through for the player's display name.
    """

    player_name: Optional[str] = None
    mark: Optional[dict] = None  # {"challenge_id": str, "ops": int, "complexity": str}
    fail: Optional[str] = None  # challenge_id
    reset: bool = False
    career_mode: Optional[bool] = None
    leetcode_username: Optional[str] = None
    gemini_api_key: Optional[str] = None
    sidebar_width: Optional[int] = None
    sidebar_position: Optional[str] = None
    sidebar_collapsed: Optional[bool] = None
    active_set: Optional[str] = None


# ----------------------------------------------------------------------------
# Solutions
# ----------------------------------------------------------------------------


class SolutionGet(BaseModel):
    challenge_id: str
    source: str
    exists: bool


class SolutionPut(BaseModel):
    source: str


class SolutionVersionsGet(BaseModel):
    challenge_id: str
    active_version: int
    versions: list[int]
    version_names: dict[int, str]
    modified_versions: list[int] = Field(default_factory=list)
    source: str


class VersionSwitchRequest(BaseModel):
    version: int

class VersionRenameRequest(BaseModel):
    name: str


# ----------------------------------------------------------------------------
# Profiles & Verification
# ----------------------------------------------------------------------------

class ProfileSummary(BaseModel):
    name: str
    career_mode: bool
    leetcode_username: str
    completed_count: int
    verified_leetcode_count: int

class ProfilesResponse(BaseModel):
    active_profile: str
    profiles: list[ProfileSummary]

class CreateProfileRequest(BaseModel):
    name: str
    career_mode: bool = False
    leetcode_username: str = ""

class VerifyLeetCodeRequest(BaseModel):
    challenge_id: str

class VerifyLeetCodeResponse(BaseModel):
    success: bool
    message: str
    unlocked_leetcode: list[str]
    milestones: list[str]


class AnalyzeRequest(BaseModel):
    source: str
    n: int
    seed: Optional[int] = None
    returned: str
    expected: str
    inputs: dict[str, str] = Field(default_factory=dict)


class AnalyzeResponse(BaseModel):
    analysis: str
