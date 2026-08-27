"""Batch submit all canonical LeetCode optimal solutions to the live LeetCode judge.

Paces submissions with conservative pacing (default 10s) to respect LeetCode Nginx
rate limits, uses GraphQL questionId mapping for 100% accurate backend IDs, logs
results to a persistent JSONL ledger, updates submission.json on Accepted verdicts,
and generates a live Markdown report of all invalid submissions for debugging.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from server.app.challenge_packages import (  # noqa: E402
    leetcode_metadata,
    leetcode_package_dir,
)

COOKIE_PATH = ROOT / "dsa" / "leetcode" / "_local" / ".leetcode_cookie"
RESULTS_JSONL = ROOT / "dsa" / "leetcode" / "_reports" / "batch_validation_results.jsonl"
INVALID_REPORT_MD = ROOT / "dsa" / "leetcode" / "_reports" / "invalid_submissions_report.md"
DEFAULT_DELAY_SECONDS = 10.0
DEFAULT_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/150.0.0.0 Safari/537.36"
)
BASE_URL = "https://leetcode.com"


def _cookie_header() -> str:
    raw = os.environ.get("LEETCODE_COOKIE", "").strip()
    if raw:
        return raw
    if COOKIE_PATH.is_file():
        return COOKIE_PATH.read_text(encoding="utf-8").strip()
    session = os.environ.get("LEETCODE_SESSION", "").strip()
    csrf = os.environ.get("LEETCODE_CSRF_TOKEN", "").strip()
    if session and csrf:
        return f"LEETCODE_SESSION={session}; csrftoken={csrf}"
    return ""


def _csrf_from_cookie(cookie: str) -> str:
    env = os.environ.get("LEETCODE_CSRF_TOKEN", "").strip()
    if env:
        return env
    match = re.search(r"(?:^|;\s*)csrftoken=([^;]+)", cookie)
    return match.group(1) if match else ""


def _session_cookie_from_cookie(cookie: str) -> str:
    match = re.search(r"(?:^|;\s*)LEETCODE_SESSION=([^;]+)", cookie)
    return match.group(1) if match else ""


def _cf_clearance_from_cookie(cookie: str) -> str:
    match = re.search(r"(?:^|;\s*)cf_clearance=([^;]+)", cookie)
    return match.group(1) if match else ""


def _session(cookie: str = "") -> requests.Session:
    session = requests.Session()
    user_agent = os.environ.get("LEETCODE_USER_AGENT", "").strip() or DEFAULT_USER_AGENT
    session.headers.update(
        {
            "User-Agent": user_agent,
            "Accept": "application/json, text/plain, */*",
            "Accept-Language": "en-US,en;q=0.9",
            "Origin": BASE_URL,
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
        }
    )
    if cookie:
        session.headers["Cookie"] = cookie
    return session


def fetch_all_backend_question_ids(session: requests.Session) -> dict[str, str]:
    """Fetch mapping of slug -> backend questionId from LeetCode GraphQL."""
    query = "query { allQuestions { questionId questionFrontendId titleSlug } }"
    try:
        resp = session.post(
            f"{BASE_URL}/graphql/",
            json={"query": query},
            headers={"Referer": f"{BASE_URL}/problems/"},
            timeout=25,
        )
        if resp.status_code == 200:
            data = resp.json().get("data", {}).get("allQuestions", [])
            mapping = {str(item["titleSlug"]): str(item["questionId"]) for item in data if "titleSlug" in item and "questionId" in item}
            print(f"Successfully loaded {len(mapping)} official LeetCode question IDs from GraphQL.", flush=True)
            return mapping
    except Exception as exc:
        print(f"Warning: could not fetch GraphQL question mapping: {exc}", flush=True)
    return {}


def _load_all_packages() -> list[tuple[int, str, Path]]:
    """Return sorted list of (frontend_id_num, package_name, package_path)."""
    leetcode_dir = ROOT / "dsa" / "leetcode"
    packages: list[tuple[int, str, Path]] = []
    for entry in leetcode_dir.iterdir():
        if not entry.is_dir() or entry.name.startswith("_"):
            continue
        prefix = entry.name.split("_")[0]
        try:
            num = int(prefix)
        except ValueError:
            continue
        packages.append((num, entry.name, entry))
    packages.sort(key=lambda x: x[0])
    return packages


def _load_package_submission_target(
    package_dir: Path,
    question_id_map: dict[str, str],
) -> dict[str, Any] | None:
    manifest_path = package_dir / "variants" / "optimal" / "submission.json"
    meta_path = package_dir / "metadata.json"
    meta = json.loads(meta_path.read_text(encoding="utf-8")) if meta_path.is_file() else {}

    frontend_id = str(meta.get("frontend_id") or package_dir.name.split("_")[0].lstrip("0") or "0")
    title_slug = str(meta.get("slug") or meta.get("title_slug") or package_dir.name.split("_", 1)[1])
    
    # Priority: GraphQL official backend ID > manifest question_id > metadata question_id
    qid = question_id_map.get(title_slug) or str(meta.get("question_id") or frontend_id)

    if not manifest_path.is_file():
        category = meta.get("category", "algorithms")
        lang = {
            "database": "postgresql",
            "shell": "bash",
            "javascript": "javascript",
            "pandas": "pythondata",
        }.get(category, "python3")
        opt_dir = package_dir / "variants" / "optimal"
        ext_map = {"postgresql": ".sql", "mysql": ".sql", "bash": ".sh", "javascript": ".js", "python3": ".py", "python": ".py", "pythondata": ".py"}
        expected_ext = ext_map.get(lang, ".py")
        sol_file = opt_dir / f"solution{expected_ext}"
        if not sol_file.is_file():
            sols = list(opt_dir.glob("solution.*")) + list((opt_dir / "solutions").glob("solution.*"))
            if sols:
                sol_file = sols[0]
                if category == "pandas":
                    lang = "pythondata"
                else:
                    lang = {".sql": "postgresql", ".sh": "bash", ".js": "javascript", ".py": "python3"}.get(sol_file.suffix, "python3")
            else:
                return None
        return {
            "question_id": qid,
            "frontend_id": frontend_id,
            "title_slug": title_slug,
            "language": lang,
            "source_path": sol_file,
            "manifest_path": manifest_path,
        }

    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    source_name = str(manifest.get("source") or "solution.py")
    source_path = manifest_path.parent / source_name
    if not source_path.is_file():
        source_path = manifest_path.parent / "solutions" / source_name
        if not source_path.is_file():
            return None
    
    # Use official GraphQL qid if available, otherwise manifest qid
    final_qid = question_id_map.get(str(manifest.get("title_slug") or title_slug)) or str(manifest.get("question_id") or qid)

    raw_lang = str(manifest.get("language") or "python3")
    if raw_lang == "python":
        raw_lang = "python3"
    if meta.get("category") == "pandas" or raw_lang in ("pandas", "pythondata"):
        raw_lang = "pythondata"
    elif raw_lang in ("mysql", "postgresql") or source_path.suffix == ".sql":
        if raw_lang not in ("mysql", "postgresql", "mssql", "oraclesql"):
            raw_lang = "postgresql"

    return {
        "question_id": final_qid,
        "frontend_id": str(manifest.get("frontend_id") or frontend_id),
        "title_slug": str(manifest.get("title_slug") or title_slug),
        "language": raw_lang,
        "source_path": source_path,
        "manifest_path": manifest_path,
    }


def _load_previous_results() -> dict[str, dict[str, Any]]:
    """Load previously recorded results keyed by frontend_id."""
    results: dict[str, dict[str, Any]] = {}
    if not RESULTS_JSONL.is_file():
        return results
    for line in RESULTS_JSONL.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            record = json.loads(line)
            fid = str(record.get("frontend_id") or "")
            if fid:
                results[fid] = record
        except json.JSONDecodeError:
            continue
    return results


def append_result(record: dict[str, Any]) -> None:
    RESULTS_JSONL.parent.mkdir(parents=True, exist_ok=True)
    with RESULTS_JSONL.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False, sort_keys=True) + "\n")


def generate_invalid_report() -> None:
    """Generate Markdown report summarizing all invalid/failed submissions."""
    if not RESULTS_JSONL.is_file():
        return

    records_by_id: dict[str, dict[str, Any]] = {}
    for line in RESULTS_JSONL.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
            fid = str(rec.get("frontend_id") or "")
            if fid:
                records_by_id[fid] = rec
        except json.JSONDecodeError:
            continue

    total_submitted = len(records_by_id)
    accepted_records: list[dict[str, Any]] = []
    invalid_records: list[dict[str, Any]] = []

    for fid in sorted(records_by_id.keys(), key=lambda x: int(x) if x.isdigit() else 999999):
        rec = records_by_id[fid]
        if rec.get("accepted"):
            accepted_records.append(rec)
        else:
            invalid_records.append(rec)

    verdict_counter = Counter(r.get("verdict_status", "Unknown") for r in records_by_id.values())

    lines: list[str] = [
        "# LeetCode Batch Submission & Validation Report",
        "",
        f"- **Generated At**: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}",
        f"- **Total Problems Tested**: {total_submitted}",
        f"- **Accepted**: {len(accepted_records)} ({len(accepted_records)/max(1, total_submitted)*100:.1f}%)",
        f"- **Invalid / Failed**: {len(invalid_records)} ({len(invalid_records)/max(1, total_submitted)*100:.1f}%)",
        "",
        "## Verdict Distribution",
        "",
        "| Verdict | Count | Share |",
        "|---|---|---|",
    ]

    for verdict, count in verdict_counter.most_common():
        lines.append(f"| {verdict} | {count} | {count/max(1, total_submitted)*100:.1f}% |")

    lines.extend([
        "",
        f"## Invalid Submissions Queue ({len(invalid_records)} problems to fix)",
        "",
    ])

    if not invalid_records:
        lines.append("🎉 **All tested solutions are valid and Accepted by LeetCode!**\n")
    else:
        lines.append("| # | Frontend ID | Slug | Language | Verdict | Details |")
        lines.append("|---|---|---|---|---|---|")
        for i, rec in enumerate(invalid_records, 1):
            fid = rec.get("frontend_id", "")
            slug = rec.get("title_slug", "")
            lang = rec.get("language", "")
            verdict = rec.get("verdict_status", "Unknown")
            details = rec.get("error_summary", "").replace("\n", " ").replace("|", "\\|")[:120]
            lines.append(f"| {i} | [{fid}](https://leetcode.com/problems/{slug}/) | `{slug}` | `{lang}` | **{verdict}** | {details} |")

        lines.extend([
            "",
            "## Detailed Failure Logs",
            "",
        ])

        for rec in invalid_records:
            fid = rec.get("frontend_id", "")
            slug = rec.get("title_slug", "")
            lang = rec.get("language", "")
            verdict = rec.get("verdict_status", "Unknown")
            sub_id = rec.get("submission_id", "N/A")
            raw_verdict = rec.get("verdict_raw", {})

            lines.extend([
                f"### Problem {fid}: {slug}",
                f"- **Language**: `{lang}`",
                f"- **Verdict**: **{verdict}**",
                f"- **Submission ID**: `{sub_id}`",
                f"- **LeetCode URL**: https://leetcode.com/problems/{slug}/",
            ])

            if rec.get("error"):
                lines.extend(["```text", f"Error: {rec['error']}", "```", ""])
            elif raw_verdict:
                if raw_verdict.get("compile_error"):
                    lines.extend(["**Compile Error:**", "```text", str(raw_verdict["compile_error"]), "```", ""])
                if raw_verdict.get("runtime_error"):
                    lines.extend(["**Runtime Error:**", "```text", str(raw_verdict["runtime_error"]), "```", ""])
                if raw_verdict.get("last_testcase"):
                    lines.extend([
                        "**Failed Testcase Input:**",
                        "```text",
                        str(raw_verdict["last_testcase"]),
                        "```",
                        f"- **Expected Output**: `{raw_verdict.get('expected_output', '')}`",
                        f"- **Actual Output**: `{raw_verdict.get('code_output', '')}`",
                        "",
                    ])

    INVALID_REPORT_MD.parent.mkdir(parents=True, exist_ok=True)
    INVALID_REPORT_MD.write_text("\n".join(lines) + "\n", encoding="utf-8")


def submit_problem(
    target: dict[str, Any],
    session: requests.Session,
    csrf_token: str,
    session_cookie: str,
    cf_clearance: str,
    poll_timeout: float = 60.0,
) -> dict[str, Any]:
    slug = target["title_slug"]
    qid = target["question_id"]
    lang = target["language"]
    source_code = target["source_path"].read_text(encoding="utf-8")

    headers = {
        "Referer": f"{BASE_URL}/problems/{slug}/submissions/",
        "x-csrftoken": csrf_token,
        "Content-Type": "application/json",
        "Origin": BASE_URL,
    }
    payload = {
        "question_id": str(qid),
        "lang": lang,
        "typed_code": source_code,
        "questionSlug": slug,
    }

    submit_url = f"{BASE_URL}/problems/{slug}/submit/"
    submission_id = ""
    result: dict[str, Any] = {}

    rate_limit_cooldown = 120.0
    while True:
        try:
            response = session.post(submit_url, json=payload, headers=headers, timeout=30)
            if response.status_code == 429:
                print(f"\n[HTTP 429 Rate limited by LeetCode. Pausing {rate_limit_cooldown}s for rate-limiter bucket cooldown on {slug}...]", flush=True)
                time.sleep(rate_limit_cooldown)
                rate_limit_cooldown = min(rate_limit_cooldown * 1.5, 300.0)
                continue
            rate_limit_cooldown = 120.0
            if response.status_code == 403:
                return {
                    "accepted": False,
                    "submission_id": "",
                    "verdict_status": "HTTP 403 Blocked",
                    "error": "HTTP 403 Cloudflare block: session or csrf token expired or blocked",
                }
            elif response.status_code >= 400:
                return {
                    "accepted": False,
                    "submission_id": "",
                    "verdict_status": f"HTTP {response.status_code}",
                    "error": f"Submit returned status {response.status_code}: {response.text[:300]}",
                }
            else:
                data = response.json()
                submission_id = str(data.get("submission_id") or "")
                if not submission_id:
                    return {
                        "accepted": False,
                        "submission_id": "",
                        "verdict_status": "No Submission ID",
                        "error": f"Response lacked submission_id: {data}",
                    }
                break
        except Exception as exc:
            print(f"\n[Network exception submitting {slug}: {exc}. Retrying in 10s...]", flush=True)
            time.sleep(10.0)

    if not submission_id and not result:
        return {
            "accepted": False,
            "submission_id": "",
            "verdict_status": "Submit Failed",
            "error": "Failed to obtain submission_id",
        }

    # Poll for result if not already obtained
    if not result:
        deadline = time.monotonic() + poll_timeout
        check_url = f"{BASE_URL}/submissions/detail/{submission_id}/check/"
        while time.monotonic() < deadline:
            time.sleep(0.8)
            try:
                check_resp = session.get(
                    check_url,
                    headers={"Referer": f"{BASE_URL}/problems/{slug}/submissions/"},
                    timeout=20,
                )
                if check_resp.status_code == 200:
                    result = check_resp.json()
                    if result.get("state") == "SUCCESS" or result.get("finished"):
                        break
            except Exception:
                continue
        else:
            return {
                "accepted": False,
                "submission_id": submission_id,
                "verdict_status": "Judge Timeout",
                "error": f"Timed out polling submission {submission_id}",
            }

    status_msg = str(result.get("status_msg") or result.get("state") or "Unknown")
    status_code = result.get("status_code")
    accepted = status_msg == "Accepted" or status_code == 10


    error_summary = ""
    if not accepted:
        if result.get("compile_error"):
            error_summary = f"Compile Error: {result.get('compile_error')}"[:200]
        elif result.get("runtime_error"):
            error_summary = f"Runtime Error: {result.get('runtime_error')}"[:200]
        elif result.get("last_testcase"):
            error_summary = f"WA on testcase: input={result.get('last_testcase', '')[:60]}, expected={result.get('expected_output', '')[:40]}, actual={result.get('code_output', '')[:40]}"
        else:
            error_summary = status_msg

    return {
        "accepted": accepted,
        "submission_id": submission_id,
        "verdict_status": status_msg,
        "runtime": result.get("status_runtime") or result.get("runtime"),
        "memory": result.get("status_memory") or result.get("memory"),
        "total_correct": result.get("total_correct"),
        "total_testcases": result.get("total_testcases"),
        "error_summary": error_summary,
        "verdict_raw": result,
    }


def update_manifest_on_accepted(target: dict[str, Any], submission_id: str) -> None:
    manifest_path: Path = target["manifest_path"]
    if not manifest_path.is_file():
        payload = {
            "schema_version": 1,
            "provider": "leetcode.com",
            "status": "verified",
            "question_id": target["question_id"],
            "frontend_id": target["frontend_id"],
            "title_slug": target["title_slug"],
            "paid_only": False,
            "language": target["language"],
            "source": target["source_path"].name,
            "verified_submission_id": submission_id,
            "verified_at": datetime.now(timezone.utc).isoformat(),
        }
        manifest_path.parent.mkdir(parents=True, exist_ok=True)
        manifest_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return

    try:
        payload = json.loads(manifest_path.read_text(encoding="utf-8"))
        payload["status"] = "verified"
        payload["verified_submission_id"] = submission_id
        payload["verified_at"] = datetime.now(timezone.utc).isoformat()
        manifest_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except Exception as exc:
        print(f"Warning: could not update manifest at {manifest_path}: {exc}", flush=True)


def main() -> None:
    parser = argparse.ArgumentParser(description="Submit LeetCode optimal solutions with pacing and reporting.")
    parser.add_argument("--delay", type=float, default=DEFAULT_DELAY_SECONDS, help="Delay in seconds after each submission (default: 10.0)")
    parser.add_argument("--start-id", type=int, default=1, help="Start frontend ID (inclusive)")
    parser.add_argument("--end-id", type=int, default=4005, help="End frontend ID (inclusive)")
    parser.add_argument("--limit", type=int, default=None, help="Maximum number of packages to process")
    parser.add_argument("--ids", nargs="+", help="Specific challenge IDs, e.g. lc_1 lc_2 or numeric 1 2")
    parser.add_argument("--skip-accepted", action="store_true", help="Skip problems already marked as Accepted in previous ledger")
    parser.add_argument("--retry-failed", action="store_true", help="Only process problems that previously failed or errored")
    parser.add_argument("--resubmit-mysql-and-failed", action="store_true", help="Resubmit all problems that failed or were previously submitted as MySQL")
    parser.add_argument("--dry-run", action="store_true", help="Inspect and validate targets without submitting to LeetCode")
    parser.add_argument("--no-manifest-update", action="store_true", help="Do not update submission.json files on Accepted")
    args = parser.parse_args()

    cookie = _cookie_header()
    csrf = _csrf_from_cookie(cookie)
    session_val = _session_cookie_from_cookie(cookie)
    cf_val = _cf_clearance_from_cookie(cookie)

    if not args.dry_run and (not cookie or not csrf):
        raise SystemExit(
            "LeetCode credentials missing. Ensure dsa/leetcode/_local/.leetcode_cookie or "
            "LEETCODE_COOKIE/LEETCODE_SESSION environment variables are set."
        )

    session = _session(cookie) if not args.dry_run else None
    question_id_map: dict[str, str] = {}
    if session:
        question_id_map = fetch_all_backend_question_ids(session)

    all_packages = _load_all_packages()
    previous_results = _load_previous_results()

    # Filter packages
    selected: list[tuple[int, str, Path]] = []
    if args.ids:
        id_set = {i.removeprefix("lc_") for i in args.ids}
        for num, name, path in all_packages:
            if str(num) in id_set:
                selected.append((num, name, path))
    else:
        for num, name, path in all_packages:
            if args.start_id <= num <= args.end_id:
                selected.append((num, name, path))

    if args.skip_accepted:
        selected = [p for p in selected if not previous_results.get(str(p[0]), {}).get("accepted")]

    if args.retry_failed:
        selected = [
            p for p in selected
            if str(p[0]) in previous_results and not previous_results[str(p[0])].get("accepted")
        ]

    if args.resubmit_mysql_and_failed:
        selected = [
            p for p in selected
            if str(p[0]) in previous_results and (
                not previous_results[str(p[0])].get("accepted") or
                previous_results[str(p[0])].get("language") == "mysql"
            )
        ]

    if args.limit:
        selected = selected[: args.limit]

    print(f"Selected {len(selected)} problem package(s) for execution (Delay: {args.delay}s).", flush=True)
    if args.dry_run:
        print("[DRY RUN MODE] No requests will be sent to LeetCode.\n", flush=True)

    success_count = 0
    fail_count = 0

    for idx, (num, name, package_dir) in enumerate(selected, 1):
        target = _load_package_submission_target(package_dir, question_id_map)
        if target is None:
            print(f"[{idx}/{len(selected)}] Problem {num} ({name}): No valid optimal submission target found! Skipping.", flush=True)
            fail_count += 1
            continue

        fid = target["frontend_id"]
        slug = target["title_slug"]
        lang = target["language"]
        src_path = target["source_path"]

        if args.dry_run:
            print(f"[{idx}/{len(selected)}] [DRY-RUN] Problem {fid} ({slug}) [QID: {target['question_id']}] | Lang: {lang} | Source: {src_path.relative_to(ROOT)}")
            continue

        print(f"[{idx}/{len(selected)}] Submitting Problem {fid}: {slug} [QID: {target['question_id']}] ({lang})...", end=" ", flush=True)
        assert session is not None
        t_start = time.monotonic()
        res = submit_problem(target, session, csrf, session_val, cf_val)
        elapsed = time.monotonic() - t_start

        accepted = res.get("accepted", False)
        verdict = res.get("verdict_status", "Unknown")
        sub_id = res.get("submission_id", "")

        record = {
            "frontend_id": fid,
            "title_slug": slug,
            "language": lang,
            "source_path": str(src_path.relative_to(ROOT)),
            "submission_id": sub_id,
            "accepted": accepted,
            "verdict_status": verdict,
            "runtime": res.get("runtime"),
            "memory": res.get("memory"),
            "total_correct": res.get("total_correct"),
            "total_testcases": res.get("total_testcases"),
            "error_summary": res.get("error_summary", ""),
            "error": res.get("error", ""),
            "verdict_raw": res.get("verdict_raw", {}),
            "submitted_at": datetime.now(timezone.utc).isoformat(),
        }

        append_result(record)
        generate_invalid_report()

        if accepted:
            success_count += 1
            print(f"ACCEPTED! (ID: {sub_id}, {res.get('runtime', '')} {res.get('memory', '')})", flush=True)
            if not args.no_manifest_update:
                update_manifest_on_accepted(target, sub_id)
        else:
            fail_count += 1
            print(f"NOT ACCEPTED ({verdict}) -> {res.get('error_summary', res.get('error', ''))[:80]}", flush=True)

        # Enforce exact delay requested
        if idx < len(selected) and args.delay > 0:
            time.sleep(args.delay)

    print("\n" + "=" * 60)
    print(f"Batch completed! Total: {len(selected)} | Accepted: {success_count} | Failed/Invalid: {fail_count}")
    print(f"Full ledger saved to: {RESULTS_JSONL.relative_to(ROOT)}")
    print(f"Invalid submissions report: {INVALID_REPORT_MD.relative_to(ROOT)}")
    print("=" * 60, flush=True)


if __name__ == "__main__":
    main()
