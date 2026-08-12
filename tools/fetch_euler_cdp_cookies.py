"""Fetch active session cookies from Chrome CDP remote debugging port 9222."""

from __future__ import annotations

import asyncio
import json
import urllib.request
import websockets


def get_browser_ws_url() -> str:
    with urllib.request.urlopen("http://127.0.0.1:9222/json/version") as resp:
        data = json.loads(resp.read().decode("utf-8"))
        return data["webSocketDebuggerUrl"]


async def fetch_cdp_cookies() -> dict[str, str]:
    ws_url = get_browser_ws_url()
    async with websockets.connect(ws_url) as ws:
        # Get cookies
        req = {
            "id": 1,
            "method": "Storage.getCookies",
        }
        await ws.send(json.dumps(req))
        resp = await ws.recv()
        data = json.loads(resp)
        cookies = {}
        for c in data.get("result", {}).get("cookies", []):
            if "projecteuler.net" in c.get("domain", ""):
                cookies[c["name"]] = c["value"]
        return cookies


def main():
    print("Connecting to Chrome CDP at 127.0.0.1:9222...")
    try:
        cookies = asyncio.run(fetch_cdp_cookies())
        print(f"Found {len(cookies)} Project Euler cookies via CDP:")
        for k, v in cookies.items():
            print(f"  {k} = {v[:30]}..." if len(v) > 30 else f"  {k} = {v}")
        cookie_str = "; ".join(f"{k}={v}" for k, v in cookies.items())
        print("\nCookie string:")
        print(cookie_str)
    except Exception as err:
        print(f"Error fetching cookies via CDP: {err}")


if __name__ == "__main__":
    main()
