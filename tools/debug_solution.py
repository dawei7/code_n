"""Run one cOde(n) solution as a debugpy launch target."""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path


def _workspace_root() -> Path:
    return Path(os.environ.get("CODEN_HOME") or Path(__file__).resolve().parent.parent)


def main() -> int:
    parser = argparse.ArgumentParser(description="Debug a cOde(n) challenge solution.")
    parser.add_argument("challenge_id")
    parser.add_argument("--n", type=int, default=16)
    parser.add_argument("--seed", type=int, default=1)
    parser.add_argument("--mode", choices=["practice", "real_test"], default="practice")
    parser.add_argument(
        "--no-hold",
        action="store_true",
        help="Exit normally when the run finishes instead of waiting for debugger stop.",
    )
    args = parser.parse_args()

    root = _workspace_root()
    sys.path.insert(0, str(root))
    solution_path = root / "solutions" / f"{args.challenge_id}.py"
    source = solution_path.read_text(encoding="utf-8")

    from server.app.engine_runner import run_player_code

    print(f"running {args.challenge_id} (n={args.n}, seed={args.seed}, mode={args.mode})")
    result = run_player_code(
        challenge_id=args.challenge_id,
        source=source,
        n=args.n,
        seed=args.seed,
        mode=args.mode,
        execution_path=str(solution_path),
    )
    print(result.message)
    if result.setup_data_repr and not result.passed:
        print("inputs:")
        for key, value in result.setup_data_repr.items():
            print(f"  {key}: {value}")
    if result.return_value_repr:
        print(f"returned: {result.return_value_repr}")
    if result.reference_return_value_repr and not result.correct:
        print(f"expected: {result.reference_return_value_repr}")

    if not args.no_hold and sys.gettrace() is not None:
        try:
            input("debugger attached; press Stop or Enter to finish")
        except EOFError:
            pass
    return 0 if result.passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
