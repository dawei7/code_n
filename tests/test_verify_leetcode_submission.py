"""Non-destructive verification for replacement LeetCode sources."""

from __future__ import annotations

import json
from pathlib import Path
from unittest.mock import Mock, patch

from server.app.routes.leetcode_submission import LeetCodeCredentials
from tools import verify_leetcode_submission


def test_accepted_replacement_candidate_does_not_mutate_verified_evidence(
    tmp_path: Path,
) -> None:
    branch = tmp_path / "optimal"
    canonical = branch / "solution.py"
    branch.mkdir(parents=True, exist_ok=True)
    canonical.write_text("verified source\n", encoding="utf-8")
    candidate = tmp_path / "candidate.py"
    candidate.write_text("replacement source\n", encoding="utf-8")
    manifest_path = branch / "submission.json"
    manifest = {
        "status": "verified",
        "question_id": "1",
        "title_slug": "two-sum",
        "language": "python3",
        "source": "solution.py",
        "verified_submission_id": "old-submission",
    }
    manifest_path.write_text(json.dumps(manifest), encoding="utf-8")

    submit_response = Mock(status_code=200)
    submit_response.json.return_value = {"submission_id": "new-submission"}
    check_response = Mock()
    check_response.json.return_value = {
        "state": "SUCCESS",
        "status_msg": "Accepted",
        "status_code": 10,
    }
    client = Mock()
    client.post.return_value = submit_response
    client.get.return_value = check_response
    credentials = LeetCodeCredentials(session="session", csrf_token="csrf")

    with (
        patch.object(
            verify_leetcode_submission,
            "load_manifest",
            return_value=(manifest.copy(), manifest_path),
        ),
        patch.object(
            verify_leetcode_submission,
            "_account_status",
            return_value={"state": "valid", "is_premium": False},
        ),
        patch.object(verify_leetcode_submission, "_session", return_value=client),
        patch.object(
            verify_leetcode_submission,
            "verify_remote_metadata",
            return_value={"isPaidOnly": False},
        ),
    ):
        result = verify_leetcode_submission.submit_candidate(
            "lc_1",
            credentials,
            candidate_source=candidate,
        )

    assert result == {
        "accepted": True,
        "submission_id": "new-submission",
        "status": "Accepted",
    }
    assert canonical.read_text(encoding="utf-8") == "verified source\n"
    assert json.loads(manifest_path.read_text(encoding="utf-8")) == manifest
