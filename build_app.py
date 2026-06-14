"""Build the cOde(n) desktop app end-to-end.

Pipeline:
    1. Build the React app               (``web/``    → ``web/dist/``)
    2. Bundle the FastAPI server         (``server/`` → ``server/dist/coden-server/``)
    3. Compile the Electron main process (``electron/`` → ``electron/dist/``)
    4. Build the Electron .exe           (``electron/`` → ``electron/release/coden-*.exe``)

Run with::

    .venv/Scripts/python.exe build_app.py

The final artifact is the portable ``.exe`` that the user can
double-click to start cOde(n) without any of the dev-tooling
dependencies installed (no Python, no Node, no venv — everything
is bundled).

Each step is idempotent; running this script twice is a no-op
until something changes. Use ``--step`` to limit to a single
phase (useful for debugging):

    .venv/Scripts/python.exe build_app.py --step electron
    .venv/Scripts/python.exe build_app.py --step server
"""
from __future__ import annotations

import argparse
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
IS_WINDOWS = platform.system() == "Windows"


def venv_python() -> str:
    """Path to the project venv's Python interpreter."""
    if IS_WINDOWS:
        return str(REPO_ROOT / ".venv" / "Scripts" / "python.exe")
    return str(REPO_ROOT / ".venv" / "bin" / "python")


def find_tool(name: str) -> str:
    """Find a CLI tool's full path. On Windows, falls back to common
    install locations if the user's PATH doesn't include the tool.
    """
    full = shutil.which(name)
    if full:
        return full
    if IS_WINDOWS:
        candidates = {
            "npm": [r"C:\Program Files\nodejs\npm.cmd",
                    r"C:\Program Files\nodejs\npm.exe"],
            "node": [r"C:\Program Files\nodejs\node.exe"],
        }.get(name, [])
        for candidate in candidates:
            if os.path.exists(candidate):
                return candidate
    raise FileNotFoundError(
        f"Could not find '{name}' on PATH. Install Node.js (provides npm) "
        f"and ensure it's on PATH, or set CODEN_NPM to the full path."
    )


def run(cmd: list[str], cwd: Path | None = None, env: dict | None = None,
        check: bool = True) -> None:
    """Run a subprocess, streaming stdout/stderr to the parent."""
    print(f"\n>>> {' '.join(cmd)}  (cwd={cwd or REPO_ROOT})")
    result = subprocess.run(cmd, cwd=cwd or REPO_ROOT, env=env)
    if check and result.returncode != 0:
        print(f"FAILED: {cmd} exited {result.returncode}")
        sys.exit(result.returncode)


def step_web() -> None:
    """Build the React app."""
    npm = find_tool("npm")
    run([npm, "install", "--no-audit", "--no-fund"], cwd=REPO_ROOT / "web")
    run([npm, "run", "build"], cwd=REPO_ROOT / "web")
    expected = REPO_ROOT / "web" / "dist" / "index.html"
    if not expected.is_file():
        print(f"web build did not produce {expected}")
        sys.exit(1)
    print(f"OK: web app at {expected.relative_to(REPO_ROOT)}")


def step_server() -> None:
    """Build the PyInstaller server bundle."""
    run([venv_python(), "-m", "PyInstaller", "server.spec",
         "--clean", "--noconfirm", "--distpath", str(REPO_ROOT / "server" / "dist")],
        cwd=REPO_ROOT / "server")
    expected = REPO_ROOT / "server" / "dist" / "coden-server" / (
        "coden-server.exe" if IS_WINDOWS else "coden-server"
    )
    if not expected.is_file():
        print(f"server build did not produce {expected}")
        sys.exit(1)
    print(f"OK: bundled server at {expected.relative_to(REPO_ROOT)}")


def step_electron_build() -> None:
    """Compile the Electron main process TypeScript."""
    npm = find_tool("npm")
    run([npm, "install", "--no-audit", "--no-fund"], cwd=REPO_ROOT / "electron")
    run([npm, "run", "build"], cwd=REPO_ROOT / "electron")
    expected = REPO_ROOT / "electron" / "dist" / "main.js"
    if not expected.is_file():
        print(f"electron build did not produce {expected}")
        sys.exit(1)
    print(f"OK: electron main at {expected.relative_to(REPO_ROOT)}")


def step_electron_dist(publish: str = "never") -> None:
    """Package the Electron app.

    Outputs both an NSIS installer and a portable ``win-unpacked/``
    folder (driven by ``electron-builder.json``'s ``win.target``
    list, which now contains both):

    - ``electron/release/cOde(n)-Setup-<version>.exe`` (NSIS
      installer, per-user, ~95 MB) — this is what end users
      install.
    - ``electron/release/win-unpacked/cOde(n).exe`` (portable
      folder, ~170 MB) — useful for dev / smoke tests.

    The ``publish`` value is forwarded to electron-builder:
        never          - default; build only, no GitHub release.
        onTagOrDraft   - publish only when the current commit
                         already has a tag (or a draft release
                         exists). Used by ``release.py``.
        always         - force-publish on every build. Dangerous;
                         use only if you know what you're doing.
    """
    npx = find_tool("npx")
    run([npx, "electron-builder", "--win", "--x64", "--publish", publish],
        cwd=REPO_ROOT / "electron")
    unpacked = REPO_ROOT / "electron" / "release" / "win-unpacked"
    if not unpacked.is_dir():
        print(f"electron unpacked dir missing: {unpacked}")
        sys.exit(1)
    launcher = unpacked / ("cOde(n).exe" if IS_WINDOWS else "coden")
    if not launcher.is_file():
        print(f"launcher missing: {launcher}")
        sys.exit(1)
    # Find the NSIS installer electron-builder just produced.
    installers = sorted((REPO_ROOT / "electron" / "release").glob(
        "cOde(n)-Setup-*.exe"
    ))
    size_mb = launcher.stat().st_size / (1024 * 1024)
    print(f"OK: launcher at {launcher.relative_to(REPO_ROOT)} ({size_mb:.1f} MB)")
    if installers:
        inst = installers[-1]
        inst_mb = inst.stat().st_size / (1024 * 1024)
        print(f"OK: installer at {inst.relative_to(REPO_ROOT)} ({inst_mb:.1f} MB)")
    print()
    print("To run (portable):")
    print(f"  {launcher}")
    if installers:
        print()
        print("To install (NSIS):")
        print(f"  {installers[-1]}")
    print()
    print("If Windows SmartScreen shows 'Windows protected your PC':")
    print("  click 'More info' -> 'Run anyway' (no code-signing cert yet).")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--step",
        choices=["web", "server", "electron-build", "electron-dist", "all"],
        default="all",
    )
    parser.add_argument(
        "--publish",
        choices=["never", "onTagOrDraft", "always"],
        default="never",
        help=(
            "Forwarded to electron-builder when --step electron-dist "
            "is selected. 'never' (default) builds only; "
            "'onTagOrDraft' creates a GitHub release if the current "
            "commit has a matching tag (used by release.py); "
            "'always' force-publishes on every build."
        ),
    )
    args = parser.parse_args()

    print(f"cOde(n) build pipeline — {REPO_ROOT}")
    print(f"Python: {venv_python()}")
    print(f"Platform: {platform.system()} {platform.release()}")

    if args.step in ("web", "all"):
        step_web()
    if args.step in ("server", "all"):
        step_server()
    if args.step in ("electron-build", "all"):
        step_electron_build()
    if args.step in ("electron-dist", "all"):
        step_electron_dist(args.publish)

    print("\nBuild complete.")


if __name__ == "__main__":
    main()
