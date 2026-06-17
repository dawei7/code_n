"""Tests for ``POST /api/vscode/active`` — the cOde(n) → VSCode
active-challenge handoff.

The endpoint writes the player's current challenge id to
``solutions/.vscode-active`` so the next time the user
presses F5 in VSCode, the launch config defaults to the
right challenge. ``tools/run_solution.py`` reads the file
when no id is passed on the command line.
"""
from __future__ import annotations

import json
import os
import unittest

from . import conftest  # noqa: F401


class VSCodeHandoffTest(conftest._Base):
    """The /api/vscode/active endpoint."""

    def test_writes_file_for_valid_challenge(self) -> None:
        r = self.client.post(
            "/api/vscode/active",
            json={"challenge_id": "sort_01"},
        )
        self.assertEqual(r.status_code, 200)
        body = r.json()
        self.assertTrue(body["ok"])
        self.assertIn(".vscode-active", body["path"])

        # The file is what tools/run_solution.py reads. Format:
        # ``{"id": "sort_01"}``.
        handoff_path = os.path.join(
            os.environ["CODEN_SOLUTIONS_DIR"],
            ".vscode-active",
        )
        self.assertTrue(os.path.isfile(handoff_path))
        with open(handoff_path, "r", encoding="utf-8") as f:
            payload = json.loads(f.read())
        self.assertEqual(payload["id"], "sort_01")

    def test_rejects_unknown_challenge(self) -> None:
        r = self.client.post(
            "/api/vscode/active",
            json={"challenge_id": "does_not_exist"},
        )
        # Safety guard: a typo shouldn't silently leave the
        # handoff at the wrong value.
        self.assertEqual(r.status_code, 404)
        self.assertIn("not found", r.json().get("detail", ""))

    def test_overwrites_previous_handoff(self) -> None:
        # First write sort_01, then write search_03. The file
        # should reflect the second call.
        self.client.post(
            "/api/vscode/active",
            json={"challenge_id": "sort_01"},
        )
        r = self.client.post(
            "/api/vscode/active",
            json={"challenge_id": "search_03"},
        )
        self.assertEqual(r.status_code, 200)
        handoff_path = os.path.join(
            os.environ["CODEN_SOLUTIONS_DIR"],
            ".vscode-active",
        )
        with open(handoff_path, "r", encoding="utf-8") as f:
            payload = json.loads(f.read())
        self.assertEqual(payload["id"], "search_03")

    def test_handoff_file_format_is_stable(self) -> None:
        # The format is the contract with tools/run_solution.py:
        # a JSON object with an ``id`` key. If we ever change
        # it, we have to update the script.
        self.client.post(
            "/api/vscode/active",
            json={"challenge_id": "intro_01"},
        )
        handoff_path = os.path.join(
            os.environ["CODEN_SOLUTIONS_DIR"],
            ".vscode-active",
        )
        with open(handoff_path, "r", encoding="utf-8") as f:
            text = f.read()
        # The file is JSON; the top-level object has an "id" key.
        payload = json.loads(text)
        self.assertIn("id", payload)
        self.assertIsInstance(payload["id"], str)


if __name__ == "__main__":
    unittest.main()
