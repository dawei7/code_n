"""Cut a new release of cOde(n) in one command.

Pipeline:
    1. Bump the version in ``electron/package.json`` (default:
       minor; --patch for hotfix; --set X.Y.Z for explicit).
    2. Commit the version bump + any pending changes on the
       current branch.
    3. Push the branch to ``origin main``.
    4. Create a ``vX.Y.Z`` tag locally and push it.
    5. Build web + server + electron artifacts.
    6. Run ``electron-builder --publish onTagOrDraft`` with
       ``$GH_TOKEN`` set, which creates a published GitHub
       release for the new tag, attaches the NSIS installer +
       its ``.blockmap`` + ``latest.yml``, and (because
       ``releaseType: "release"`` + ``channel: "latest"`` in
       ``electron-builder.json``) is automatically picked up by
       every installed cOde(n) on the next launch.

Usage:
    .venv/Scripts/python.exe release.py              # minor bump
    .venv/Scripts/python.exe release.py --patch      # patch bump
    .venv/Scripts/python.exe release.py --set 1.0.0  # explicit
    .venv/Scripts/python.exe release.py --dry-run    # don't push/publish
    .venv/Scripts/python.exe release.py --no-build   # tag+push only

Prereqs:
    - ``$GH_TOKEN`` must be set in the shell (see RELEASING.md
      section 2 for how to create a fine-grained PAT with
      ``Contents: Read and write`` on ``dawei7/code_n``).
    - The working tree must be clean (no uncommitted changes).
    - The remote ``origin`` must point at the GitHub repo.

The ``--dry-run`` flag walks through the bump, commit, tag, and
build phases but stops before the actual ``git push`` /
``electron-builder --publish`` step. Use it to dry-test a new
version locally.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
ELECTRON_DIR = REPO_ROOT / "electron"
PACKAGE_JSON = ELECTRON_DIR / "package.json"
SEMVER_RE = re.compile(r"^(\d+)\.(\d+)\.(\d+)$")


# ---------------------------------------------------------------------------
# Small git helpers
# ---------------------------------------------------------------------------

def _run(cmd: list[str], cwd: Path | None = None,
         check: bool = True, env: dict | None = None) -> subprocess.CompletedProcess:
    """Run a subprocess, streaming output to the parent."""
    print(f"\n$ {' '.join(cmd)}  (cwd={cwd or REPO_ROOT})")
    result = subprocess.run(
        cmd, cwd=cwd or REPO_ROOT, env=env, text=True,
        capture_output=True,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=sys.stderr)
    if check and result.returncode != 0:
        print(f"FAILED: {' '.join(cmd)} exited {result.returncode}")
        sys.exit(result.returncode)
    return result


def _git(*args: str, check: bool = True) -> subprocess.CompletedProcess:
    return _run(["git", *args], cwd=REPO_ROOT, check=check)


def current_branch() -> str:
    return (_git("rev-parse", "--abbrev-ref", "HEAD").stdout or "").strip()


def working_tree_clean() -> bool:
    """True iff ``git status --porcelain`` is empty."""
    res = _run(["git", "status", "--porcelain"], cwd=REPO_ROOT, check=False)
    return (res.stdout or "").strip() == ""


def tag_exists_remote(tag: str) -> bool:
    """True iff ``git ls-remote --tags origin <tag>`` returns a SHA."""
    res = _run(
        ["git", "ls-remote", "--tags", "origin", tag],
        cwd=REPO_ROOT, check=False,
    )
    return bool((res.stdout or "").strip())


# ---------------------------------------------------------------------------
# Version bump
# ---------------------------------------------------------------------------

def read_version() -> tuple[int, int, int]:
    with PACKAGE_JSON.open("r", encoding="utf-8") as f:
        data = json.load(f)
    version = data.get("version", "")
    m = SEMVER_RE.match(version)
    if not m:
        print(f"FATAL: electron/package.json 'version' is {version!r}, "
              f"expected semver X.Y.Z")
        sys.exit(1)
    return int(m.group(1)), int(m.group(2)), int(m.group(3))


def write_version(major: int, minor: int, patch: int) -> None:
    new_version = f"{major}.{minor}.{patch}"
    with PACKAGE_JSON.open("r", encoding="utf-8") as f:
        data = json.load(f)
    data["version"] = new_version
    with PACKAGE_JSON.open("w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
        f.write("\n")
    print(f"  bumped electron/package.json version: "
          f"{major}.{minor}.{patch - 1} -> {new_version}")


def compute_new_version(
    bump_mode: str, explicit: str | None,
) -> tuple[int, int, int]:
    """Return (major, minor, patch) for the new version.

    ``bump_mode`` is 'minor' or 'patch' (used when ``explicit``
    is None). If ``explicit`` is given, parse it and ignore
    ``bump_mode``.
    """
    if explicit is not None:
        m = SEMVER_RE.match(explicit)
        if not m:
            print(f"FATAL: --set value {explicit!r} is not semver X.Y.Z")
            sys.exit(1)
        return int(m.group(1)), int(m.group(2)), int(m.group(3))
    major, minor, patch = read_version()
    if bump_mode == "minor":
        return major, minor + 1, 0
    if bump_mode == "patch":
        return major, minor, patch + 1
    raise AssertionError(f"unreachable: {bump_mode}")


# ---------------------------------------------------------------------------
# Build steps (delegate to build_app.py to keep one source of truth)
# ---------------------------------------------------------------------------

def run_build(venv_python: str) -> None:
    """Run web + server + electron-build + electron-dist steps.

    The electron-dist step is invoked with ``--publish onTagOrDraft``
    so electron-builder only creates a GitHub release when the
    current commit has the matching tag.
    """
    _run([venv_python, "build_app.py", "--step", "web"])
    _run([venv_python, "build_app.py", "--step", "server"])
    _run([venv_python, "build_app.py", "--step", "electron-build"])
    _run([venv_python, "build_app.py", "--step", "electron-dist",
          "--publish", "onTagOrDraft"])


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--patch", action="store_true",
        help="Bump the patch version (0.1.0 -> 0.1.1) instead of minor.",
    )
    parser.add_argument(
        "--set", dest="explicit", metavar="X.Y.Z",
        help="Set an explicit version instead of auto-bumping.",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Bump + commit + tag + build, but do NOT push or publish.",
    )
    parser.add_argument(
        "--no-build", action="store_true",
        help="Tag + push only; skip the full build (assumes the "
             "build has already been run for the current commit).",
    )
    args = parser.parse_args()

    # -- Sanity checks --------------------------------------------------

    if not PACKAGE_JSON.is_file():
        print(f"FATAL: {PACKAGE_JSON} not found; are you running from the repo root?")
        sys.exit(1)

    if not working_tree_clean():
        print("FATAL: working tree is dirty. Commit or stash your changes first.")
        _run(["git", "status", "--short"], check=False)
        sys.exit(1)

    branch = current_branch()
    if branch != "main":
        print(f"FATAL: current branch is '{branch}', not 'main'. "
              f"Releases are only cut from main.")
        sys.exit(1)

    if not args.dry_run and "GH_TOKEN" not in os.environ:
        print(
            "FATAL: $GH_TOKEN is not set. electron-builder needs it to\n"
            "create the GitHub release. See RELEASING.md section 2 for\n"
            "how to create a fine-grained PAT with 'Contents: Read and\n"
            "write' on dawei7/code_n."
        )
        sys.exit(1)

    # -- Compute + write the new version -------------------------------

    bump_mode = "patch" if args.patch else "minor"
    new_major, new_minor, new_patch = compute_new_version(
        bump_mode, args.explicit,
    )
    new_version = f"{new_major}.{new_minor}.{new_patch}"
    tag = f"v{new_version}"

    if not args.dry_run and tag_exists_remote(tag):
        print(f"FATAL: tag {tag} already exists on origin. Refusing to overwrite.")
        sys.exit(1)

    print(f"\nNew version: {new_version}  (tag: {tag})")

    if not args.dry_run:
        write_version(new_major, new_minor, new_patch)
        _git("add", "electron/package.json")
        _git("commit", "-m", f"chore(release): v{new_version}")
        _git("push", "origin", "main")
        _git("tag", tag)
        _git("push", "origin", tag)
    else:
        print("(dry-run: skipping bump / commit / push / tag)")

    # -- Build + publish ------------------------------------------------

    if not args.no_build:
        venv_python = str(REPO_ROOT / ".venv" / "Scripts" / "python.exe")
        if not Path(venv_python).is_file():
            print(f"FATAL: venv python not found at {venv_python}")
            sys.exit(1)
        run_build(venv_python)
    else:
        print("(skipping build; assuming it's already done)")

    # -- Done -----------------------------------------------------------

    if args.dry_run:
        print(f"\nDry-run complete. New version {new_version} is staged "
              f"locally but NOT pushed and NOT published.")
        return

    print(f"\nRelease complete!")
    print(f"  Version: v{new_version}")
    print(f"  Tag:     {tag}")
    print(f"  URL:     https://github.com/dawei7/code_n/releases/tag/{tag}")
    print()
    print("Every installed cOde(n) on the previous version will auto-pull")
    print("this release on its next launch (the 'Restart to install' pill")
    print("appears when the background download finishes).")


if __name__ == "__main__":
    main()
