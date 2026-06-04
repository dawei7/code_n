"""Run a challenge with a player's solution script.

Usage: python run_challenge.py <challenge_id> [player_script.py] [--n SIZE] [--seed SEED] [--no-animate] [--pygame] [--speed PRESET]
       python run_challenge.py --list
       python run_challenge.py --diff <challenge_id>

The player script must define a function called `solve` that accepts
the challenge's parameters and returns the expected result.

If no script path is supplied, cOde(n) loads solutions/<challenge_id>.py.
"""

from challenges.registry import get_challenge, list_challenges
from code_n.counter import ComplexityClass, OpStats, reset_counter
from code_n.grid import CellType, Grid
from code_n.progress import load_progress, save_progress
from code_n.solutions import create_solution_file, resolve_solution_path
import sys
import os
import importlib.util
import argparse

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


# Hard cap on the input size. cOde(n) is built around visualizing the
# whole algorithm in a single window; values above 50 either:
#   - don't fit on screen even at the smallest zoom (BFS/DFS grids), or
#   - produce so many tracked operations that the budget math stops
#     matching the spirit of the complexity class (sorting/searching).
# Larger inputs don't add pedagogical value; they just make the
# visualizer annoying to use. Bump this in one place if you ever need
# to raise the ceiling.
MAX_N = 50
DEFAULT_N = 50


class PlayerScriptError(Exception):
    """Raised when a player script cannot be loaded or does not define solve()."""


def load_player_script(script_path: str):
    """Load the player's script and return the module."""
    if not os.path.exists(script_path):
        raise PlayerScriptError(f"Script not found: {script_path}")

    spec = importlib.util.spec_from_file_location("player_solution", script_path)
    module = importlib.util.module_from_spec(spec)

    # Make code_n available to the player script
    sys.modules["player_solution"] = module
    try:
        spec.loader.exec_module(module)
    except Exception as exc:
        raise PlayerScriptError(f"Could not load your script: {type(exc).__name__}: {exc}") from exc

    if not hasattr(module, "solve"):
        raise PlayerScriptError("Your script must define a solve(...) function.")

    return module


def show_pygame_error(challenge, n: int, seed: int | None, speed: str | None, message: str, detail: str = ""):
    """Display a player-facing setup/load error in the Pygame challenge window."""
    from code_n.pygame_renderer import PygameRenderer, VisualRunResult

    reset_counter()
    try:
        challenge.setup(n, seed)
        grid = challenge.grid or Grid(1, 1)
    except Exception:
        grid = Grid(1, 1)
        grid.set(0, 0, CellType.VALUE, value="!")

    visual_result = VisualRunResult(
        passed=False,
        message=message,
        stats=OpStats(),
        actual_complexity=ComplexityClass.O_1,
        required_complexity=challenge.info.required_complexity,
        n=n,
        description=challenge.info.description,
        return_value=detail,
    )
    PygameRenderer(speed=speed or "instant").play(
        grid=grid,
        operations=[],
        title=challenge.info.name,
        result=visual_result,
    )


def main():
    parser = argparse.ArgumentParser(description="Run a cOde(n) challenge")
    parser.add_argument("challenge_id", nargs="?", default=None,
                        help="The challenge ID (e.g., intro_01)")
    parser.add_argument("script", nargs="?", help="Path to your solution script (default: solutions/<challenge_id>.py)")
    parser.add_argument("--n", type=int, default=DEFAULT_N, help=f"Input size (default: {DEFAULT_N}, max: {MAX_N})")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    parser.add_argument("--no-animate", action="store_true", help="Skip animation")
    parser.add_argument("--pygame", action="store_true", help="Show an animated Pygame visualization")
    parser.add_argument(
        "--speed",
        default=None,
        help="Pygame replay speed: step, crawl, very-slow, slow, normal, fast, turbo, instant (or 1-8). If omitted, choose in the Pygame window.",
    )
    parser.add_argument("--list", action="store_true",
                        help="Print all available challenge IDs and their required complexity, then exit.")
    parser.add_argument("--diff", metavar="CHALLENGE_ID", default=None,
                        help="Print a side-by-side summary of the current progress record vs. a fresh run.")

    args = parser.parse_args()

    if args.list:
        _print_challenge_list()
        return

    if args.diff:
        _print_progress_diff(args.diff)
        return

    if not args.challenge_id:
        parser.error("challenge_id is required (or use --list / --diff).")

    # Check challenge exists first, so we can ask the challenge for its
    # own size cap. 2D challenges (BFS/DFS) accept at most 35; 1D
    # challenges accept the global MAX_N of 50.
    progress = load_progress()

    challenge = get_challenge(args.challenge_id)
    if not challenge:
        print(f"\033[91mUnknown challenge: {args.challenge_id}\033[0m")
        sys.exit(1)

    max_n_for_challenge = challenge.max_n
    if args.n > max_n_for_challenge:
        print(
            f"\033[93mNote: --n={args.n} exceeds the maximum of "
            f"{max_n_for_challenge} for {args.challenge_id}. "
            f"Clamping to {max_n_for_challenge} for this run.\033[0m"
        )
        args.n = max_n_for_challenge
    if args.n < 1:
        parser.error("--n must be a positive integer.")

    # Load player script
    solution = resolve_solution_path(args.challenge_id, args.script)
    if not solution.exists:
        solution_path = create_solution_file(
            args.challenge_id,
            challenge.info.name,
            challenge.info.description,
        )
        message = f"Created missing solution script: {os.path.relpath(solution_path, os.path.dirname(os.path.abspath(__file__)))}. Implement solve(...), then run again."
        if args.pygame:
            show_pygame_error(challenge, args.n, args.seed, args.speed, message)
        print(f"\033[93m{message}\033[0m")
        sys.exit(1)

    try:
        player = load_player_script(solution.path)
    except PlayerScriptError as exc:
        message = str(exc)
        progress.fail(args.challenge_id)
        save_progress(progress)
        if args.pygame:
            show_pygame_error(challenge, args.n, args.seed, args.speed, message)
        else:
            print(f"\033[91mError: {message}\033[0m")
            print("Example:")
            print("  def solve(data, n):")
            print("      # your algorithm here")
            print("      return result")
        sys.exit(1)

    # Run the challenge
    print(f"\n\033[1;96m Running: {challenge.info.name} (n={args.n})\033[0m\n")
    print(f"\033[90mSolution: {os.path.relpath(solution.path, os.path.dirname(os.path.abspath(__file__)))}\033[0m")

    try:
        result = challenge.run(
            solve_fn=player.solve,
            n=args.n,
            seed=args.seed,
            animate=(not args.no_animate and not args.pygame),
            pygame=args.pygame,
            pygame_speed=args.speed,
        )
    except Exception:
        progress.fail(args.challenge_id)
        save_progress(progress)
        raise

    # Store the latest run status. DONE only means the latest run passed.
    if result.passed:
        progress.complete(
            args.challenge_id,
            result.stats.total,
            result.actual_complexity.value,
        )
    else:
        progress.fail(args.challenge_id)

    save_progress(progress)

    if not result.passed:
        if result.message:
            print(f"\n\033[91m{result.message}\033[0m")
        print(f"\n\033[93mTry again! Use: python main.py info {args.challenge_id}\033[0m")

    sys.exit(0 if result.passed else 1)


def _print_challenge_list():
    """Pretty-print the catalog of challenges for the CLI."""
    print(f"\n\033[1m{'ID':<14} {'Required':<14} {'Difficulty':<10} Name\033[0m")
    print("-" * 70)
    for cid in list_challenges():
        challenge = get_challenge(cid)
        if not challenge:
            continue
        info = challenge.info
        print(f"{cid:<14} {info.required_complexity.value:<14} {info.difficulty:<10} {info.name}")
    print()
    print("Run one with: python run_challenge.py <challenge_id>")
    print("Show details: python main.py info <challenge_id>")


def _print_progress_diff(challenge_id: str):
    """Print the saved best record for a challenge; useful for checking
    whether a refactor moved the needle."""
    challenge = get_challenge(challenge_id)
    if not challenge:
        print(f"\033[91mUnknown challenge: {challenge_id}\033[0m")
        sys.exit(1)

    progress = load_progress()
    record = progress.records.get(challenge_id)
    status = progress.status_for(challenge_id)

    print(f"\n\033[1m=== {challenge.info.name} ({challenge_id}) ===\033[0m")
    print(f"  Status:     {status}")
    print(f"  Required:   {challenge.info.required_complexity.value}")
    if record is None:
        print("  Best run:   <no completed run yet>")
    else:
        print(f"  Best ops:   {record.best_ops}")
        print(f"  Achieved:   {record.complexity_achieved}")
        print(f"  Attempts:   {record.attempts}")
    print()
    print("Run a fresh attempt: python run_challenge.py", challenge_id)


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
