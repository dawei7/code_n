"""Secure desktop bridge for package-authored LeetCode submissions.

Credentials are supplied per call by Electron's OS-encrypted credential store.
They are never persisted by FastAPI, returned to the renderer, or logged.
"""
from __future__ import annotations

import hmac
import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests
from fastapi import APIRouter, Header, HTTPException
from pydantic import BaseModel

from server.app import progress_store
from server.app.challenge_packages import leetcode_submission_manifest_path


router = APIRouter(prefix="/leetcode")
_GRAPHQL_URL = "https://leetcode.com/graphql/"
_BASE_URL = "https://leetcode.com"
_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/150.0.0.0 Safari/537.36"
)


class LeetCodeCredentials(BaseModel):
    session: str
    csrf_token: str
    cloudflare_clearance: str = ""


class CredentialRequest(BaseModel):
    credentials: LeetCodeCredentials


def _require_desktop_bridge(token: str | None) -> None:
    expected = os.environ.get("CODEN_DESKTOP_BRIDGE_TOKEN", "")
    if expected and (not token or not hmac.compare_digest(token, expected)):
        raise HTTPException(status_code=403, detail="Desktop bridge authentication failed.")


def _manifest(challenge_id: str) -> tuple[dict[str, Any], Path | None]:
    path = leetcode_submission_manifest_path(challenge_id)
    if path is None or not path.is_file():
        return {}, path
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}, path
    return (payload if isinstance(payload, dict) else {}), path


def _availability(challenge_id: str) -> dict[str, Any]:
    manifest, path = _manifest(challenge_id)
    status = str(manifest.get("status") or "missing")
    source_path: Path | None = None
    if path is not None and manifest.get("source"):
        source_path = path.parent / str(manifest["source"])
    source_ready = bool(source_path and source_path.is_file())
    verified = status == "verified" and source_ready
    if not manifest:
        reason = "No reviewed LeetCode submission is packaged for this problem yet."
    elif status != "verified":
        reason = "The packaged LeetCode submission is awaiting acceptance verification."
    elif not source_ready:
        reason = "The verified LeetCode submission source is missing from this package."
    else:
        reason = ""
    return {
        "challenge_id": challenge_id,
        "available": verified,
        "status": status,
        "reason": reason,
        "title_slug": str(manifest.get("title_slug") or ""),
        "language": str(manifest.get("language") or ""),
        "paid_only": bool(manifest.get("paid_only", False)),
        "verified_at": manifest.get("verified_at"),
    }


def _session(credentials: LeetCodeCredentials) -> requests.Session:
    client = requests.Session()
    client.headers.update(
        {
            "User-Agent": _USER_AGENT,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": _BASE_URL,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }
    )
    client.cookies.set("LEETCODE_SESSION", credentials.session, domain="leetcode.com")
    client.cookies.set("csrftoken", credentials.csrf_token, domain="leetcode.com")
    if credentials.cloudflare_clearance:
        client.cookies.set("cf_clearance", credentials.cloudflare_clearance, domain="leetcode.com")
    return client


def _account_status(credentials: LeetCodeCredentials) -> dict[str, Any]:
    query = "query globalData { userStatus { isSignedIn username realName isPremium } }"
    try:
        response = _session(credentials).post(
            _GRAPHQL_URL,
            json={"query": query},
            headers={"Referer": f"{_BASE_URL}/"},
            timeout=20,
        )
    except requests.RequestException as exc:
        return {"state": "unreachable", "message": f"LeetCode could not be reached: {exc}"}
    if response.status_code in {401, 403}:
        return {
            "state": "blocked" if response.status_code == 403 else "expired",
            "message": "LeetCode rejected the session. Refresh the saved cookies and try again.",
        }
    try:
        user = response.json().get("data", {}).get("userStatus", {})
    except (ValueError, AttributeError):
        return {"state": "blocked", "message": "LeetCode returned a non-API response; Cloudflare clearance may need refreshing."}
    if not user.get("isSignedIn"):
        return {"state": "expired", "message": "The saved LeetCode session is expired or invalid."}
    return {
        "state": "valid",
        "message": "LeetCode session is ready.",
        "username": str(user.get("username") or ""),
        "real_name": str(user.get("realName") or ""),
        "is_premium": bool(user.get("isPremium")),
        "checked_at": datetime.now(timezone.utc).isoformat(),
    }


@router.get("/submissions/{challenge_id}/availability")
def submission_availability(challenge_id: str) -> dict[str, Any]:
    return _availability(challenge_id)


@router.post("/internal/session/status")
def session_status(
    body: CredentialRequest,
    x_coden_desktop_token: str | None = Header(default=None),
) -> dict[str, Any]:
    _require_desktop_bridge(x_coden_desktop_token)
    return _account_status(body.credentials)


@router.post("/internal/submissions/{challenge_id}")
def submit_verified_solution(
    challenge_id: str,
    body: CredentialRequest,
    x_coden_desktop_token: str | None = Header(default=None),
) -> dict[str, Any]:
    _require_desktop_bridge(x_coden_desktop_token)
    availability = _availability(challenge_id)
    if not availability["available"]:
        raise HTTPException(status_code=409, detail=availability["reason"])

    progress = progress_store.load()
    if challenge_id not in progress.completed:
        raise HTTPException(status_code=409, detail="Complete this problem successfully in cOde(n) before submitting.")

    account = _account_status(body.credentials)
    if account.get("state") != "valid":
        raise HTTPException(status_code=401, detail=account.get("message") or "LeetCode session is not valid.")
    if availability["paid_only"] and not account.get("is_premium"):
        raise HTTPException(status_code=403, detail="This is a LeetCode Premium problem and the connected account has no access.")

    manifest, manifest_path = _manifest(challenge_id)
    assert manifest_path is not None
    source_path = manifest_path.parent / str(manifest["source"])
    source = source_path.read_text(encoding="utf-8")
    slug = str(manifest["title_slug"])
    client = _session(body.credentials)
    headers = {
        "Referer": f"{_BASE_URL}/problems/{slug}/submissions/",
        "x-csrftoken": body.credentials.csrf_token,
        "Content-Type": "application/json",
    }
    payload = {
        "question_id": str(manifest["question_id"]),
        "lang": str(manifest["language"]),
        "typed_code": source,
        "questionSlug": slug,
    }
    try:
        response = client.post(
            f"{_BASE_URL}/problems/{slug}/submit/",
            json=payload,
            headers=headers,
            timeout=30,
        )
        response.raise_for_status()
        submission_id = str(response.json().get("submission_id") or "")
    except (requests.RequestException, ValueError) as exc:
        raise HTTPException(status_code=502, detail=f"LeetCode submission request failed: {exc}") from exc
    if not submission_id:
        raise HTTPException(status_code=502, detail="LeetCode did not return a submission ID.")

    result: dict[str, Any] = {}
    for _ in range(60):
        time.sleep(0.5)
        try:
            check = client.get(
                f"{_BASE_URL}/submissions/detail/{submission_id}/check/",
                headers={"Referer": f"{_BASE_URL}/problems/{slug}/submissions/"},
                timeout=20,
            )
            check.raise_for_status()
            result = check.json()
        except (requests.RequestException, ValueError) as exc:
            raise HTTPException(status_code=502, detail=f"LeetCode result check failed: {exc}") from exc
        if result.get("state") == "SUCCESS" or result.get("finished"):
            break
    else:
        raise HTTPException(status_code=504, detail=f"LeetCode submission {submission_id} is still being judged.")

    status = str(result.get("status_msg") or result.get("state") or "Unknown")
    accepted = status == "Accepted" or result.get("status_code") == 10
    if accepted:
        accepted_at = datetime.now(timezone.utc).isoformat()
        progress.leetcode_submissions[challenge_id] = {
            "submission_id": submission_id,
            "accepted_at": accepted_at,
            "language": str(manifest["language"]),
            "status": "Accepted",
        }
        progress_store.save(progress)
    return {
        "accepted": accepted,
        "status": status,
        "submission_id": submission_id,
        "runtime": result.get("status_runtime") or result.get("runtime"),
        "memory": result.get("status_memory") or result.get("memory"),
        "message": "Accepted by LeetCode." if accepted else f"LeetCode returned: {status}.",
    }
