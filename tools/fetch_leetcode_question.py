"""Fetch one canonical LeetCode question through an authenticated session.

Credentials are read only from environment variables populated by the secure
Electron bridge. They are never accepted as command arguments or included in
the output. The fetched statement is transient authoring evidence and is not
written into the canonical dataset.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

import requests

PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from server.app.challenge_packages import leetcode_metadata  # noqa: E402
from server.app.routes.leetcode_submission import (  # noqa: E402
    LeetCodeCredentials,
    _session,
)
from tools.leetcode_browser_submit import fetch_question_with_chrome  # noqa: E402


BASE_URL = "https://leetcode.com"
QUESTION_QUERY = """query questionData($titleSlug: String!) {
  question(titleSlug: $titleSlug) {
    questionId
    questionFrontendId
    title
    titleSlug
    isPaidOnly
    content
    codeSnippets {
      lang
      langSlug
      code
    }
  }
}"""


def credentials_from_environment() -> LeetCodeCredentials:
    session = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = os.environ.get("LEETCODE_CSRFTOKEN", "").strip()
    if not session or not csrf:
        raise RuntimeError("Authenticated LeetCode credentials are unavailable.")
    return LeetCodeCredentials(
        session=session,
        csrf_token=csrf,
        cloudflare_clearance=os.environ.get("LEETCODE_CFCLEARANCE", "").strip(),
    )


def _statement_text(content_html: str) -> str:
    with_breaks = re.sub(
        r"</?(?:p|li|ul|ol|pre|table|tr|h[1-6]|br)\b[^>]*>",
        "\n",
        content_html,
        flags=re.IGNORECASE,
    )
    without_tags = re.sub(r"<[^>]+>", " ", with_breaks)
    lines = [
        re.sub(r"[ \t]+", " ", html.unescape(line)).strip()
        for line in without_tags.splitlines()
    ]
    return "\n".join(line for line in lines if line)


def fetch_question(client: requests.Session, challenge_id: str) -> dict[str, Any]:
    metadata = leetcode_metadata(challenge_id)
    if not metadata:
        raise RuntimeError(f"No canonical metadata exists for {challenge_id}.")
    slug = str(metadata.get("slug") or "")
    if not slug:
        raise RuntimeError(f"Canonical metadata for {challenge_id} has no slug.")

    response = client.post(
        f"{BASE_URL}/graphql/",
        json={"query": QUESTION_QUERY, "variables": {"titleSlug": slug}},
        headers={"Referer": f"{BASE_URL}/problems/{slug}/"},
        timeout=60,
    )
    response.raise_for_status()
    question = response.json().get("data", {}).get("question")
    if not isinstance(question, dict):
        raise RuntimeError("LeetCode did not return authenticated question data.")
    return _question_evidence(question, challenge_id, metadata)


def _question_evidence(
    question: dict[str, Any],
    challenge_id: str,
    metadata: dict[str, Any],
) -> dict[str, Any]:
    slug = str(metadata.get("slug") or "")
    expected_frontend_id = str(metadata.get("frontend_id") or "")
    if str(question.get("questionFrontendId") or "") != expected_frontend_id:
        raise RuntimeError(
            "Authenticated question identity does not match canonical metadata "
            f"(expected={expected_frontend_id}, live={question.get('questionFrontendId')})."
        )
    if str(question.get("titleSlug") or "") != slug:
        raise RuntimeError("Authenticated question slug does not match canonical metadata.")

    content_html = str(question.get("content") or "")
    if not content_html:
        access_class = "Premium" if question.get("isPaidOnly") else "public"
        raise RuntimeError(
            f"LeetCode returned no {access_class} statement content for {challenge_id}."
        )

    return {
        "provider": "leetcode.com",
        "authenticated": True,
        "challenge_id": challenge_id,
        "question_id": str(question.get("questionId") or ""),
        "frontend_id": str(question.get("questionFrontendId") or ""),
        "title": str(question.get("title") or ""),
        "title_slug": str(question.get("titleSlug") or ""),
        "paid_only": bool(question.get("isPaidOnly")),
        "content_text": _statement_text(content_html),
        "content_html": content_html,
        "code_snippets": question.get("codeSnippets") or [],
    }


def fetch_question_via_chrome(
    challenge_id: str,
    credentials: LeetCodeCredentials,
) -> dict[str, Any]:
    metadata = leetcode_metadata(challenge_id)
    if not metadata:
        raise RuntimeError(f"No canonical metadata exists for {challenge_id}.")
    slug = str(metadata.get("slug") or "")
    if not slug:
        raise RuntimeError(f"Canonical metadata for {challenge_id} has no slug.")
    question = fetch_question_with_chrome(
        slug=slug,
        query=QUESTION_QUERY,
        session_cookie=credentials.session,
        csrf_token=credentials.csrf_token,
        clearance=credentials.cloudflare_clearance,
    )
    return _question_evidence(question, challenge_id, metadata)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("challenge_id", help="Canonical challenge id, for example lc_1902")
    args = parser.parse_args()
    if not re.fullmatch(r"lc_\d+", args.challenge_id):
        parser.error("challenge_id must use the lc_<frontend_id> form")

    try:
        credentials = credentials_from_environment()
        try:
            result = fetch_question(_session(credentials), args.challenge_id)
        except requests.RequestException:
            result = fetch_question_via_chrome(args.challenge_id, credentials)
    except (RuntimeError, requests.RequestException, ValueError, KeyError) as exc:
        print(f"Authenticated fetch failed: {exc}", file=sys.stderr)
        return 1

    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
