"""Import newly published LeetCode problems without rewriting existing packages.

This is the weekly-maintenance entry point. It delegates to the canonical
dataset sync in ``--new-problems-only`` mode, creates each new ``metadata.json``
and ``doc.md`` from the repository template, updates the canonical index and
subsets, and computes an initial estimated Elo from locally available inputs.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.sync_leetcode_dataset import main  # noqa: E402


def import_new_problems(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--page-size",
        type=int,
        default=100,
        help="Number of official problem records requested per page.",
    )
    args = parser.parse_args(argv)
    return main([
        "--new-problems-only",
        "--page-size",
        str(args.page_size),
    ])


if __name__ == "__main__":
    raise SystemExit(import_new_problems(sys.argv[1:]))
