"""LeetCode submission availability and security boundaries."""
from __future__ import annotations

import os
from unittest.mock import patch

from server.app.routes import leetcode_submission

from . import conftest


class LeetCodeSubmissionTest(conftest._Base):
    def test_challenge_list_exposes_problem_level_submission_state(self) -> None:
        response = self.client.get("/api/challenges")
        self.assertEqual(response.status_code, 200, response.text)
        two_sum = next(challenge for challenge in response.json() if challenge["id"] == "lc_1")
        self.assertEqual(two_sum["leetcode_submission_status"], "verified")
        self.assertEqual(two_sum["leetcode_submission_language"], "python3")
        self.assertFalse(two_sum["leetcode_submission_paid_only"])

    def test_two_sum_has_a_remotely_verified_submission(self) -> None:
        response = self.client.get("/api/leetcode/submissions/lc_1/availability")
        self.assertEqual(response.status_code, 200, response.text)
        body = response.json()
        self.assertTrue(body["available"])
        self.assertEqual(body["status"], "verified")
        self.assertEqual(body["reason"], "")
        manifest, _path = leetcode_submission._manifest("lc_1")
        self.assertTrue(manifest["verified_submission_id"])
        self.assertTrue(manifest["verified_at"])

    def test_missing_submission_has_an_explicit_blocked_reason(self) -> None:
        with patch.object(leetcode_submission, "_manifest", return_value=({}, None)):
            response = self.client.get("/api/leetcode/submissions/lc_2/availability")
        self.assertEqual(response.status_code, 200, response.text)
        self.assertFalse(response.json()["available"])
        self.assertIn("No reviewed LeetCode submission", response.json()["reason"])

    def test_internal_session_endpoint_requires_desktop_bridge_token(self) -> None:
        payload = {"credentials": {"session": "secret", "csrf_token": "csrf"}}
        with patch.dict(os.environ, {"CODEN_DESKTOP_BRIDGE_TOKEN": "expected"}):
            rejected = self.client.post("/api/leetcode/internal/session/status", json=payload)
            self.assertEqual(rejected.status_code, 403, rejected.text)
            with patch.object(
                leetcode_submission,
                "_account_status",
                return_value={"state": "valid", "username": "tester", "is_premium": False},
            ):
                accepted = self.client.post(
                    "/api/leetcode/internal/session/status",
                    json=payload,
                    headers={"X-Coden-Desktop-Token": "expected"},
                )
        self.assertEqual(accepted.status_code, 200, accepted.text)
        self.assertEqual(accepted.json()["username"], "tester")

    def test_candidate_cannot_be_submitted_even_with_credentials(self) -> None:
        candidate = {
            "available": False,
            "status": "candidate",
            "reason": "The packaged LeetCode submission is awaiting acceptance verification.",
            "paid_only": False,
        }
        with patch.object(leetcode_submission, "_availability", return_value=candidate):
            response = self.client.post(
                "/api/leetcode/internal/submissions/lc_1",
                json={"credentials": {"session": "secret", "csrf_token": "csrf"}},
            )
        self.assertEqual(response.status_code, 409, response.text)
        self.assertIn("awaiting acceptance verification", response.json()["detail"])

    def test_two_sum_platform_source_uses_leetcode_declaration(self) -> None:
        manifest, manifest_path = leetcode_submission._manifest("lc_1")
        self.assertIsNotNone(manifest_path)
        source = (manifest_path.parent / manifest["source"]).read_text(encoding="utf-8")
        namespace: dict[str, object] = {}
        exec(compile(source, str(manifest_path), "exec"), namespace)
        solution = namespace["Solution"]()
        self.assertEqual(solution.twoSum([2, 7, 11, 15], 9), [0, 1])

    def test_longest_common_prefix_has_verified_platform_source(self) -> None:
        availability = self.client.get("/api/leetcode/submissions/lc_14/availability")
        self.assertEqual(availability.status_code, 200, availability.text)
        self.assertTrue(availability.json()["available"])
        self.assertEqual(availability.json()["status"], "verified")

        manifest, manifest_path = leetcode_submission._manifest("lc_14")
        self.assertIsNotNone(manifest_path)
        self.assertEqual(manifest["question_id"], "14")
        self.assertTrue(manifest["verified_submission_id"])
        source = (manifest_path.parent / manifest["source"]).read_text(encoding="utf-8")
        namespace: dict[str, object] = {}
        exec(compile(source, str(manifest_path), "exec"), namespace)
        solution = namespace["Solution"]()
        self.assertEqual(solution.longestCommonPrefix(["flower", "flow", "flight"]), "fl")
