"""Build a Windows double-clickable cOde(n) distribution.

Run from the project root:
    .venv\\Scripts\\python.exe build_windows_exe.py

Output:
    dist/cOde(n)/cOde(n).exe

The resulting folder is portable: zip dist/cOde(n) and distribute it.
Players do not need Python or pip installed.
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
APP_NAME = "cOde(n)"
DIST_DIR = ROOT / "dist" / APP_NAME
HIDDEN_IMPORTS = [
    "code_n.api",
    "code_n.counter",
    "code_n.execution_trace",
    "code_n.grid",
    "code_n.pygame_renderer",
    "code_n.tracked",
]


def run(command: list[str]):
    print(" ".join(command))
    subprocess.check_call(command, cwd=ROOT)


def ensure_pyinstaller():
    try:
        import PyInstaller  # noqa: F401
    except ImportError:
        run([sys.executable, "-m", "pip", "install", "pyinstaller>=6.6"])


def _sync_optimal_solutions():
    """Write optimal_solutions/<id>.py for any registered spec
    that doesn't already have one.

    The 16 hand-written originals (intro_01, sort_01..05, search_01..04,
    graph_01, graph_04, dp_01..04) are kept as-is - they have nicer
    prose headers. The auto-generated files are for any spec added
    by the AlgorithmSpec framework, so the Solve button always has
    a file to copy.
    """
    from challenges.registry import CHALLENGE_REGISTRY

    out_dir = ROOT / "optimal_solutions"
    out_dir.mkdir(parents=True, exist_ok=True)
    for cid, cls in CHALLENGE_REGISTRY.items():
        target = out_dir / f"{cid}.py"
        if target.exists():
            continue
        inst = cls()
        spec = inst._spec
        body = spec.source.lstrip("\n")
        # Strip the leading triple-quoted docstring so the auto-
        # generated file's header is the only one.
        for quote in ('"""', "'''"):
            if body.startswith(quote):
                end = body.find(quote, 3)
                if end > 0:
                    body = body[end + len(quote) :].lstrip("\n")
                break
        header = (
            f'"""Optimal solution for {cid}: {spec.name}.\n'
            f"\n"
            f"Auto-generated from challenges/algorithms/{spec.category}.py:SPECS.\n"
            f"{spec.required_complexity.value} time.\n"
            f'"""\n\n\n'
        )
        with open(target, "w", encoding="utf-8") as file:
            file.write(header)
            file.write(body)


def copy_player_files():
    DIST_DIR.mkdir(parents=True, exist_ok=True)
    for folder_name in ["solutions", "player_scripts", "optimal_solutions"]:
        src = ROOT / folder_name
        dst = DIST_DIR / folder_name
        if dst.exists():
            shutil.rmtree(dst)
        if src.exists():
            shutil.copytree(src, dst)

    progress = ROOT / "progress.json"
    if progress.exists():
        shutil.copy2(progress, DIST_DIR / "progress.json")


def build():
    ensure_pyinstaller()
    command = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--noconfirm",
        "--clean",
        "--windowed",
        "--name",
        APP_NAME,
        "--distpath",
        str(ROOT / "dist"),
        "--workpath",
        str(ROOT / "build"),
        "--specpath",
        str(ROOT / "build"),
    ]
    for module_name in HIDDEN_IMPORTS:
        command.extend(["--hidden-import", module_name])
    command.append(str(ROOT / "play.py"))
    run(command)
    _sync_optimal_solutions()
    copy_player_files()
    print()
    print(f"Built: {DIST_DIR / (APP_NAME + '.exe')}")
    print(f"Zip the whole dist/{APP_NAME} folder for distribution.")


if __name__ == "__main__":
    build()
