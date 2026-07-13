"""Clean up old cOde(n) GitHub release assets to save space.

By default, every GitHub Release keeps its own copy of every
asset (NSIS installer + blockmap + latest.yml = ~95 MB per
release). For a fast-moving project, that adds up fast.

This script walks all releases, identifies the most recent
published one (the "latest" in the sense that GitHub's
Releases API returns them sorted by created_at desc), and
deletes the assets of every older release. The release
*entries* themselves are kept (so the version history is
visible), but the installers and blockmaps for old versions
are gone. Saves ~95 MB per old release.

The cleanup is a one-way operation. The current release
that's already installed on users' machines can no longer
auto-update past the LATEST version (which is correct: they
need to install the newest version directly).

Usage:
    # dry run - show what would be deleted
    .venv/Scripts/python.exe release_cleanup.py --dry-run

    # actually delete old release assets (default: only
    # releases older than the most recent one)
    .venv/Scripts/python.exe release_cleanup.py --yes

    # delete assets of ALL releases older than the given tag
    .venv/Scripts/python.exe release_cleanup.py --keep v0.5.0 --yes

    # delete the assets of just one specific release
    .venv/Scripts/python.exe release_cleanup.py --only v0.4.0 --yes

    # also delete the old RELEASE (not just assets); keeps
    # only the entry's name visible in the Releases page
    .venv/Scripts/python.py release_cleanup.py --yes --delete-releases

Prereqs:
    - $GH_TOKEN must be set (in the shell, or in electron/.env).
      The token needs ``Contents: read and write`` on
      ``dawei7/code_n``.

Idempotent: re-running after a successful cleanup is a no-op
(there are no old assets to delete). Safe to wire into
``release.py`` via the ``--cleanup-old`` flag.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path
from typing import Optional

import urllib.error
import urllib.request
import json


REPO = "dawei7/code_n"
API_BASE = "https://api.github.com"


def _get_token() -> str:
    """Pull GH_TOKEN from the environment, falling back to
    the value in ``electron/.env`` (without the surrounding
    shell-export shenanigans). Returns the empty string if
    not found, which makes API calls fail with a clear error.
    """
    token = os.environ.get("GH_TOKEN")
    if token:
        return token
    env_file = Path("electron") / ".env"
    if env_file.is_file():
        for line in env_file.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if line.startswith("GH_TOKEN="):
                return line.split("=", 1)[1].strip()
    return ""


def _api(method: str, path: str, token: str,
         body: Optional[dict] = None) -> tuple[int, dict | str]:
    """Single GitHub API call.

    Returns ``(status_code, parsed_json_or_text)``. Raises
    ``urllib.error.HTTPError`` on transport failures (other
    than the rate-limit / 4xx / 5xx returned in the body).
    """
    url = f"{API_BASE}{path}"
    data = None
    headers = {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "coden-release-cleanup/1.0",
    }
    if body is not None:
        data = json.dumps(body).encode("utf-8")
        headers["Content-Type"] = "application/json"
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            raw = resp.read().decode("utf-8")
            try:
                return resp.status, json.loads(raw) if raw else {}
            except json.JSONDecodeError:
                return resp.status, raw
    except urllib.error.HTTPError as e:
        raw = e.read().decode("utf-8", errors="replace")
        try:
            return e.code, json.loads(raw) if raw else {}
        except json.JSONDecodeError:
            return e.code, raw


def list_releases(token: str) -> list[dict]:
    """All releases (incl. drafts), sorted newest-first by
    GitHub's default ordering.
    """
    releases: list[dict] = []
    page = 1
    while True:
        status, payload = _api(
            "GET", f"/repos/{REPO}/releases?per_page=100&page={page}", token,
        )
        if status != 200:
            print(f"ERROR: GitHub API returned {status}: {payload}")
            sys.exit(1)
        if not isinstance(payload, list) or not payload:
            break
        releases.extend(payload)
        if len(payload) < 100:
            break
        page += 1
    return releases


def delete_asset(asset_id: int, asset_name: str, token: str) -> bool:
    """Delete a single release asset. Returns True on success."""
    status, payload = _api(
        "DELETE", f"/repos/{REPO}/releases/assets/{asset_id}", token,
    )
    if status == 204:
        print(f"  [OK] deleted asset {asset_name!r} (id={asset_id})")
        return True
    print(f"  [FAIL] could not delete {asset_name!r} (id={asset_id}): "
          f"HTTP {status}: {payload}")
    return False


def delete_release(release_id: int, tag: str, token: str) -> bool:
    """Delete a release entirely (keeps the tag + git history)."""
    status, payload = _api(
        "DELETE", f"/repos/{REPO}/releases/{release_id}", token,
    )
    if status == 204:
        print(f"  [OK] deleted release {tag!r} (id={release_id})")
        return True
    print(f"  [FAIL] could not delete release {tag!r} (id={release_id}): "
          f"HTTP {status}: {payload}")
    return False


def format_bytes(n: int) -> str:
    if n < 1024:
        return f"{n} B"
    if n < 1024 * 1024:
        return f"{n / 1024:.1f} KB"
    return f"{n / (1024 * 1024):.1f} MB"


def main() -> int:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what would be deleted, but make no API writes.",
    )
    parser.add_argument(
        "--yes", action="store_true",
        help="Skip the confirmation prompt. Required for any "
             "non-dry-run action.",
    )
    parser.add_argument(
        "--keep", metavar="TAG",
        help="Keep assets of this specific tag; delete the rest. "
             "Default: keep the most recent published release.",
    )
    parser.add_argument(
        "--only", metavar="TAG",
        help="Only act on this one release (delete its assets / "
             "release). Other releases are untouched.",
    )
    parser.add_argument(
        "--delete-releases", action="store_true",
        help="Also delete the release ENTRIES (not just their "
             "assets). Use with care - this removes the release "
             "from the Releases page entirely (the git tag stays).",
    )
    args = parser.parse_args()

    if not args.dry_run and not args.yes:
        print("Refusing to run without --yes (or --dry-run). Pass --yes to confirm.")
        return 2

    token = _get_token()
    if not token:
        print("FATAL: GH_TOKEN not set. Put it in the environment or in electron/.env.")
        return 1

    releases = list_releases(token)
    if not releases:
        print("No releases found. Nothing to do.")
        return 0

    # Find the keep-set.
    if args.keep:
        keep_tags = {args.keep}
    elif args.only:
        keep_tags = set()  # we're only acting on this one
    else:
        # Default: keep the most recent *published* (non-draft,
        # non-prerelease) release.
        latest = None
        for r in releases:
            if r.get("draft") or r.get("prerelease"):
                continue
            latest = r
            break
        if latest is None:
            print("No published release found. Aborting.")
            return 1
        keep_tags = {latest["tag_name"]}

    if args.only:
        # Only delete the one named release's assets.
        targets = [r for r in releases if r["tag_name"] == args.only]
    else:
        # Delete every release's assets except the keep-set.
        targets = [r for r in releases if r["tag_name"] not in keep_tags]

    # Filter out drafts (we never touch drafts).
    targets = [r for r in targets if not r.get("draft")]

    if not targets:
        print("Nothing to clean up - every release is in the keep-set.")
        return 0

    # Preview + total size.
    total_assets = 0
    total_bytes = 0
    print(f"\nFound {len(targets)} release(s) to clean up:")
    for r in targets:
        assets = r.get("assets", [])
        n = len(assets)
        size = sum(a.get("size", 0) for a in assets)
        total_assets += n
        total_bytes += size
        print(f"  - {r['tag_name']:12s}  {n} asset(s)  {format_bytes(size)}")
    print(f"\nTotal: {total_assets} assets, {format_bytes(total_bytes)} "
          f"will be deleted.")
    if args.delete_releases:
        print(f"The {len(targets)} release entries themselves will also be "
              f"removed (git tags stay).")

    if args.dry_run:
        print("\n(dry-run; no API writes were made.)")
        return 0

    if not args.yes:
        # Defensive: if --yes wasn't passed but we got here, abort.
        print("Refusing to delete without --yes.")
        return 2

    print()
    deleted = 0
    for r in targets:
        print(f"Processing {r['tag_name']}...")
        # Delete each asset on this release.
        for asset in list(r.get("assets", [])):
            if delete_asset(asset["id"], asset["name"], token):
                deleted += 1
        # Optionally also delete the release entry.
        if args.delete_releases:
            if delete_release(r["id"], r["tag_name"], token):
                deleted += 1

    print(f"\nDone. {deleted} item(s) deleted, {format_bytes(total_bytes)} freed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
