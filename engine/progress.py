"""Progress tracking - saves/loads player completion state."""

import json
import os
import re
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Literal

from .branding import normalize_player_name

_PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_CODEN_HOME = os.environ.get("CODEN_HOME", os.path.join(_PROJECT_ROOT, ".coden-data"))
PROGRESS_FILE = os.environ.get(
    "CODEN_PROGRESS_FILE",
    os.path.join(_CODEN_HOME, "progress.json"),
)

DEFAULT_ACCENT_COLORS = {"light": "#0284c7", "dark": "#03dac6"}
_HEX_COLOR = re.compile(r"^#[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?$")
_RGBA_COLOR = re.compile(
    r"^rgba\(\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(0(?:\.\d+)?|1(?:\.0+)?)\s*\)$",
    re.IGNORECASE,
)


def normalize_accent_colors(value: object) -> dict[str, str]:
    """Return safe per-theme CSS colors with teal defaults."""

    result = dict(DEFAULT_ACCENT_COLORS)
    if not isinstance(value, dict):
        return result
    for theme in ("light", "dark"):
        raw = value.get(theme)
        if not isinstance(raw, str):
            continue
        color = raw.strip()
        if _HEX_COLOR.fullmatch(color):
            result[theme] = color.lower()
            continue
        match = _RGBA_COLOR.fullmatch(color)
        if not match:
            continue
        red, green, blue = (int(match.group(index)) for index in range(1, 4))
        if max(red, green, blue) > 255:
            continue
        alpha = float(match.group(4))
        result[theme] = f"rgba({red}, {green}, {blue}, {alpha:g})"
    return result


@dataclass
class LevelRecord:
    challenge_id: str
    best_ops: int
    complexity_achieved: str
    attempts: int = 0


@dataclass
class PlayerProgress:
    player_name: str = ""
    completed: set[str] = field(default_factory=set)
    records: dict[str, LevelRecord] = field(default_factory=dict)
    last_status: dict[str, str] = field(default_factory=dict)
    career_mode: bool = False
    leetcode_username: str = ""
    leetcode_solved: list[str] = field(default_factory=list)
    leetcode_submissions: dict[str, dict] = field(default_factory=dict)
    unlocked_leetcode: list[str] = field(default_factory=list)
    milestones: list[str] = field(default_factory=list)
    gemini_api_key: str = ""
    active_set: str = "leetcode"
    sidebar_width: int = 256
    sidebar_position: str = "left"
    sidebar_collapsed: bool = False
    pane_font_scales: dict[str, float] = field(default_factory=dict)
    pane_sizes: dict[str, float] = field(default_factory=dict)
    accent_colors: dict[str, str] = field(default_factory=lambda: dict(DEFAULT_ACCENT_COLORS))
    custom_problem_sets: list[dict] = field(default_factory=list)

    def complete(self, challenge_id: str, ops: int, complexity: str):
        self.completed.add(challenge_id)
        self.last_status[challenge_id] = "done"
        existing = self.records.get(challenge_id)
        if existing:
            existing.attempts += 1
            if ops < existing.best_ops:
                existing.best_ops = ops
                existing.complexity_achieved = complexity
        else:
            self.records[challenge_id] = LevelRecord(
                challenge_id=challenge_id,
                best_ops=ops,
                complexity_achieved=complexity,
                attempts=1
            )

    def fail(self, challenge_id: str):
        self.completed.discard(challenge_id)
        self.last_status[challenge_id] = "failed"

    def reset_statuses(
        self,
        challenge_ids: Iterable[str] | None = None,
        scope: Literal["all", "coden", "leetcode"] = "all",
    ):
        """Clear selected progress while preserving profile settings and solutions."""

        if scope not in {"all", "coden", "leetcode"}:
            raise ValueError(f"Unsupported progress reset scope: {scope}")

        selected = None if challenge_ids is None else {str(challenge_id) for challenge_id in challenge_ids}

        if scope in {"all", "coden"}:
            if selected is None:
                self.completed.clear()
                self.records.clear()
                self.last_status.clear()
            else:
                self.completed.difference_update(selected)
                for challenge_id in selected:
                    self.records.pop(challenge_id, None)
                    self.last_status.pop(challenge_id, None)

        if scope in {"all", "leetcode"}:
            if selected is None:
                self.leetcode_solved.clear()
                self.leetcode_submissions.clear()
                self.unlocked_leetcode.clear()
            else:
                self.leetcode_solved = [
                    challenge_id
                    for challenge_id in self.leetcode_solved
                    if challenge_id not in selected
                ]
                self.unlocked_leetcode = [
                    challenge_id
                    for challenge_id in self.unlocked_leetcode
                    if challenge_id not in selected
                ]
                for challenge_id in selected:
                    self.leetcode_submissions.pop(challenge_id, None)

        # Milestones belong to the retired progression model and are never
        # retained after a progress mutation.
        self.milestones.clear()

    def status_for(self, challenge_id: str) -> str:
        status = self.last_status.get(challenge_id)
        if status:
            return status
        if challenge_id in self.completed:
            return "done"
        return "open"

    def to_dict(self) -> dict:
        return {
            "player_name": normalize_player_name(self.player_name) if self.player_name else "",
            "completed": list(self.completed),
            "last_status": self.last_status,
            "records": {
                k: {
                    "challenge_id": v.challenge_id,
                    "best_ops": v.best_ops,
                    "complexity_achieved": v.complexity_achieved,
                    "attempts": v.attempts,
                }
                for k, v in self.records.items()
            },
            "career_mode": self.career_mode,
            "leetcode_username": self.leetcode_username,
            "leetcode_solved": list(self.leetcode_solved),
            "leetcode_submissions": dict(self.leetcode_submissions),
            "unlocked_leetcode": list(self.unlocked_leetcode),
            "milestones": list(self.milestones),
            "gemini_api_key": self.gemini_api_key,
            "active_set": self.active_set,
            "sidebar_width": self.sidebar_width,
            "sidebar_position": self.sidebar_position,
            "sidebar_collapsed": self.sidebar_collapsed,
            "pane_font_scales": dict(self.pane_font_scales),
            "pane_sizes": dict(self.pane_sizes),
            "accent_colors": normalize_accent_colors(self.accent_colors),
            "custom_problem_sets": [
                dict(problem_set)
                for problem_set in self.custom_problem_sets
                if isinstance(problem_set, dict)
            ],
        }

    @classmethod
    def from_dict(cls, data: dict) -> "PlayerProgress":
        progress = cls()
        progress.player_name = normalize_player_name(data.get("player_name", "")) if data.get("player_name") else ""
        progress.last_status = dict(data.get("last_status", {}))
        old_completed = set(data.get("completed", []))
        for k, v in data.get("records", {}).items():
            progress.records[k] = LevelRecord(**v)
        for challenge_id in old_completed:
            progress.last_status.setdefault(challenge_id, "done")
        progress.completed = {challenge_id for challenge_id, status in progress.last_status.items() if status == "done"}
        progress.career_mode = bool(data.get("career_mode", False))
        progress.leetcode_username = str(data.get("leetcode_username", ""))
        progress.leetcode_solved = list(data.get("leetcode_solved", []))
        progress.leetcode_submissions = {
            str(challenge_id): dict(record)
            for challenge_id, record in dict(data.get("leetcode_submissions", {})).items()
            if isinstance(record, dict)
        }
        progress.unlocked_leetcode = list(data.get("unlocked_leetcode", []))
        progress.milestones = list(data.get("milestones", []))
        progress.gemini_api_key = str(data.get("gemini_api_key", ""))
        progress.active_set = str(data.get("active_set", "leetcode"))
        progress.sidebar_width = int(data.get("sidebar_width", 256))
        progress.sidebar_position = str(data.get("sidebar_position", "left"))
        progress.sidebar_collapsed = bool(data.get("sidebar_collapsed", False))
        progress.pane_font_scales = {
            str(scope): max(0.75, min(1.5, float(scale)))
            for scope, scale in dict(data.get("pane_font_scales", {})).items()
        }
        progress.pane_sizes = {
            str(scope): max(120.0, min(1600.0, float(size)))
            for scope, size in dict(data.get("pane_sizes", {})).items()
        }
        progress.accent_colors = normalize_accent_colors(data.get("accent_colors"))
        raw_custom_sets = data.get("custom_problem_sets", [])
        progress.custom_problem_sets = [
            dict(problem_set)
            for problem_set in raw_custom_sets
            if isinstance(problem_set, dict)
        ] if isinstance(raw_custom_sets, list) else []
        return progress


def save_progress(progress: PlayerProgress, path: str | None = None):
    # Resolve the path at call time (not import time) so tests
    # can patch PROGRESS_FILE before invoking this function.
    if path is None:
        path = PROGRESS_FILE
    with open(path, "w", encoding="utf-8") as f:
        json.dump(progress.to_dict(), f, indent=2)


def load_progress(path: str | None = None) -> PlayerProgress:
    if path is None:
        path = PROGRESS_FILE
    if not os.path.exists(path):
        return PlayerProgress()
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return PlayerProgress.from_dict(data)
