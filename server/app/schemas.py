"""Pydantic schemas for the cOde(n) HTTP API.

All request and response bodies are defined here so the route modules
stay focused on wiring. Pydantic v2 syntax (``BaseModel`` + type
hints); ``model_dump`` produces the JSON-serialisable dict.

Naming convention: outbound models end in ``Out`` (or are themselves
``*Response`` / ``*Summary`` / ``*Detail``); inbound models are
``*Request`` / ``*Update`` / ``*Put``.
"""
from __future__ import annotations

from typing import Any, Literal, Optional

from pydantic import BaseModel, Field

from engine.languages import SupportedLanguage


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


class TestCaseSummary(BaseModel):
    """Visible validated case metadata shown in the practice UI."""

    id: str
    name: str
    kind: str
    visible: bool = True
    input_repr: str
    expected_repr: str = ""
    tags: list[str] = Field(default_factory=list)


class ChallengeSummary(BaseModel):
    """Card data for the challenge list in the left rail."""

    id: str
    name: str
    category: str
    categories: list[str] = Field(default_factory=list)
    difficulty_label: str = ""
    elo_rating: float | None = None
    estimated_elo_rating: float | None = None
    frequency: float | None = None
    difficulty_estimate: int | None = None
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
    leetcode_category: str = ""
    leetcode_category_title: str = ""
    leetcode_frontend_id: str = ""
    leetcode_topics: list[dict[str, Any]] = Field(default_factory=list)
    leetcode_subsets: list[str] = Field(default_factory=list)
    leetcode_tags: list[str] = Field(default_factory=list)
    leetcode_company_tags: list[dict[str, Any]] = Field(default_factory=list)
    leetcode_study_plans: list[dict[str, Any]] = Field(default_factory=list)
    leetcode_external_subsets: list[dict[str, Any]] = Field(default_factory=list)
    supported_languages: list[str] = Field(default_factory=list)
    primary_language: str = "python"
    runnable_in_coden: bool = True
    has_guided_example: bool = False
    leetcode_submission_status: str = "missing"
    leetcode_submission_language: str = ""
    leetcode_submission_paid_only: bool = False


class ChallengeDetail(ChallengeSummary):
    """Full data for the challenge view, including the starter code.

    Personal solutions live in a writable per-user overlay, grouped by the
    canonical LeetCode problem package and stored only as v1, v2, or v3.
    """

    params: list[ParamDoc]
    samples: list[Sample]
    test_cases: list[TestCaseSummary] = Field(default_factory=list)
    starter_source: str
    starter_sources: dict[SupportedLanguage, str] = Field(default_factory=dict)
    optimal_source: str
    optimal_sources: dict[SupportedLanguage, str] = Field(default_factory=dict)
    # Per-algorithm complexity notes (best/average/worst/space/
    # stable/in_place) for the scientific complexity panel.
    # Empty dict â†’ hide the panel for this algorithm.
    complexity_notes: dict[str, str] = {}  # The Solve button writes this verbatim.


# ----------------------------------------------------------------------------
# Run
# ----------------------------------------------------------------------------


class CustomRunCase(BaseModel):
    """One user-authored local case supplied by the editor."""

    id: str
    name: str = "Custom case"
    input: dict[str, Any]


class RunRequest(BaseModel):
    """Body for ``POST /api/challenges/{id}/run``.

    The player edits in the cOde(n) tab; the route receives the current
    source, exec's it, and runs it against the engine.

    ``mode`` controls which authored validated cases are selected:
      - ``"practice"`` (default): run the selected visible case IDs, or
        the first visible case when no explicit selection was provided.
      - ``"real_test"``: run every visible system case, every supplied custom
        case, every hidden real-test case, and the benchmark cases. Benchmark
        results are hidden from the client except for pass/fail. Custom
        failures are diagnostic and do not affect the official verdict.

    The HTTP judge uses authored validated cases only.
    """

    source: str = Field(
        ...,
        description=(
            "Full source for the selected language. Python is executable for all "
            "challenge shapes; C++, Java, C#, JavaScript, Go, and Kotlin use "
            "function-call harnesses where supported."
        ),
    )
    language: SupportedLanguage = "python"
    mode: Literal["practice", "real_test"] = "practice"
    case_ids: list[str] = Field(default_factory=list)
    custom_input: Optional[dict[str, Any]] = None
    custom_cases: list[CustomRunCase] = Field(default_factory=list)


class ScalingPoint(BaseModel):
    n: int
    user_ops: int
    ref_ops: int
    ci_low: int
    ci_high: int


class RuntimeScalingPoint(BaseModel):
    size: int
    user_ms: float
    reference_ms: float
    ratio: float


class RunCaseResult(BaseModel):
    id: str
    name: str
    kind: str
    correct: bool
    passed: bool
    message: str = ""
    input_repr: str
    return_value_repr: str
    expected_repr: Optional[str] = None
    runtime_user_ms: Optional[float] = None
    hidden: bool = False
    counts_toward_verdict: bool = True


class RunResponse(BaseModel):
    """The result of a single run.

    The verdict (``passed``, ``correct``, ``within_threshold``,
    ``actual_complexity``, ``message``) is derived from correctness plus
    either the calibrated runtime check against the optimal reference or a
    verified non-scaling complexity certificate. Legacy fields
    (``user_ast_ops``, ``reference_ast_ops``, ``reference_ci_low``,
    ``reference_ci_high``) remain nullable for older clients and no longer drive the
    pass/fail verdict.

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
    mode: str = "practice"      # Echoed: "practice" or "real_test"
    too_efficient: bool = False # Legacy flag; new verdicts use correctness
                                # plus explicit complexity verification.
    too_efficient_reason: str = ""
    message: str
    return_value_repr: str
    reference_return_value_repr: Optional[str] = None
    setup_data_repr: Optional[dict[str, str]] = None
    # ---- Legacy static-op fields ----------------------------------
    # Kept nullable for wire compatibility with older UI state and progress
    # records. New verdicts do not compute or trust these.
    user_ast_ops: Optional[int] = None
    reference_ast_ops: Optional[int] = None
    reference_ci_low: Optional[int] = None
    reference_ci_high: Optional[int] = None
    reference_coefficient: Optional[float] = None
    scaling_data: list[ScalingPoint] = Field(default_factory=list)
    runtime_check: bool = False
    runtime_passed: Optional[bool] = None
    runtime_user_ms: Optional[float] = None
    runtime_reference_ms: Optional[float] = None
    runtime_ratio: Optional[float] = None
    runtime_limit_ms: Optional[float] = None
    runtime_trials: int = 0
    runtime_message: str = ""
    benchmark_correct: bool = True
    runtime_scaling_data: list[RuntimeScalingPoint] = Field(default_factory=list)
    complexity_check: bool = False
    complexity_passed: Optional[bool] = None
    complexity_method: str = ""
    complexity_message: str = ""
    case_results: list[RunCaseResult] = Field(default_factory=list)
    selected_case_ids: list[str] = Field(default_factory=list)


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
    leetcode_submissions: dict[str, dict] = Field(default_factory=dict)
    unlocked_leetcode: list[str] = Field(default_factory=list)
    milestones: list[str] = Field(default_factory=list)
    gemini_api_key: str = ""
    active_set: str = "leetcode"
    sidebar_width: int = 256
    sidebar_position: str = "left"
    sidebar_collapsed: bool = False
    pane_font_scales: dict[str, float] = Field(default_factory=dict)
    pane_sizes: dict[str, float] = Field(default_factory=dict)
    accent_colors: dict[str, str] = Field(default_factory=dict)


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
    pane_font_scales: Optional[dict[str, float]] = None
    pane_sizes: Optional[dict[str, float]] = None
    accent_colors: Optional[dict[str, str]] = None
    active_set: Optional[str] = None


class ProgressResetRequest(BaseModel):
    """A deliberately confirmed reset for one or more challenge ids."""

    scope: Literal["all", "coden", "leetcode"]
    challenge_ids: list[str] = Field(min_length=1, max_length=5000)
    confirmation: str


class CustomProblemSetsUpdate(BaseModel):
    """Complete replacement payload for the active profile's custom sets."""

    sets: list[dict] = Field(default_factory=list, max_length=40)


class CustomProblemSetsOut(BaseModel):
    version: int = 1
    sets: list[dict] = Field(default_factory=list)


# ----------------------------------------------------------------------------
# Solutions
# ----------------------------------------------------------------------------


class SolutionGet(BaseModel):
    challenge_id: str
    language: SupportedLanguage = "python"
    source: str
    exists: bool


class SolutionPut(BaseModel):
    source: str


class SolutionVersionsGet(BaseModel):
    challenge_id: str
    language: SupportedLanguage = "python"
    active_version: int
    versions: list[int]
    version_names: dict[int, str]
    modified_versions: list[int] = Field(default_factory=list)
    source: str
    starter_source: str = ""
    filename: str = ""


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


class TutorChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str


class AnalyzeRequest(BaseModel):
    source: str = ""
    language: SupportedLanguage = "python"
    returned: str = ""
    expected: str = ""
    inputs: dict[str, str] = Field(default_factory=dict)
    optimal_source: str = ""
    question: Optional[str] = None
    messages: list[TutorChatMessage] = Field(default_factory=list)


class AnalyzeResponse(BaseModel):
    analysis: str
