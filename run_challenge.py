"""Run a challenge with a player's solution script.

Usage: python run_challenge.py <challenge_id> [player_script.py] [--n SIZE] [--seed SEED] [--no-animate] [--pygame] [--speed PRESET]

The player script must define a function called `solve` that accepts
the challenge's parameters and returns the expected result.

If no script path is supplied, cOde(n) loads solutions/<challenge_id>.py.
"""

from challenges.registry import get_challenge
from code_n.counter import ComplexityClass, OpStats, reset_counter
from code_n.grid import CellType, Grid
from code_n.tree import ChallengeTree
from code_n.progress import load_progress, save_progress
from code_n.solutions import create_solution_file, resolve_solution_path
import sys
import os
import importlib.util
import argparse

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


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
    parser.add_argument("challenge_id", help="The challenge ID (e.g., intro_01)")
    parser.add_argument("script", nargs="?", help="Path to your solution script (default: solutions/<challenge_id>.py)")
    parser.add_argument("--n", type=int, default=16, help="Input size (default: 16)")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for reproducibility")
    parser.add_argument("--no-animate", action="store_true", help="Skip animation")
    parser.add_argument("--pygame", action="store_true", help="Show an animated Pygame visualization")
    parser.add_argument(
        "--speed",
        default=None,
        help="Pygame replay speed: step, crawl, very-slow, slow, normal, fast, turbo, instant (or 1-8). If omitted, choose in the Pygame window.",
    )

    args = parser.parse_args()

    # Check challenge exists and is unlocked
    progress = load_progress()
    tree = ChallengeTree()

    challenge = get_challenge(args.challenge_id)
    if not challenge:
        print(f"\033[91mUnknown challenge: {args.challenge_id}\033[0m")
        sys.exit(1)

    if not tree.is_unlocked(args.challenge_id, progress.completed):
        print(f"\033[91mChallenge '{args.challenge_id}' is locked!\033[0m")
        print("Complete its prerequisites first.")
        parents = tree.get_parents(args.challenge_id)
        for p in parents:
            status = "OK" if p.challenge_id in progress.completed else "--"
            print(f"  {status} {p.challenge_id}: {p.name}")
        sys.exit(1)

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

    result = challenge.run(
        solve_fn=player.solve,
        n=args.n,
        seed=args.seed,
        animate=(not args.no_animate and not args.pygame),
        pygame=args.pygame,
        pygame_speed=args.speed,
    )

    # Update progress if passed
    if result.passed:
        progress.complete(
            args.challenge_id,
            result.stats.total,
            result.actual_complexity.value,
        )
        save_progress(progress)

        # Show what's unlocked
        newly_available = tree.get_available(progress.completed)
        if newly_available:
            print("\n\033[1;92mNewly unlocked:\033[0m")
            for node in newly_available:
                print(f"  -> {node.challenge_id}: {node.name}")
    else:
        print(f"\n\033[93mTry again! Use: python main.py info {args.challenge_id}\033[0m")

    sys.exit(0 if result.passed else 1)


if __name__ == "__main__":
    main()
