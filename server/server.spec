# -*- mode: python ; coding: utf-8 -*-
"""PyInstaller definition for the canonical LeetCode FastAPI server.

The LeetCode packages are shipped as an Electron extra resource and resolved
through ``CODEN_DSA_DIR``. They are intentionally not embedded in the frozen
Python archive.
"""

from PyInstaller.utils.hooks import collect_submodules


block_cipher = None

hiddenimports = [
    "server.app.main",
    "server.app.config",
    "server.app.schemas",
    "server.app.ast_ops",
    "server.app.challenge_packages",
    "server.app.challenge_sets",
    "server.app.dap_client",
    "server.app.engine_runner",
    "server.app.error_handlers",
    "server.app.external_programs",
    "server.app.optimal_sources",
    "server.app.progress_store",
    "server.app.source_ops",
    "server.app.special_environments",
    "server.app.too_efficient",
    "server.app.trace_codec",
    "server.app.validated_cases",
    "server.app.routes.challenges",
    "server.app.routes.debug",
    "server.app.routes.docs",
    "server.app.routes.health",
    "server.app.routes.practice_export",
    "server.app.routes.profiles",
    "server.app.routes.progress",
    "server.app.routes.run",
    "server.app.routes.solutions",
    "engine.branding",
    "engine.challenge",
    "engine.counter",
    "engine.execution_trace",
    "engine.grid",
    "engine.languages",
    "engine.progress",
    "engine.samples",
    "engine.solutions",
    "engine.special_environments",
    "challenges.registry",
    "challenges.spec",
    "challenges.algorithms.leetcode",
    "debugpy",
    "debugpy._vendored",
] + collect_submodules("uvicorn") + collect_submodules("fastapi") + collect_submodules("starlette") + collect_submodules("debugpy")


a = Analysis(
    ["run_server.py"],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=["pygame", "pytest", "tkinter"],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="coden-server",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="coden-server",
)
