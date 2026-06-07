"""cOde(n) - Main game launcher.

Run this to see the challenge tree, check progress, and get instructions.
"""

from challenges.registry import get_challenge, list_challenges
from code_n.branding import BACKSTORY_SHORT, GAME_SUBTITLE, GAME_TITLE, normalize_player_name
from code_n.progress import load_progress, save_progress
from code_n.samples import sample_lines
from code_n.solutions import SOLUTIONS_DIR, ensure_solutions_dir
from code_n.tree import ChallengeTree
import sys
import os

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def print_banner():
    print("\033[1;96m")
    print("==============================================")
    print(f"  {GAME_TITLE}")
    print(f"  {GAME_SUBTITLE}")
    print("==============================================")
    print("\033[0m")


def print_help():
    print("""
\033[1mHow to Play:\033[0m
    1. Look at the challenge tree below to see available challenges.
    2. Pick a challenge (e.g., 'intro_01').
    3. Save your solution as solutions/<challenge_id>.py.
    4. Run it: python run_challenge.py <challenge_id>

\033[1mRules:\033[0m
    - Write normal Python indexing, comparisons, loops, and assignments.
    - The game records operations through list-like and grid-like wrappers.
    - Every read, write, compare, and swap is counted.
    - Your solution must be CORRECT and within the COMPLEXITY THRESHOLD.
    - The threshold is based on operation count, not wall-clock time.

\033[1mCommands:\033[0m
    python main.py                                      Show this menu and challenge tree
    python main.py nav                                  Open the Pygame challenge navigator
    python main.py name <name>                          Set the student's name
    python main.py info <id>                            Show details for a specific challenge
    python main.py reset                                Reset all progress
    python run_challenge.py <challenge_id>              Run a saved solution
    python run_challenge.py <challenge_id> --pygame     Run with graphics
    python run_challenge.py <challenge_id> --pygame --speed step
    python run_challenge.py <challenge_id> --pygame --speed very-slow
    python run_challenge.py <challenge_id> <script.py>  Run a specific script
""")


def show_challenge_info(challenge_id: str):
    challenge = get_challenge(challenge_id)
    if not challenge:
        print(f"\033[91mUnknown challenge: {challenge_id}\033[0m")
        print(f"Available: {', '.join(list_challenges())}")
        return

    info = challenge.info
    print(f"\n\033[1m{'═' * 50}\033[0m")
    print(f"\033[1;93m  {info.id}: {info.name}\033[0m")
    print(f"\033[1m{'═' * 50}\033[0m")
    print(f"\n  Category:   {info.category}")
    print(f"  Difficulty: {'★' * info.difficulty}{'☆' * (10 - info.difficulty)}")
    print(f"  Required:   {info.required_complexity.value}")
    print(f"\n\033[1mDescription:\033[0m")
    for line in info.description.split("\n"):
        print(f"  {line}")
    samples = sample_lines(info.id)
    if samples:
        print(f"\n\033[1mSamples:\033[0m")
        for line in samples:
            print(f"  {line}" if line else "")
    if info.hint:
        print(f"\n\033[1;90mHint: {info.hint}\033[0m")
    print()


def main():
    print_banner()
    ensure_solutions_dir()

    progress = load_progress()
    tree = ChallengeTree()

    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd in ("nav", "pygame", "gui"):
            from code_n.navigation import launch_navigation
            launch_navigation()
            return
        elif cmd == "info" and len(sys.argv) > 2:
            show_challenge_info(sys.argv[2])
            return
        elif cmd == "name":
            raw_name = " ".join(sys.argv[2:]) if len(sys.argv) > 2 else input("Student name: ")
            progress.player_name = normalize_player_name(raw_name)
            save_progress(progress)
            print(f"\033[92mStudent name set to {progress.player_name}.\033[0m")
            return
        elif cmd == "reset":
            from code_n.progress import PlayerProgress, save_progress as sp
            sp(PlayerProgress())
            print("\033[92mProgress reset!\033[0m")
            return
        else:
            show_challenge_info(cmd)
            return

    print_help()
    print(f"\033[1mBackstory:\033[0m {BACKSTORY_SHORT}")
    if progress.player_name:
        print(f"\033[1mStudent:\033[0m {progress.player_name}")
    else:
        print("\033[1mStudent:\033[0m Choose a name with: python main.py name <name>")
    print()
    print(tree.render_tree(progress))

    # Show open challenges
    available = tree.get_available(progress.completed)
    if available:
        print("\n\033[1;92mOpen challenges:\033[0m")
        for node in available:
            print(f"  -> {node.challenge_id}: {node.name}")
        print(f"\n\033[1mSave scripts in:\033[0m {os.path.relpath(SOLUTIONS_DIR, os.path.dirname(os.path.abspath(__file__)))}")
        print("Navigation: python main.py nav")
        print("Example: python run_challenge.py intro_01 --pygame")
        print("Speed presets: slow, normal, fast, turbo, instant")
    print()


if __name__ == "__main__":
    main()
