"""``tools/run_solution.py`` — the VSCode run/debug entry point.

This is a thin CLI wrapper around :func:`server.app.engine_runner.run_player_code`.
It's what the repo's ``.vscode/launch.json`` invokes when the user
presses F5 inside VSCode: VSCode's ``debugpy`` extension wraps the
script in a debug session, so the player gets the full VSCode debug
experience (breakpoints, locals, watch, call stack) for free.

The script does exactly what cOde(n)'s ``Run`` button does, minus
the in-app editor and step player:

  1. Read ``solutions/<id>.py`` from disk (the file-on-disk source
     of truth).
  2. Call :func:`run_player_code` with the requested n + seed.
  3. Print the verdict to stdout (a short human-readable line).

VSCode's debugpy adds the breakpoints / locals / step buttons on
top — cOde(n) just shows the verdict and the complexity analysis
when the player comes back.

Usage from a terminal::

    .venv/Scripts/python.exe tools/run_solution.py sort_01 --n 16 --seed 1
    .venv/Scripts/python.exe tools/run_solution.py search_03 --n 35 --mode real_test

Usage from VSCode (via the repo's ``.vscode/launch.json``):

    Open solutions/<id>.py → F5 → "Run current challenge" → prompted
    for challenge id + n + seed → the script runs under debugpy →
    the breakpoints you set in solutions/<id>.py hit normally.

Why a separate CLI instead of running the FastAPI server?
    The FastAPI server runs the player's source in-process via
    ``runpy.run_path`` (so it can iterate on the code without
    subprocess overhead). For a one-off ``Run`` in cOde(n), the
    in-process path is fine. For a debug session in VSCode, the
    user actually wants the script to be a real Python process
    that debugpy can attach to — they want to set breakpoints
    in their own file, not in a transient ``solutions/abc123.py``
    that gets deleted the moment the run completes.

    ``run_solution.py`` is a real script. The player's
    ``solutions/<id>.py`` is the file VSCode opens. debugpy
    hits breakpoints there normally. The verdict is printed
    to the integrated terminal.

Active-challenge sync
---------------------

cOde(n)'s "Open in VSCode" button writes the current challenge id
to ``solutions/.vscode-active`` (a tiny gitignored file). When
you press F5 in VSCode without arguments, this script reads
that file and uses the id stored there as the default. The
``.vscode/launch.json`` uses a prompt input for the challenge id
explicitly, so the file is just a convenience for the case
where the user types ``python tools/run_solution.py`` directly.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path


# Repo root: tools/run_solution.py → parent is tools → parent is repo.
_REPO_ROOT = Path(__file__).resolve().parent.parent


def _read_solution(challenge_id: str) -> str:
    """Read the player's saved solution for ``challenge_id`` from disk.

    Falls back to a minimal no-op starter if the file doesn't exist
    (e.g. a brand-new challenge that the player has never opened in
    VSCode). The engine runner will reject the no-op for non-trivial
    challenges — the user just gets a clear "Incorrect solution!"
    message rather than a crash, which is the right UX for a
    debug-then-fix workflow.
    """
    solution_path = _REPO_ROOT / "solutions" / f"{challenge_id}.py"
    if solution_path.is_file():
        return solution_path.read_text(encoding="utf-8")
    return f"def solve(**kwargs):\n    # No solution yet for {challenge_id}\n    return None\n"


def _read_active_challenge() -> str | None:
    """Read the cOde(n) → VSCode active-challenge handoff file.

    The file lives in ``solutions/.vscode-active`` (gitignored).
    Format: ``{"id": "sort_01", "n": 16, "seed": 1}`` or
    ``{"id": "sort_01"}`` if the user hasn't set n/seed. Returns
    just the id; n/seed are still CLI args (the user is
    intentionally specifying them on the launch config).
    """
    handoff_path = _REPO_ROOT / "solutions" / ".vscode-active"
    if not handoff_path.is_file():
        return None
    try:
        payload = json.loads(handoff_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return None
    return payload.get("id") or None


def _format_verdict(result) -> str:
    """Render the :class:`RunResponse` as a one-line human-readable verdict.

    The format mirrors what cOde(n) shows in the StatusBanner:
    a green "OK Passed!" or an amber/rose line with the
    reason. The exact colour codes are ANSI; VSCode's integrated
    terminal renders them. Plain ``cmd.exe`` ignores them.

    We use ASCII-only glyphs (PASS / SLOW / REJ / FAIL) so the
    output is portable to Windows consoles (which can't encode
    the unicode "✓ / ✗ / ⚠ / ⏱" characters in cp1252). The
    coloured ANSI prefix is enough to make it scannable in a
    proper terminal.
    """
    if result.passed:
        return (
            f"\033[32mPASS\033[0m "
            f"{result.user_ast_ops:,} ops "
            f"({result.actual_complexity}, required {result.required_complexity})"
        )
    if result.too_efficient:
        return f"\033[33mREJ\033[0m rejected (too efficient) — {result.too_efficient_reason or result.message}"
    if result.correct and not result.within_threshold:
        return (
            f"\033[33mSLOW\033[0m correct but too slow: "
            f"{result.user_ast_ops:,} ops at {result.actual_complexity}; "
            f"need {result.required_complexity}"
        )
    return f"\033[31mFAIL\033[0m {result.message}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a cOde(n) challenge solution. Used by VSCode's F5.",
    )
    parser.add_argument(
        "challenge_id",
        nargs="?",
        default=None,
        help=(
            "The challenge id (e.g. sort_01). If omitted, reads the "
            "id from solutions/.vscode-active (written by cOde(n)'s "
            "'Open in VSCode' button)."
        ),
    )
    parser.add_argument("--n", type=int, default=16, help="Input size (default: 16)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed (default: 1)")
    parser.add_argument(
        "--mode",
        choices=["practice", "real_test"],
        default="practice",
        help="Run mode (default: practice)",
    )
    parser.add_argument(
        "--no-ansi",
        action="store_true",
        help="Strip ANSI colour codes from the verdict (for piping to a file).",
    )
    args = parser.parse_args()

    challenge_id = args.challenge_id or _read_active_challenge()
    if not challenge_id:
        print(
            "error: no challenge_id given and solutions/.vscode-active is missing.\n"
            "       Pass the id explicitly: tools/run_solution.py <id> --n N --seed S\n"
            "       Or open cOde(n) and click 'Open in VSCode' to write the handoff file.",
            file=sys.stderr,
        )
        return 2

    # Make the repo root importable so server.* and challenges.* work.
    sys.path.insert(0, str(_REPO_ROOT))

    # Read the file-on-disk source (the same one cOde(n) reads).
    source = _read_solution(challenge_id)
    seed = args.seed if args.seed is not None else 1

    # Lazy import: the engine + FastAPI surface is heavy, and we
    # don't want to pay for it on a syntax error in the player's
    # solution (the engine will tell us the syntax error itself).
    from server.app.engine_runner import run_player_code

    print(
        f"-> running {challenge_id} (n={args.n}, seed={seed}, mode={args.mode})",
        file=sys.stderr,
    )
    result = run_player_code(
        challenge_id=challenge_id,
        source=source,
        n=args.n,
        seed=seed,
        mode=args.mode,
        # Pass the workspace path so debugpy can hit breakpoints
        # in the player's open editor file. The engine normally
        # copies the source into a temp dir for tracer filename
        # uniqueness; the explicit ``execution_path`` opt-out
        # (added for this VSCode entry point) keeps everything
        # mapped to ``solutions/<id>.py``.
        execution_path=str(_REPO_ROOT / "solutions" / f"{challenge_id}.py"),
    )

    verdict_line = _format_verdict(result)
    if args.no_ansi or not sys.stdout.isatty():
        # Strip ANSI for non-tty output (pipes, file redirects).
        import re
        verdict_line = re.sub(r"\033\[[0-9;]*m", "", verdict_line)
    print(verdict_line)
    if result.return_value_repr:
        # The return value is a compact JSON-ish string from the
        # engine. Show it on a separate line so the player can see
        # what ``solve()`` actually produced.
        print(f"  returned: {result.return_value_repr}")
    if result.user_ast_ops is not None and result.reference_ast_ops is not None:
        ci = f"[{result.reference_ci_low:,}, {result.reference_ci_high:,}]"
        print(
            f"  ops: {result.user_ast_ops:,} (you) vs "
            f"{result.reference_ast_ops:,} (ref) — ±5% band: {ci}"
        )

    # Exit code: 0 on pass, 1 on fail. CI scripts can use this
    # to gate commits. Note: an unfixed solution will exit 1, which
    # is fine for the player's debug loop (they see the verdict
    # in the terminal and iterate).
    return 0 if result.passed else 1


def _is_debugger_attached() -> bool:
    """Return True if debugpy is currently attached to this process.

    debugpy sets ``sys.flags.debug`` and exposes ``sys.gettrace()``
    returning a non-None callable. Either signal is enough for the
    VSCode F5 case; we don't try to be clever about remote attach.
    """
    if getattr(sys, "flags", None) is not None and getattr(sys.flags, "debug", 0):
        return True
    return sys.gettrace() is not None


if __name__ == "__main__":
    exit_code = main()
    # Under a debugger, leave the process alive so the player can
    # inspect post-run state (locals, return value, the trace
    # object) after the verdict prints. ``SystemExit`` would
    # tear down the process before they get a chance to look.
    if _is_debugger_attached():
        # Block forever so the IDE stays attached. The user ends
        # the session with the Stop button. ``input()`` on EOF
        # raises EOFError, which we swallow.
        try:
            print(
                "\n[run_solution] debugger attached — process held open. "
                "Press Stop in VSCode to end the session.",
                file=sys.stderr,
            )
            input()
        except EOFError:
            pass
    else:
        raise SystemExit(exit_code)
