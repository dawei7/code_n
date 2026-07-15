"""Validated, package-authored algorithm visualization manifests.

The manifest describes teaching phases and deterministic state snapshots. Code
is never duplicated in the manifest: semantic anchors are resolved against the
package's canonical solution and returned with that real source for Monaco.
The generic player owns playback, navigation, narration, and code sync; each
renderer owns only the problem-shaped scene.
"""
from __future__ import annotations

from functools import lru_cache
from math import isclose
from pathlib import Path, PurePosixPath
from typing import Annotated, Literal

from pydantic import BaseModel, ConfigDict, Field, TypeAdapter, model_validator

from server.app.challenge_packages import (
    leetcode_package_dir,
    leetcode_visualization_path,
)


class _StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class VisualizationPhase(_StrictModel):
    id: str = Field(min_length=1)
    title: str = Field(min_length=1)
    summary: str = Field(min_length=1)


class VisualizationComplexity(_StrictModel):
    time: str = Field(min_length=1)
    space: str = Field(min_length=1)


class VisualizationBadge(_StrictModel):
    label: str = Field(min_length=1)
    tone: Literal["neutral", "active", "attention", "success"] = "neutral"


class VisualizationCodeAnchorManifest(_StrictModel):
    start: str = Field(min_length=1)
    end: str | None = None


class VisualizationCodeManifest(_StrictModel):
    language: str = Field(min_length=1)
    source_path: str = Field(min_length=1)
    anchors: dict[str, VisualizationCodeAnchorManifest] = Field(min_length=1)


class VisualizationStepBase(_StrictModel):
    id: str = Field(min_length=1)
    phase: str = Field(min_length=1)
    title: str = Field(min_length=1)
    description: str = Field(min_length=1)
    insight: str = ""
    badge: VisualizationBadge
    active_code: list[str] = Field(min_length=1)
    duration_ms: int = Field(default=1600, ge=900, le=5000)


class VisualizationManifestBase(_StrictModel):
    version: Literal[2]
    challenge_id: str
    title: str = Field(min_length=1)
    pattern: str = Field(min_length=1)
    summary: str = Field(min_length=1)
    learning_objective: str = Field(min_length=1)
    invariant: str = Field(min_length=1)
    complexity: VisualizationComplexity
    phases: list[VisualizationPhase] = Field(min_length=1)
    code: VisualizationCodeManifest


def _validate_lesson_structure(
    phases: list[VisualizationPhase],
    steps: list[VisualizationStepBase],
    anchors: dict[str, VisualizationCodeAnchorManifest],
) -> None:
    step_ids: set[str] = set()
    phase_ids = [phase.id for phase in phases]
    if len(set(phase_ids)) != len(phase_ids):
        raise ValueError("visualization phase ids must be unique")
    phase_order = {phase_id: index for index, phase_id in enumerate(phase_ids)}
    previous_phase_index = 0

    for step in steps:
        if step.id in step_ids:
            raise ValueError(f"duplicate visualization step id: {step.id}")
        step_ids.add(step.id)
        if step.phase not in phase_order:
            raise ValueError(f"step {step.id} references unknown phase {step.phase!r}")
        current_phase_index = phase_order[step.phase]
        if current_phase_index < previous_phase_index:
            raise ValueError(f"step {step.id} moves backward in the phase sequence")
        previous_phase_index = current_phase_index
        missing_anchors = set(step.active_code) - set(anchors)
        if missing_anchors:
            raise ValueError(
                f"step {step.id} references unknown code anchors: {sorted(missing_anchors)}"
            )

    if {step.phase for step in steps} != set(phase_ids):
        raise ValueError("every visualization phase must contain at least one step")


class VisualizationCodeRange(_StrictModel):
    start_line: int = Field(ge=1)
    end_line: int = Field(ge=1)


class ResolvedVisualizationCode(_StrictModel):
    language: str
    source_path: str
    source: str
    anchors: dict[str, VisualizationCodeRange]


class ArrayHashMapExample(_StrictModel):
    nums: list[int] = Field(min_length=2)
    target: int


class HashMapEntry(_StrictModel):
    value: int
    index: int = Field(ge=0)


class TraceVariables(_StrictModel):
    index: int | None = Field(default=None, ge=0)
    value: int | None = None
    complement: int | None = None


class ArrayHashMapState(_StrictModel):
    event: Literal["ready", "scanning", "miss", "stored", "found", "returned"]
    current_index: int | None = Field(default=None, ge=0)
    match_index: int | None = Field(default=None, ge=0)
    visited_indices: list[int] = Field(default_factory=list)
    variables: TraceVariables
    seen: list[HashMapEntry] = Field(default_factory=list)
    result: list[int] | None = None
    changed: list[
        Literal["index", "value", "complement", "lookup", "seen", "result"]
    ] = Field(default_factory=list)


class ArrayHashMapStep(VisualizationStepBase):
    state: ArrayHashMapState


class ArrayHashMapVisualizationManifest(VisualizationManifestBase):
    renderer: Literal["array-hash-map"]
    example: ArrayHashMapExample
    steps: list[ArrayHashMapStep] = Field(min_length=2)

    @model_validator(mode="after")
    def validate_trace(self) -> "ArrayHashMapVisualizationManifest":
        size = len(self.example.nums)
        _validate_lesson_structure(self.phases, self.steps, self.code.anchors)

        for step in self.steps:
            state = step.state
            indices = [
                state.current_index,
                state.match_index,
                *state.visited_indices,
                *(entry.index for entry in state.seen),
                *(state.result or []),
            ]
            if any(index is not None and index >= size for index in indices):
                raise ValueError(f"step {step.id} references an index outside the example array")

            if state.current_index is not None:
                if state.variables.index != state.current_index:
                    raise ValueError(f"step {step.id} has inconsistent current index state")
                if state.variables.value != self.example.nums[state.current_index]:
                    raise ValueError(f"step {step.id} has inconsistent current value state")

            if len({entry.value for entry in state.seen}) != len(state.seen):
                raise ValueError(f"step {step.id} contains duplicate hash-map keys")

            if state.result is not None:
                if len(state.result) != 2 or state.result[0] == state.result[1]:
                    raise ValueError(f"step {step.id} must return two distinct indices")
                left, right = state.result
                if self.example.nums[left] + self.example.nums[right] != self.example.target:
                    raise ValueError(f"step {step.id} result does not sum to the target")

        final_state = self.steps[-1].state
        if final_state.event != "returned" or final_state.result is None:
            raise ValueError("the final array-hash-map step must return the answer")
        return self


PartitionBoundary = int | Literal["-inf", "inf"]


class BinaryPartitionExample(_StrictModel):
    nums1: list[int]
    nums2: list[int]
    expected: float


class BinaryPartitionBoundaries(_StrictModel):
    left1: PartitionBoundary | None = None
    right1: PartitionBoundary | None = None
    left2: PartitionBoundary | None = None
    right2: PartitionBoundary | None = None


class BinaryPartitionComparison(_StrictModel):
    left1_le_right2: bool | None = None
    left2_le_right1: bool | None = None


class BinaryPartitionState(_StrictModel):
    event: Literal[
        "ready", "searching", "partitioned", "compared", "narrowed", "valid", "returned"
    ]
    low: int | None = Field(default=None, ge=0)
    high: int | None = Field(default=None, ge=0)
    cut1: int | None = Field(default=None, ge=0)
    cut2: int | None = Field(default=None, ge=0)
    boundaries: BinaryPartitionBoundaries
    comparison: BinaryPartitionComparison
    violation: Literal["none", "left1-too-large", "left2-too-large", "valid"] = "none"
    result: float | None = None
    changed: list[
        Literal["range", "cuts", "boundaries", "comparison", "result"]
    ] = Field(default_factory=list)


class BinaryPartitionStep(VisualizationStepBase):
    state: BinaryPartitionState


def _boundary_value(values: list[int], index: int, *, side: Literal["left", "right"]) -> PartitionBoundary:
    if side == "left":
        return values[index - 1] if index else "-inf"
    return values[index] if index < len(values) else "inf"


def _numeric_boundary(value: PartitionBoundary) -> float:
    if value == "-inf":
        return float("-inf")
    if value == "inf":
        return float("inf")
    return float(value)


class BinaryPartitionVisualizationManifest(VisualizationManifestBase):
    renderer: Literal["binary-partition"]
    example: BinaryPartitionExample
    steps: list[BinaryPartitionStep] = Field(min_length=2)

    @model_validator(mode="after")
    def validate_trace(self) -> "BinaryPartitionVisualizationManifest":
        nums1 = self.example.nums1
        nums2 = self.example.nums2
        if not nums1 and not nums2:
            raise ValueError("binary-partition example must contain at least one value")
        if nums1 != sorted(nums1) or nums2 != sorted(nums2):
            raise ValueError("binary-partition example arrays must be sorted")
        if len(nums1) > len(nums2):
            raise ValueError("binary-partition example must put the shorter array first")

        merged = sorted([*nums1, *nums2])
        middle = len(merged) // 2
        expected = (
            float(merged[middle])
            if len(merged) % 2
            else (merged[middle - 1] + merged[middle]) / 2.0
        )
        if not isclose(self.example.expected, expected):
            raise ValueError("binary-partition example has an incorrect expected median")

        _validate_lesson_structure(self.phases, self.steps, self.code.anchors)
        left_size = (len(merged) + 1) // 2
        for step in self.steps:
            state = step.state
            if (state.low is None) != (state.high is None):
                raise ValueError(f"step {step.id} must define both search bounds or neither")
            if state.low is not None and state.high is not None:
                if state.low > state.high or state.high > len(nums1):
                    raise ValueError(f"step {step.id} has an invalid binary-search range")

            if (state.cut1 is None) != (state.cut2 is None):
                raise ValueError(f"step {step.id} must define both cuts or neither")
            boundary_values = state.boundaries.model_dump()
            has_boundaries = any(value is not None for value in boundary_values.values())
            has_comparison = state.comparison.left1_le_right2 is not None
            if has_comparison != (state.comparison.left2_le_right1 is not None):
                raise ValueError(f"step {step.id} must define both comparisons or neither")

            if state.cut1 is None or state.cut2 is None:
                if has_boundaries or has_comparison or state.violation != "none":
                    raise ValueError(f"step {step.id} cannot evaluate a missing partition")
                continue

            if state.cut1 > len(nums1) or state.cut2 > len(nums2):
                raise ValueError(f"step {step.id} places a cut outside an example array")
            if state.cut2 != left_size - state.cut1:
                raise ValueError(f"step {step.id} cuts do not create the required left size")

            expected_boundaries = {
                "left1": _boundary_value(nums1, state.cut1, side="left"),
                "right1": _boundary_value(nums1, state.cut1, side="right"),
                "left2": _boundary_value(nums2, state.cut2, side="left"),
                "right2": _boundary_value(nums2, state.cut2, side="right"),
            }
            if has_boundaries:
                if boundary_values != expected_boundaries:
                    raise ValueError(f"step {step.id} has boundary values inconsistent with its cuts")
            elif has_comparison or state.violation != "none":
                raise ValueError(f"step {step.id} cannot compare boundaries before reading them")

            if has_comparison:
                first = _numeric_boundary(expected_boundaries["left1"]) <= _numeric_boundary(expected_boundaries["right2"])
                second = _numeric_boundary(expected_boundaries["left2"]) <= _numeric_boundary(expected_boundaries["right1"])
                if state.comparison.left1_le_right2 != first or state.comparison.left2_le_right1 != second:
                    raise ValueError(f"step {step.id} has an incorrect partition comparison")
                expected_violation = "valid" if first and second else "left1-too-large" if not first else "left2-too-large"
                if state.violation != expected_violation:
                    raise ValueError(f"step {step.id} has an incorrect partition verdict")

            if state.result is not None:
                if state.violation != "valid" or not isclose(state.result, expected):
                    raise ValueError(f"step {step.id} returns an invalid median")

        final_state = self.steps[-1].state
        if final_state.event != "returned" or final_state.result is None:
            raise ValueError("the final binary-partition step must return the median")
        return self


class VisualizationDefinitionBase(_StrictModel):
    """Common resolved API payload consumed by the reusable player."""

    version: Literal[2]
    challenge_id: str
    title: str
    pattern: str
    summary: str
    learning_objective: str
    invariant: str
    complexity: VisualizationComplexity
    phases: list[VisualizationPhase]
    code: ResolvedVisualizationCode


class ArrayHashMapVisualizationDefinition(VisualizationDefinitionBase):
    renderer: Literal["array-hash-map"]
    example: ArrayHashMapExample
    steps: list[ArrayHashMapStep]


class BinaryPartitionVisualizationDefinition(VisualizationDefinitionBase):
    renderer: Literal["binary-partition"]
    example: BinaryPartitionExample
    steps: list[BinaryPartitionStep]


VisualizationManifest = Annotated[
    ArrayHashMapVisualizationManifest | BinaryPartitionVisualizationManifest,
    Field(discriminator="renderer"),
]
VisualizationDefinition = Annotated[
    ArrayHashMapVisualizationDefinition | BinaryPartitionVisualizationDefinition,
    Field(discriminator="renderer"),
]
_MANIFEST_ADAPTER = TypeAdapter(VisualizationManifest)


def _unique_matching_line(lines: list[str], needle: str, *, anchor_name: str) -> int:
    matches = [index for index, line in enumerate(lines) if needle in line]
    if len(matches) != 1:
        raise ValueError(
            f"code anchor {anchor_name!r} expected one line containing {needle!r}, "
            f"found {len(matches)}"
        )
    return matches[0] + 1


def _resolve_code(
    challenge_id: str,
    manifest: VisualizationCodeManifest,
) -> ResolvedVisualizationCode:
    package_dir = leetcode_package_dir(challenge_id)
    if package_dir is None:
        raise ValueError(f"canonical package not found for {challenge_id}")

    relative = PurePosixPath(manifest.source_path)
    if relative.is_absolute() or not relative.parts or relative.parts[0] != "solutions":
        raise ValueError("visualization code source must be a package-local solutions/* file")
    if ".." in relative.parts:
        raise ValueError("visualization code source may not traverse outside the package")

    package_root = package_dir.resolve()
    source_path = (package_root / Path(*relative.parts)).resolve()
    try:
        source_path.relative_to(package_root)
    except ValueError as exc:
        raise ValueError("visualization code source escapes the canonical package") from exc
    if not source_path.is_file():
        raise ValueError(f"visualization code source does not exist: {manifest.source_path}")

    source = source_path.read_text(encoding="utf-8")
    lines = source.splitlines()
    resolved: dict[str, VisualizationCodeRange] = {}
    for name, anchor in manifest.anchors.items():
        start_line = _unique_matching_line(lines, anchor.start, anchor_name=name)
        end_line = start_line
        if anchor.end:
            end_line = _unique_matching_line(lines, anchor.end, anchor_name=name)
            if end_line < start_line:
                raise ValueError(f"code anchor {name!r} ends before it starts")
        resolved[name] = VisualizationCodeRange(
            start_line=start_line,
            end_line=end_line,
        )

    return ResolvedVisualizationCode(
        language=manifest.language,
        source_path=manifest.source_path,
        source=source,
        anchors=resolved,
    )


@lru_cache(maxsize=4096)
def load_visualization(challenge_id: str) -> VisualizationDefinition | None:
    """Load, validate, and resolve one optional visualization manifest."""
    path = leetcode_visualization_path(challenge_id)
    if path is None or not path.is_file():
        return None
    manifest = _MANIFEST_ADAPTER.validate_json(path.read_text(encoding="utf-8"))
    if manifest.challenge_id != challenge_id:
        raise ValueError(
            f"visualization challenge_id {manifest.challenge_id!r} does not match {challenge_id!r}"
        )
    code = _resolve_code(challenge_id, manifest.code)
    definition_type = (
        ArrayHashMapVisualizationDefinition
        if isinstance(manifest, ArrayHashMapVisualizationManifest)
        else BinaryPartitionVisualizationDefinition
    )
    return definition_type(**manifest.model_dump(exclude={"code"}), code=code)
