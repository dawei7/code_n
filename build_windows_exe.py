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
    copy_player_files()
    print()
    print(f"Built: {DIST_DIR / (APP_NAME + '.exe')}")
    print(f"Zip the whole dist/{APP_NAME} folder for distribution.")


if __name__ == "__main__":
    build()
