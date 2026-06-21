"""Progress tracking - saves/loads player completion state."""

import json
import os
from dataclasses import dataclass, field

from .branding import normalize_player_name
from .solutions import PROJECT_ROOT

PROGRESS_FILE = os.path.join(PROJECT_ROOT, "progress.json")


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
    unlocked_leetcode: list[str] = field(default_factory=list)
    milestones: list[str] = field(default_factory=list)
    gemini_api_key: str = ""
    active_set: str = "gfg"

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

    def reset_statuses(self):
        self.completed.clear()
        self.records.clear()
        self.last_status.clear()
        self.leetcode_solved.clear()
        self.unlocked_leetcode.clear()
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
            "unlocked_leetcode": list(self.unlocked_leetcode),
            "milestones": list(self.milestones),
            "gemini_api_key": self.gemini_api_key,
            "active_set": self.active_set
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
        progress.unlocked_leetcode = list(data.get("unlocked_leetcode", []))
        progress.milestones = list(data.get("milestones", []))
        progress.gemini_api_key = str(data.get("gemini_api_key", ""))
        progress.active_set = str(data.get("active_set", "neetcode"))
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
