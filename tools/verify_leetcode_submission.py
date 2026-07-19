"""Submit one package candidate and promote it only after LeetCode accepts it.

Credentials are intentionally read from environment variables, never command
arguments, so they do not appear in shell history or process listings.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from server.app.challenge_packages import leetcode_submission_manifest_path  # noqa: E402
from server.app.routes.leetcode_submission import (  # noqa: E402
    LeetCodeCredentials,
    _account_status,
    _session,
)
from tools.leetcode_browser_submit import submit_with_chrome  # noqa: E402


BASE_URL = "https://leetcode.com"


def credentials_from_environment() -> LeetCodeCredentials:
    session = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = os.environ.get("LEETCODE_CSRFTOKEN", "").strip()
    if not session or not csrf:
        raise RuntimeError("Set LEETCODE_SESSION and LEETCODE_CSRFTOKEN in the current shell.")
    return LeetCodeCredentials(
        session=session,
        csrf_token=csrf,
        cloudflare_clearance=os.environ.get("LEETCODE_CFCLEARANCE", "").strip(),
    )


def load_manifest(challenge_id: str, variant_id: str | None = None) -> tuple[dict, Path]:
    path = leetcode_submission_manifest_path(challenge_id, variant_id)
    if path is None or not path.is_file():
        suffix = f" variant {variant_id}" if variant_id else ""
        raise RuntimeError(f"No submission.json exists for {challenge_id}{suffix}.")
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise RuntimeError(f"{path} must contain a JSON object.")
    source = path.parent / str(payload.get("source") or "")
    if not source.is_file():
        raise RuntimeError(f"Submission source is missing: {source}")
    return payload, path


def verify_remote_metadata(client: requests.Session, manifest: dict) -> dict:
    query = """query questionData($titleSlug: String!) {
      question(titleSlug: $titleSlug) {
        questionId questionFrontendId titleSlug isPaidOnly
        codeSnippets { langSlug }
      }
    }"""
    response = client.post(
        f"{BASE_URL}/graphql/",
        json={"query": query, "variables": {"titleSlug": manifest["title_slug"]}},
        headers={"Referer": f"{BASE_URL}/problems/{manifest['title_slug']}/"},
        timeout=20,
    )
    response.raise_for_status()
    question = response.json().get("data", {}).get("question")
    if not isinstance(question, dict):
        raise RuntimeError("LeetCode did not return question metadata; access may be restricted.")
    if str(question.get("questionId")) != str(manifest.get("question_id")):
        raise RuntimeError(
            "Manifest question_id does not match LeetCode "
            f"(manifest={manifest.get('question_id')}, live={question.get('questionId')})."
        )
    languages = {str(snippet.get("langSlug")) for snippet in question.get("codeSnippets", [])}
    if str(manifest.get("language")) not in languages:
        raise RuntimeError("Manifest language is not supported by this LeetCode problem.")
    return question


def submit_candidate(
    challenge_id: str,
    credentials: LeetCodeCredentials,
    variant_id: str | None = None,
) -> dict:
    manifest, manifest_path = load_manifest(challenge_id, variant_id)
    account = _account_status(credentials)
    if account.get("state") != "valid":
        raise RuntimeError(str(account.get("message") or "LeetCode session is invalid."))
    client = _session(credentials)
    question = verify_remote_metadata(client, manifest)
    if question.get("isPaidOnly") and not account.get("is_premium"):
        raise RuntimeError("This candidate requires LeetCode Premium access for the connected account.")

    slug = str(manifest["title_slug"])
    source_path = manifest_path.parent / str(manifest["source"])
    response = client.post(
        f"{BASE_URL}/problems/{slug}/submit/",
        json={
            "question_id": str(manifest["question_id"]),
            "lang": str(manifest["language"]),
            "typed_code": source_path.read_text(encoding="utf-8"),
            "questionSlug": slug,
        },
        headers={
            "Referer": f"{BASE_URL}/problems/{slug}/submissions/",
            "x-csrftoken": credentials.csrf_token,
            "Content-Type": "application/json",
        },
        timeout=30,
    )
    if response.status_code == 403:
        submission_id, result = submit_with_chrome(
            slug=slug,
            question_id=str(manifest["question_id"]),
            language=str(manifest["language"]),
            source=source_path.read_text(encoding="utf-8"),
            session_cookie=credentials.session,
            csrf_token=credentials.csrf_token,
            clearance=credentials.cloudflare_clearance,
        )
    else:
        response.raise_for_status()
        submission_id = str(response.json().get("submission_id") or "")
        result = {}
    if not submission_id:
        raise RuntimeError("LeetCode did not return a submission ID.")

    if not result:
        for _ in range(60):
            time.sleep(0.5)
            check = client.get(
                f"{BASE_URL}/submissions/detail/{submission_id}/check/",
                headers={"Referer": f"{BASE_URL}/problems/{slug}/submissions/"},
                timeout=20,
            )
            check.raise_for_status()
            result = check.json()
            if result.get("state") == "SUCCESS" or result.get("finished"):
                break
    status = str(result.get("status_msg") or result.get("state") or "Unknown")
    accepted = status == "Accepted" or result.get("status_code") == 10
    print(f"LeetCode submission {submission_id}: {status}")
    if not accepted:
        return {"accepted": False, "submission_id": submission_id, "status": status}

    manifest.update(
        {
            "status": "verified",
            "paid_only": bool(question.get("isPaidOnly")),
            "verified_submission_id": submission_id,
            "verified_at": datetime.now(timezone.utc).isoformat(),
        }
    )
    temporary = manifest_path.with_suffix(".json.tmp")
    temporary.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    temporary.replace(manifest_path)
    print(f"Promoted verified package manifest: {manifest_path}")
    return {"accepted": True, "submission_id": submission_id, "status": status}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("challenge_id", help="Canonical challenge id, for example lc_1")
    parser.add_argument(
        "--variant",
        help="Optional solution-variant id, for example simplified.",
    )
    parser.add_argument(
        "--confirm-submit",
        action="store_true",
        help="Required acknowledgement that this creates a real LeetCode submission.",
    )
    args = parser.parse_args()
    if not args.confirm_submit:
        parser.error("--confirm-submit is required; verification creates a real external submission.")
    try:
        result = submit_candidate(
            args.challenge_id,
            credentials_from_environment(),
            args.variant,
        )
    except (RuntimeError, requests.RequestException, ValueError, KeyError) as exc:
        print(f"Verification failed: {exc}", file=sys.stderr)
        return 1
    return 0 if result["accepted"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
