"""Build the cOde(n) desktop app end-to-end.

Pipeline:
    1. Build the React app               (``web/`` -> ``web/dist/``)
    2. Bundle the FastAPI server         (``server/`` -> ``server/dist/coden-server/``)
    3. Compile the Electron main process (``electron/`` -> ``electron/dist/``)
    4. Build the Electron .exe           (``electron/`` -> ``electron/release/coden-*.exe``)

Run with::

    .venv/Scripts/python.exe build_app.py

The final artifact is the portable ``.exe`` that the user can
double-click to start cOde(n) without any of the dev-tooling
dependencies installed (no Python, no Node, no venv - everything
is bundled).

Each step is idempotent; running this script twice is a no-op
until something changes. Use ``--step`` to limit to a single
phase (useful for debugging):

    .venv/Scripts/python.exe build_app.py --step electron-build
    .venv/Scripts/python.exe build_app.py --step server
"""
from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent
IS_WINDOWS = platform.system() == "Windows"

DEBUG_PYTHON_SITE_PACKAGES = (
    "debugpy",
    "debugpy-*.dist-info",
    "pydantic",
    "pydantic-*.dist-info",
    "pydantic_core",
    "pydantic_core-*.dist-info",
    "typing_extensions.py",
    "typing_extensions-*.dist-info",
    "annotated_types",
    "annotated_types-*.dist-info",
    "typing_inspection",
    "typing_inspection-*.dist-info",
    "yaml",
    "pyyaml-*.dist-info",
    "PyYAML-*.dist-info",
    "pandas",
    "pandas-*.dist-info",
    "pandas.libs",
    "numpy",
    "numpy-*.dist-info",
    "numpy.libs",
    "dateutil",
    "python_dateutil-*.dist-info",
    "pytz",
    "pytz-*.dist-info",
    "tzdata",
    "tzdata-*.dist-info",
    "six.py",
    "six-*.dist-info",
)


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


def run_capture(cmd: list[str], cwd: Path | None = None) -> str:
    """Run a subprocess and return trimmed stdout."""
    result = subprocess.run(
        cmd,
        cwd=cwd or REPO_ROOT,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        print(f"FAILED: {cmd} exited {result.returncode}")
        if result.stdout:
            print(result.stdout)
        if result.stderr:
            print(result.stderr)
        sys.exit(result.returncode)
    return result.stdout.strip()


def truthy_env(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in {"1", "true", "yes", "on"}


def electron_package_version() -> str:
    package_json = REPO_ROOT / "electron" / "package.json"
    with package_json.open("r", encoding="utf-8") as f:
        data = json.load(f)
    version = data.get("version")
    if not isinstance(version, str) or not version:
        raise ValueError(f"{package_json} is missing a string version")
    return version


def has_windows_code_signing_config() -> bool:
    """Best-effort hint for whether electron-builder was given signing input."""
    cert_file = bool(os.environ.get("WIN_CSC_LINK") or os.environ.get("CSC_LINK"))
    azure = all(
        os.environ.get(name)
        for name in ("AZURE_TENANT_ID", "AZURE_CLIENT_ID", "AZURE_CLIENT_SECRET")
    )
    return cert_file or azure


def windows_signature_summary(path: Path) -> tuple[bool, str]:
    """Return (is_valid, human summary) for a Windows Authenticode signature."""
    if not IS_WINDOWS:
        return False, "signature check skipped on non-Windows host"
    if not path.is_file():
        return False, "missing artifact"

    script = (
        "$sig = Get-AuthenticodeSignature -LiteralPath $env:CODEN_SIGNATURE_TARGET; "
        "$subject = if ($sig.SignerCertificate) { "
        "$sig.SignerCertificate.Subject } else { '' }; "
        "Write-Output ($sig.Status.ToString() + '|' + $subject + '|' + "
        "$sig.StatusMessage)"
    )
    env = os.environ.copy()
    env["CODEN_SIGNATURE_TARGET"] = str(path)
    result = subprocess.run(
        [
            "powershell.exe",
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-Command",
            script,
        ],
        env=env,
        text=True,
        capture_output=True,
    )
    if result.returncode != 0:
        detail = (result.stderr or result.stdout or "").strip()
        return False, f"signature check failed: {detail or result.returncode}"

    status, subject, message = (result.stdout.strip().split("|", 2) + ["", ""])[:3]
    if status == "Valid":
        return True, f"valid ({subject})" if subject else "valid"
    if status == "NotSigned":
        return False, "not signed"
    return False, f"{status}: {message}".strip()


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
    step_debug_python_runtime()
    step_debug_tools_dir()


def _copytree_clean(src: Path, dst: Path, *, ignore=None) -> None:
    if dst.exists():
        shutil.rmtree(dst)
    shutil.copytree(src, dst, ignore=ignore)


def _ignore_debug_python_lib(_dir: str, names: list[str]) -> set[str]:
    drop_dirs = {"__pycache__", "test", "tests", "idlelib", "turtledemo", "ensurepip"}
    return {name for name in names if name in drop_dirs or name.endswith(".pyc")}


def _python_base_prefix() -> Path:
    return Path(
        run_capture([
            venv_python(),
            "-c",
            "import sys; print(sys.base_prefix)",
        ])
    )


def _venv_site_packages() -> Path:
    return Path(
        run_capture([
            venv_python(),
            "-c",
            "import sysconfig; print(sysconfig.get_paths()['purelib'])",
        ])
    )


def _copy_site_package_pattern(source_site: Path, target_site: Path, pattern: str) -> int:
    copied = 0
    for src in source_site.glob(pattern):
        dst = target_site / src.name
        if dst.exists():
            continue
        if src.is_dir():
            shutil.copytree(src, dst, ignore=lambda _d, names: {n for n in names if n == "__pycache__" or n.endswith(".pyc")})
        else:
            shutil.copy2(src, dst)
        copied += 1
    return copied


def step_debug_python_runtime() -> None:
    """Create the bundled Python runtime used by the in-app debugger.

    The packaged FastAPI server is a frozen executable, not a general Python
    interpreter. debugpy needs a real python.exe for its adapter, launcher, and
    debuggee subprocesses, so Windows releases ship a small runtime next to the
    server bundle instead of depending on the user's machine.
    """
    if not IS_WINDOWS:
        print("Skipping bundled debug Python runtime on non-Windows host.")
        return

    base = _python_base_prefix()
    source_site = _venv_site_packages()
    target = REPO_ROOT / "server" / "dist" / "debug-python"

    if target.exists():
        shutil.rmtree(target)
    target.mkdir(parents=True)

    for name in ("python.exe", "pythonw.exe"):
        src = base / name
        if not src.is_file():
            print(f"debug Python source file missing: {src}")
            sys.exit(1)
        shutil.copy2(src, target / name)

    for pattern in ("python*.dll", "vcruntime*.dll"):
        for src in base.glob(pattern):
            shutil.copy2(src, target / src.name)

    _copytree_clean(base / "DLLs", target / "DLLs")
    _copytree_clean(base / "Lib", target / "Lib", ignore=_ignore_debug_python_lib)

    target_site = target / "Lib" / "site-packages"
    if target_site.exists():
        shutil.rmtree(target_site)
    target_site.mkdir(parents=True)

    copied = 0
    for pattern in DEBUG_PYTHON_SITE_PACKAGES:
        copied += _copy_site_package_pattern(source_site, target_site, pattern)

    expected = target / "python.exe"
    run([
        str(expected),
        "-c",
        "import debugpy.adapter.__main__, pandas, pydantic, yaml; print('OK: debug Python and pandas imports ready')",
    ])
    size_mb = sum(p.stat().st_size for p in target.rglob("*") if p.is_file()) / (1024 * 1024)
    print(
        f"OK: bundled debug Python at {target.relative_to(REPO_ROOT)} "
        f"({size_mb:.1f} MB, copied {copied} package entries)"
    )


def step_debug_tools_dir() -> None:
    """Create the optional packaged debug-tools slot.

    Non-Python debugging still needs native toolchains/adapters. The app looks
    for them in CODEN_DEBUG_TOOLS_DIR, and packaged Electron builds set that
    variable to resources/debug-tools when this folder is present. Release
    builders can place lldb-dap/g++/javac/java/netcoredbg/dotnet/node/go/dlv/
    kotlinc or wrappers under this directory without changing the app code.
    """
    target = REPO_ROOT / "server" / "dist" / "debug-tools"
    target.mkdir(parents=True, exist_ok=True)
    bash_bundle = os.environ.get("CODEN_BASH_BUNDLE_DIR", "").strip()
    if bash_bundle:
        bash_source = Path(bash_bundle)
        if not bash_source.is_dir():
            print(f"CODEN_BASH_BUNDLE_DIR is not a directory: {bash_source}")
            sys.exit(1)
        bash_target = target / "bash"
        if bash_target.exists():
            shutil.rmtree(bash_target)
        shutil.copytree(bash_source, bash_target)
    readme = target / "README.txt"
    readme.write_text(
        "\n".join(
            [
                "Optional cOde(n) native debugger tools.",
                "",
                "The packaged Electron app sets CODEN_DEBUG_TOOLS_DIR to this",
                "directory when it exists. The FastAPI debugger searches common",
                "subfolders such as bin, cpp/bin, java/bin, jdk/bin, csharp/bin,",
                "dotnet/bin, node/bin, go/bin, kotlin/bin, javascript, and js-debug for:",
                "",
                "- C++: lldb-dap or lldb-vscode, plus g++ or clang++",
                "- Java: javac, java, plus java-debug-adapter(.exe/.jar) or java-debug.jar",
                "- C#: netcoredbg plus dotnet",
                "- JavaScript: node plus js-debug-adapter(.js/.exe)",
                "- Go: dlv plus go",
                "- Kotlin: kotlinc, java, plus the Java debug adapter",
                "- Bash runs: bash/bin/bash.exe (set CODEN_BASH_BUNDLE_DIR during release builds)",
                "",
                "Users can still override every path with CODEN_CPP_DEBUG_ADAPTER,",
                "CODEN_CPP_COMPILER, CODEN_JAVAC, CODEN_JAVA, CODEN_JAVA_DEBUG_ADAPTER,",
                "CODEN_NETCOREDBG, CODEN_DOTNET, CODEN_NODE, CODEN_JS_DEBUG_ADAPTER,",
                "CODEN_GO, CODEN_GO_DEBUG_ADAPTER, CODEN_KOTLINC, or CODEN_BASH.",
            ]
        )
        + "\n",
        encoding="utf-8",
    )
    print(f"OK: debug-tools slot at {target.relative_to(REPO_ROOT)}")


def step_electron_build() -> None:
    """Compile the Electron main process TypeScript.

    The tsconfig has ``rootDir: ".."`` (set to ``..`` to
    accommodate a cross-project type import from
    ``../web/src/types/electron.ts``), so the compiled
    output mirrors the source structure: the entry is at
    ``dist/electron/src/main.js`` (not ``dist/main.js``).
    This step checks for the actual output path.
    """
    npm = find_tool("npm")
    run([npm, "install", "--no-audit", "--no-fund"], cwd=REPO_ROOT / "electron")
    run([npm, "run", "build"], cwd=REPO_ROOT / "electron")
    expected = REPO_ROOT / "electron" / "dist" / "electron" / "src" / "main.js"
    if not expected.is_file():
        print(f"electron build did not produce {expected}")
        sys.exit(1)
    print(f"OK: electron main at {expected.relative_to(REPO_ROOT)}")


def step_electron_dist(
    publish: str = "never",
    require_code_signing: bool = False,
) -> None:
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
    required_inputs = [
        REPO_ROOT / "server" / "dist" / "coden-server" / (
            "coden-server.exe" if IS_WINDOWS else "coden-server"
        ),
        REPO_ROOT / "server" / "dist" / "debug-python" / "python.exe",
        REPO_ROOT / "server" / "dist" / "debug-tools" / "README.txt",
    ]
    missing_inputs = [p for p in required_inputs if not p.is_file()]
    if missing_inputs:
        print("electron-dist missing packaged runtime inputs:")
        for path in missing_inputs:
            print(f"  {path.relative_to(REPO_ROOT)}")
        print("Run `build_app.py --step server` first.")
        sys.exit(1)

    npx = find_tool("npx")
    cmd = [npx, "electron-builder", "--win", "--x64", "--publish", publish]
    if require_code_signing:
        cmd.append("-c.forceCodeSigning=true")
    run(cmd, cwd=REPO_ROOT / "electron")
    unpacked = REPO_ROOT / "electron" / "release" / "win-unpacked"
    if not unpacked.is_dir():
        print(f"electron unpacked dir missing: {unpacked}")
        sys.exit(1)
    launcher = unpacked / ("cOde(n).exe" if IS_WINDOWS else "coden")
    if not launcher.is_file():
        print(f"launcher missing: {launcher}")
        sys.exit(1)
    # Find the NSIS installer for this package version. Avoid lexical sorting
    # because 0.9.9 sorts after 0.10.3.
    version = electron_package_version()
    installer = REPO_ROOT / "electron" / "release" / f"cOde(n)-Setup-{version}.exe"
    if not installer.is_file():
        produced = sorted(
            p.name for p in (REPO_ROOT / "electron" / "release").glob(
                "cOde(n)-Setup-*.exe"
            )
        )
        print(f"installer missing for version {version}: {installer}")
        print(f"available installers: {produced}")
        sys.exit(1)
    size_mb = launcher.stat().st_size / (1024 * 1024)
    print(f"OK: launcher at {launcher.relative_to(REPO_ROOT)} ({size_mb:.1f} MB)")
    inst_mb = installer.stat().st_size / (1024 * 1024)
    print(f"OK: installer at {installer.relative_to(REPO_ROOT)} ({inst_mb:.1f} MB)")

    if IS_WINDOWS:
        artifacts = [launcher, installer]
        print()
        print("Windows code-signing status:")
        signature_results = []
        for artifact in artifacts:
            valid, summary = windows_signature_summary(artifact)
            signature_results.append(valid)
            print(f"  {artifact.name}: {summary}")
        if not all(signature_results):
            if require_code_signing:
                print("FAILED: code signing was required, but an artifact is unsigned.")
                sys.exit(1)
            if has_windows_code_signing_config():
                print("Signing config was present, but not all artifacts validate.")
                print("Check the electron-builder output before publishing.")
            else:
                print("Unsigned installers trigger Windows SmartScreen warnings.")
                print("Set WIN_CSC_LINK/WIN_CSC_KEY_PASSWORD or use Artifact Signing")
                print("before cutting a public release.")
    print()
    print("To run (portable):")
    print(f"  {launcher}")
    print()
    print("To install (NSIS):")
    print(f"  {installer}")


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
    parser.add_argument(
        "--require-code-signing",
        action="store_true",
        default=truthy_env("CODEN_REQUIRE_CODE_SIGNING"),
        help=(
            "Fail the Electron packaging step if no valid Windows code "
            "signing identity is available. Can also be enabled with "
            "CODEN_REQUIRE_CODE_SIGNING=1."
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
        step_electron_dist(args.publish, args.require_code_signing)

    print("\nBuild complete.")


if __name__ == "__main__":
    main()
