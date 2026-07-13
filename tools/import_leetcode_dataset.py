"""Compatibility wrapper for the complete LeetCode dataset sync."""

from __future__ import annotations

import sys

from tools.sync_leetcode_dataset import main


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
