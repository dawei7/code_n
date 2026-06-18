"""Build the cOde(n) desktop app end-to-end.

Pipeline:
    1. Build the React app               (``web/``    → ``web/dist/``)
    2. Bundle the FastAPI server         (``server/`` → ``server/dist/coden-server/``)
    3. Stage the per-user workspace      (``tools/`` + ``server/`` + ``code_n/`` + ``challenges/`` → ``bundled-workspace/``)
    4. Compile the Electron main process (``electron/`` → ``electron/dist/``)
    5. Build the Electron .exe           (``electron/`` → ``electron/release/coden-*.exe``)

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


def step_stage_bundled_workspace() -> None:
    """Stage the per-user VSCode workspace template.

    Populates ``bundled-workspace/`` at the repo root by copying
    a snapshot of the engine source modules (``tools/``,
    ``server/``, ``code_n/``, ``challenges/``) next to the
    hand-tuned ``.vscode/`` template (which is checked in).
    The Electron main process then copies this whole tree into
    the user's ``app.getPath('userData')`` on first launch,
    turning the userData dir into a self-contained VSCode
    workspace where ``solutions/<id>.py`` can be edited and
    debugged via F5 (the launch config runs
    ``tools/run_solution.py`` under debugpy, which needs the
    engine modules on the Python path).

    This step is idempotent: it ``rm -rf``s the per-step
    subdirs (``tools/``, ``server/``, ``code_n/``,
    ``challenges/``) and recreates them from the repo on every
    build. The ``.vscode/`` template is left untouched (it's
    hand-written, not auto-generated). This keeps the build
    deterministic: any change to the engine source flows
    straight into the bundle.

    Why a staging dir, not just bundling the repo root?
        Bundling the whole repo would also bundle .venv/,
        dist/, build/, .git/, docs/source/, etc. — ~hundreds
        of MB of useless stuff. The staging dir is exactly
        the ~500 KB of files the user needs in their
        workspace.

    Why copy the engine source if it's already in the
    PyInstaller bundle?
        The PyInstaller bundle is a frozen ``.exe``; the
        source ``.py`` files inside it are compiled to
        ``.pyc`` and embedded — debugpy can't import from
        it. ``tools/run_solution.py`` does a regular
        ``from server.app.engine_runner import
        run_player_code``; for that to work, the ``server/``
        package must be on ``sys.path`` as readable ``.py``
        files. We copy the engine source into the user's
        workspace for this reason.
    """
    stage = REPO_ROOT / "bundled-workspace"
    stage.mkdir(parents=True, exist_ok=True)

    # The .vscode/ template is hand-written and checked in.
    # If it's missing, the build is broken — bail out clearly.
    template_vsc = stage / ".vscode"
    if not template_vsc.is_dir():
        print(f"bundled-workspace template missing at {template_vsc}")
        sys.exit(1)

    # The .py source dirs are copied from the repo at build
    # time. We clear the destination first so a removed file
    # in the source is reflected in the bundle.
    for src_name in ("tools", "server", "code_n", "challenges"):
        src = REPO_ROOT / src_name
        dst = stage / src_name
        if not src.is_dir():
            print(f"source dir missing: {src}")
            sys.exit(1)
        if dst.exists():
            shutil.rmtree(dst)

        def _ignore(_dir: str, names: list[str]) -> set[str]:
            # Drop bytecode + tool caches, plus the heavy
            # build outputs (PyInstaller dist/build dirs are
            # 50+ MB on their own and aren't part of the
            # runtime engine source).
            drop = {
                "__pycache__",
                ".pytest_cache",
                ".mypy_cache",
                ".ruff_cache",
                "dist",
                "build",
            }
            return {n for n in names if n in drop or n.endswith(".pyc")}

        shutil.copytree(src, dst, ignore=_ignore)

    # Sanity check: the launch config + the F5 entry point must
    # both end up in the staging dir, or the user's "Open in
    # VSCode" → F5 loop will break.
    must_have = [
        stage / ".vscode" / "launch.json",
        stage / ".vscode" / "settings.json",
        stage / "tools" / "run_solution.py",
        stage / "server" / "app" / "engine_runner.py",
        stage / "code_n" / "challenge.py",
        stage / "challenges" / "registry.py",
    ]
    missing = [p for p in must_have if not p.is_file()]
    if missing:
        print(f"bundled-workspace missing files: {missing}")
        sys.exit(1)
    size_kb = sum(p.stat().st_size for p in stage.rglob("*") if p.is_file()) / 1024
    print(f"OK: bundled-workspace staged at {stage.relative_to(REPO_ROOT)} ({size_kb:.0f} KB)")


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
        choices=["web", "server", "stage-workspace", "electron-build", "electron-dist", "all"],
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
    if args.step in ("stage-workspace", "all"):
        step_stage_bundled_workspace()
    if args.step in ("electron-build", "all"):
        step_electron_build()
    if args.step in ("electron-dist", "all"):
        step_electron_dist(args.publish)

    print("\nBuild complete.")


if __name__ == "__main__":
    main()
