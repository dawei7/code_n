"""Browser-backed LeetCode submission fallback for Cloudflare-blocked POSTs."""
from __future__ import annotations

import asyncio
import json
import os
import subprocess
import tempfile
import time
from pathlib import Path
from typing import Any

import websockets


BASE_URL = "https://leetcode.com"
CHROME_USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/150.0.0.0 Safari/537.36"
)


def _chrome_path() -> Path:
    configured = os.environ.get("CODEN_CHROME", "").strip()
    candidates = [
        Path(configured) if configured else Path("__missing__"),
        Path(os.environ.get("PROGRAMFILES", "")) / "Google/Chrome/Application/chrome.exe",
        Path(os.environ.get("PROGRAMFILES(X86)", "")) / "Google/Chrome/Application/chrome.exe",
    ]
    for candidate in candidates:
        if candidate.is_file():
            return candidate
    raise RuntimeError("Google Chrome is required for the Cloudflare submission fallback.")


class _Cdp:
    def __init__(self, socket: Any):
        self.socket = socket
        self.next_id = 0

    async def call(self, method: str, params: dict[str, Any] | None = None, session_id: str | None = None) -> dict:
        self.next_id += 1
        message: dict[str, Any] = {"id": self.next_id, "method": method, "params": params or {}}
        if session_id:
            message["sessionId"] = session_id
        await self.socket.send(json.dumps(message))
        while True:
            response = json.loads(await self.socket.recv())
            if response.get("id") != self.next_id:
                continue
            if "error" in response:
                raise RuntimeError(f"Chrome DevTools error for {method}: {response['error']}")
            return response.get("result", {})


async def _evaluate(cdp: _Cdp, session_id: str, expression: str) -> Any:
    result = await cdp.call(
        "Runtime.evaluate",
        {"expression": expression, "awaitPromise": True, "returnByValue": True},
        session_id,
    )
    exception = result.get("exceptionDetails")
    if exception:
        raise RuntimeError(f"Chrome evaluation failed: {exception.get('text', 'unknown error')}")
    return result.get("result", {}).get("value")


async def _submit(
    websocket_url: str,
    *,
    slug: str,
    question_id: str,
    language: str,
    source: str,
    session_cookie: str,
    csrf_token: str,
    clearance: str,
) -> tuple[str, dict[str, Any]]:
    async with websockets.connect(websocket_url, proxy=None, max_size=4 * 1024 * 1024) as socket:
        cdp = _Cdp(socket)
        target = await cdp.call("Target.createTarget", {"url": f"{BASE_URL}/problems/{slug}/"})
        attached = await cdp.call("Target.attachToTarget", {"targetId": target["targetId"], "flatten": True})
        page = attached["sessionId"]
        await cdp.call("Network.enable", session_id=page)
        cookies = [
            {"name": "LEETCODE_SESSION", "value": session_cookie, "domain": ".leetcode.com", "path": "/", "secure": True},
            {"name": "csrftoken", "value": csrf_token, "domain": ".leetcode.com", "path": "/", "secure": True},
        ]
        if clearance:
            cookies.append({"name": "cf_clearance", "value": clearance, "domain": ".leetcode.com", "path": "/", "secure": True})
        await cdp.call("Network.setCookies", {"cookies": cookies}, page)
        await cdp.call("Emulation.setUserAgentOverride", {"userAgent": CHROME_USER_AGENT}, page)
        await cdp.call("Page.navigate", {"url": f"{BASE_URL}/problems/{slug}/"}, page)
        await asyncio.sleep(2)

        payload = json.dumps(
            {"question_id": question_id, "lang": language, "typed_code": source, "questionSlug": slug}
        )
        submit_expression = f"""
            fetch('/problems/{slug}/submit/', {{
              method: 'POST', credentials: 'include',
              headers: {{'Content-Type': 'application/json', 'x-csrftoken': {json.dumps(csrf_token)}}},
              body: {json.dumps(payload)}
            }}).then(async response => ({{status: response.status, text: await response.text()}}))
        """
        submitted = await _evaluate(cdp, page, submit_expression)
        if not isinstance(submitted, dict) or submitted.get("status") != 200:
            status = submitted.get("status") if isinstance(submitted, dict) else "unknown"
            raise RuntimeError(f"browser submit HTTP {status}")
        try:
            submission_id = str(json.loads(submitted["text"]).get("submission_id") or "")
        except (TypeError, json.JSONDecodeError) as exc:
            raise RuntimeError("Browser submission returned an invalid response.") from exc
        if not submission_id:
            raise RuntimeError("Browser submission returned no submission id.")

        result: dict[str, Any] = {}
        for _ in range(60):
            await asyncio.sleep(0.5)
            check_expression = f"fetch('/submissions/detail/{submission_id}/check/', {{credentials:'include'}}).then(async response => ({{status: response.status, text: await response.text()}}))"
            checked = await _evaluate(cdp, page, check_expression)
            if not isinstance(checked, dict) or checked.get("status") != 200:
                continue
            result = json.loads(checked["text"])
            if result.get("state") == "SUCCESS" or result.get("finished"):
                break
        return submission_id, result


def submit_with_chrome(**kwargs: str) -> tuple[str, dict[str, Any]]:
    with tempfile.TemporaryDirectory(prefix="coden-leetcode-chrome-") as temp:
        profile = Path(temp)
        process = subprocess.Popen(
            [
                str(_chrome_path()),
                "--headless=new",
                "--remote-debugging-port=0",
                "--remote-allow-origins=*",
                f"--user-data-dir={profile}",
                f"--user-agent={CHROME_USER_AGENT}",
                "--no-first-run",
                "--no-default-browser-check",
                "about:blank",
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        try:
            active_port = profile / "DevToolsActivePort"
            for _ in range(100):
                if active_port.is_file():
                    lines = active_port.read_text(encoding="utf-8").splitlines()
                    websocket_url = f"ws://127.0.0.1:{lines[0]}{lines[1]}"
                    return asyncio.run(_submit(websocket_url, **kwargs))
                if process.poll() is not None:
                    raise RuntimeError("Chrome exited before its verification session started.")
                time.sleep(0.05)
            raise RuntimeError("Timed out starting Chrome for LeetCode verification.")
        finally:
            process.terminate()
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
