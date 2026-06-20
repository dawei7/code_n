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
            }
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
