"""debug_worker — the subprocess that hosts debugpy for the
Debug tab in cOde(n).

Why a subprocess? The server runs the engine's regular ``Run``
path in-process (``runpy.run_path`` + ``sys.settrace``), so we
can't run debugpy in the same process — debugpy itself uses
``sys.settrace`` and would clobber our tracer. We also want the
debug session to be able to crash, hang, or be killed without
taking down the whole server. A subprocess is the clean answer.

Lifecycle::

    server (FastAPI)
      └─ spawn: python server/debug_worker.py <source_path> <challenge_id> <n> <seed>
           └─ debugpy.listen(('127.0.0.1', 0))  ← picks free port, prints it
           └─ debugpy.wait_for_client()        ← blocks until the DAP client connects
           └─ set breakpoints from env var CODEN_BREAKPOINTS
           └─ import user source, run solve(**setup_data) under the tracer
           └─ print final result as one JSON line prefixed with CODEN_RESULT:

The server's :class:`DebugController` parses the
``debugpy: listening on ...`` line for the port, then talks
DAP to the subprocess over TCP.

The subprocess is killed when the server's WebSocket closes
(handled by the routes/debug.py handler).
"""
from __future__ import annotations

import os
import runpy
import sys
import tempfile
import traceback
from pathlib import Path

# Bootstrap: this script lives in <repo>/server/debug_worker.py;
# the engine + challenges packages live at <repo>/code_n and
# <repo>/challenges. We add the repo root to sys.path so the
# imports below work the same way as in the engine_runner.
_HERE = Path(__file__).resolve().parent
_REPO_ROOT = _HERE.parent
if str(_REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(_REPO_ROOT))


def main() -> int:
    """Run one debug session and exit."""
    if len(sys.argv) != 6:
        print("usage: debug_worker.py <source_path> <challenge_id> <n> <seed> <port>", file=sys.stderr)
        return 2
    source_path = Path(sys.argv[1])
    challenge_id = sys.argv[2]
    n = int(sys.argv[3])
    seed = int(sys.argv[4]) if sys.argv[4] != "None" else None
    port = int(sys.argv[5])

    # debugpy MUST be imported and listening BEFORE the user
    # source is exec'd, so that breakpoints in the source take
    # effect. The server picks the port; we just listen on it.
    import debugpy  # noqa: E402 - intentional late import

    debugpy.listen(("127.0.0.1", port))
    sys.stdout.write(f"CODEN_LISTENING: {port}\n")
    sys.stdout.flush()

    # Block until the DAP client (the server's DebugController)
    # attaches. If the parent never connects, we time out and
    # exit; the parent will see the process go away.
    debugpy.wait_for_client()

    # Set breakpoints from the env var. The format is a
    # comma-separated list of 1-based line numbers. The
    # player's source is at ``source_path``; we set each
    # breakpoint against that file by passing the full path.
    bp_env = os.environ.get("CODEN_BREAKPOINTS", "")
    breakpoint_lines: set[int] = set()
    for piece in bp_env.split(","):
        piece = piece.strip()
        if not piece:
            continue
        try:
            breakpoint_lines.add(int(piece))
        except ValueError:
            pass
    for line in sorted(breakpoint_lines):
        try:
            # debugpy.breakpoint sets a breakpoint at the
            # current call site by default. To target a
            # specific file, we pass ``filename`` (the
            # full path). debugpy matches the path against
            # the file the frame is executing.
            debugpy.breakpoint(filename=str(source_path), line=line)
            print(f"CODEN_BP: set breakpoint at {source_path}:{line}", file=sys.stderr, flush=True)
        except Exception as e:  # pragma: no cover
            print(f"failed to set breakpoint at line {line}: {e}", file=sys.stderr, flush=True)

    # Load the challenge + setup.
    from challenges.registry import CHALLENGE_REGISTRY

    challenge_cls = CHALLENGE_REGISTRY.get(challenge_id)
    if challenge_cls is None:
        _emit_result({"ok": False, "error": f"unknown challenge: {challenge_id}"})
        return 1
    challenge = challenge_cls()
    challenge._n = n
    challenge._seed = seed
    setup_data = challenge.setup(n, seed)

    # Exec the player's source in a fresh namespace.
    namespace: dict = {"__name__": "player_solution"}
    try:
        exec(compile(source_path.read_text(encoding="utf-8"), str(source_path), "exec"), namespace)
    except SyntaxError as exc:
        _emit_result({"ok": False, "error": f"SyntaxError: {exc.msg} (line {exc.lineno})"})
        return 0

    if "solve" not in namespace:
        _emit_result({"ok": False, "error": "no `def solve(**kwargs)` in the source"})
        return 0
    solve_fn = namespace["solve"]

    # Run solve. debugpy will pause at the breakpoints; the
    # server sends `next` / `stepIn` / `continue` via DAP.
    try:
        print("CODEN_RUN: starting solve", file=sys.stderr, flush=True)
        result = solve_fn(**setup_data)
        print(f"CODEN_RUN: solve returned: {result!r}", file=sys.stderr, flush=True)
        # After solve returns, emit a "done" marker so the
        # parent knows the run completed.
        _emit_result({
            "ok": True,
            "finished": True,
            "result_repr": repr(result)[:500],
        })
    except Exception as exc:
        print(f"CODEN_RUN: solve raised: {exc}", file=sys.stderr, flush=True)
        _emit_result({
            "ok": False,
            "finished": True,
            "error": f"{type(exc).__name__}: {exc}",
            "traceback": traceback.format_exc()[-1000:],
        })

    return 0


def _emit_result(payload: dict) -> None:
    """Print one JSON line to stdout, prefixed so the parent
    can grep for it without colliding with debugpy's own
    output."""
    import json
    sys.stdout.write("CODEN_RESULT: " + json.dumps(payload) + "\n")
    sys.stdout.flush()


if __name__ == "__main__":
    raise SystemExit(main())
