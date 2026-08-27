"""Direct session-based Project Euler answer submitter.

Policy:
1. Submits answers purely via direct HTTP session cookies (headless).
2. If Project Euler requests a Captcha / Confirmation Code, it pauses and prompts
   the user to resolve/enter the code manually, never attempting automated bypass.
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import os
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent.parent
EULER_ROOT = REPO_ROOT / "dsa" / "euler"
REPORT_FILE = EULER_ROOT / "_reports" / "_submission_progress.json"

DEFAULT_COOKIES = {
    "__Host-PHPSESSID": "0ac3134f7ed5e031ec7cf7fa9e8fd8d4",
    "keep_alive": "1786817720%232086399%23jq0YJWDzvmqtddZajUDdr770b8cKaMdd",
}


def get_cookie_header(cookies: dict[str, str] | None = None) -> str:
    c = cookies or DEFAULT_COOKIES
    return "; ".join(f"{k}={v}" for k, v in c.items())


def compute_solution_answer(pkg_dir: Path) -> Any:
    sol_candidates = [
        pkg_dir / "variants" / "optimal" / "solutions" / "solution.py",
        pkg_dir / "variants" / "optimal" / "solution.py",
        pkg_dir / "solution.py",
    ]
    sol_file = next((f for f in sol_candidates if f.is_file()), None)
    if not sol_file:
        raise FileNotFoundError(f"No solution.py found in {pkg_dir.name}")

    spec = importlib.util.spec_from_file_location(f"euler_{pkg_dir.name}", sol_file)
    if not spec or not spec.loader:
        raise RuntimeError(f"Could not load module {sol_file}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)

    if hasattr(mod, "solve") and callable(mod.solve):
        return mod.solve()
    elif hasattr(mod, "Solution"):
        sol_inst = mod.Solution()
        methods = [getattr(sol_inst, m) for m in dir(sol_inst) if not m.startswith("_") and callable(getattr(sol_inst, m))]
        if methods:
            return methods[0]()
    raise RuntimeError(f"No solve() function in {sol_file}")


def submit_euler_problem(problem_num: int, captcha_code: str | None = None, cookies: dict[str, str] | None = None) -> dict[str, Any]:
    cookie_str = get_cookie_header(cookies)
    get_url = f"https://projecteuler.net/problem={problem_num}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36",
        "Cookie": cookie_str,
    }

    req = urllib.request.Request(get_url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            html = resp.read().decode("utf-8")
    except Exception as e:
        return {"status": "error", "problem": problem_num, "message": f"HTTP GET error: {e}"}

    # 1. Check if already solved
    if "You are confirmed to have solved this problem" in html or "class=\"problem_solved\"" in html:
        return {"status": "already_solved", "problem": problem_num}

    # 2. Check if signed in
    if "Signed in as" not in html and "sign_out" not in html:
        return {"status": "error", "problem": problem_num, "message": "Session cookies expired or invalid (not signed in)"}

    # 3. Find problem package & compute answer
    pkg_candidates = list(EULER_ROOT.glob(f"{problem_num:04d}_*"))
    if not pkg_candidates:
        return {"status": "error", "problem": problem_num, "message": f"Package {problem_num:04d} not found locally"}
    
    pkg_dir = pkg_candidates[0]
    try:
        ans = compute_solution_answer(pkg_dir)
    except Exception as e:
        return {"status": "error", "problem": problem_num, "message": f"Error computing solution: {e}"}

    # 4. Extract CSRF token from the answer form
    form_m = re.search(r'<form name=["\']form["\'][^>]*>(.*?)</form>', html, re.DOTALL)
    if not form_m:
        return {"status": "error", "problem": problem_num, "message": "Could not find answer submission form"}

    form_html = form_m.group(1)
    csrf_m = re.search(r'<input type=["\']hidden["\'] name=["\']csrf_token["\'] value=["\']([^"\']+)["\']', form_html)
    if not csrf_m:
        return {"status": "error", "problem": problem_num, "message": "Could not extract csrf_token from form"}

    csrf_token = csrf_m.group(1)

    # 5. Check if Captcha is required
    requires_captcha = 'name="captcha"' in form_html or 'id="captcha"' in form_html
    if requires_captcha and not captcha_code:
        # Download captcha image for user review
        captcha_img_url = "https://projecteuler.net/captcha/show_captcha.php"
        img_req = urllib.request.Request(captcha_img_url, headers=headers)
        captcha_path = Path("scratch/current_captcha.png")
        try:
            captcha_path.parent.mkdir(parents=True, exist_ok=True)
            with urllib.request.urlopen(img_req, timeout=10) as img_resp:
                captcha_path.write_bytes(img_resp.read())
        except Exception:
            pass

        return {
            "status": "captcha_required",
            "problem": problem_num,
            "answer": str(ans),
            "captcha_image": str(captcha_path),
            "message": f"Problem {problem_num} requires confirmation code. Captcha saved to {captcha_path}",
        }

    # 6. POST answer
    post_data = {
        f"guess_{problem_num}": str(ans),
        "csrf_token": csrf_token,
    }
    if requires_captcha and captcha_code:
        post_data["captcha"] = str(captcha_code).strip()

    encoded_data = urllib.parse.urlencode(post_data).encode("utf-8")

    post_headers = dict(headers)
    post_headers["Referer"] = get_url
    post_headers["Content-Type"] = "application/x-www-form-urlencoded"

    post_req = urllib.request.Request(get_url, data=encoded_data, headers=post_headers)
    try:
        with urllib.request.urlopen(post_req, timeout=10) as resp:
            resp_html = resp.read().decode("utf-8")
    except Exception as e:
        return {"status": "error", "problem": problem_num, "message": f"HTTP POST error: {e}"}

    if "Congratulations, the answer you gave to problem" in resp_html:
        return {"status": "accepted", "problem": problem_num, "answer": str(ans)}
    elif "Sorry, but the answer you gave appears to be incorrect" in resp_html:
        return {"status": "incorrect", "problem": problem_num, "answer": str(ans)}
    else:
        msg_m = re.search(r'<div id=["\']message["\'][^>]*>(.*?)</div>', resp_html, re.DOTALL)
        msg = msg_m.group(1).strip() if msg_m else "Unknown response status"
        return {"status": "response", "problem": problem_num, "message": msg, "answer": str(ans)}


def load_progress() -> dict[str, Any]:
    if REPORT_FILE.is_file():
        try:
            return json.loads(REPORT_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"accepted": [], "last_updated": None}


def save_progress(accepted: list[int]) -> None:
    REPORT_FILE.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "accepted": sorted(list(set(accepted))),
        "accepted_count": len(accepted),
        "last_updated": datetime.now(timezone.utc).isoformat(),
    }
    REPORT_FILE.write_text(json.dumps(payload, indent=2), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Direct headless session-only Project Euler submitter")
    parser.add_argument("--problem", type=int, help="Single problem number to submit")
    parser.add_argument("--captcha", type=str, help="User-provided confirmation code if required")
    parser.add_argument("--range", type=int, nargs=2, metavar=("START", "END"), help="Range of problem numbers to submit")
    parser.add_argument("--delay", type=float, default=1.0, help="Delay in seconds between submissions")
    args = parser.parse_args()

    progress = load_progress()
    accepted = set(progress.get("accepted", []))

    if args.problem:
        res = submit_euler_problem(args.problem, captcha_code=args.captcha)
        print(f"Problem {args.problem}: {res}")
        if res.get("status") in ("accepted", "already_solved"):
            accepted.add(args.problem)
            save_progress(list(accepted))
        return

    start_num, end_num = (1, 100) if not args.range else (args.range[0], args.range[1])
    print(f"Starting direct session submission for Euler problems {start_num} to {end_num}...")

    for p in range(start_num, end_num + 1):
        res = submit_euler_problem(p)
        status = res.get("status")
        ans_str = f" [answer: {res.get('answer')}]" if "answer" in res else ""
        print(f"[{p:04d}] {status.upper()}{ans_str} {res.get('message', '')}")
        
        if status in ("accepted", "already_solved"):
            accepted.add(p)
            save_progress(list(accepted))
        elif status == "captcha_required":
            print(f"\n>> CAPTCHA REQUIRED for Problem {p}! Pausing so user can resolve manually.")
            print(f"   Answer is: {res.get('answer')}")
            break

        time.sleep(args.delay)

    print(f"\nRun ended. Total accepted problems tracked: {len(accepted)}")


if __name__ == "__main__":
    main()
