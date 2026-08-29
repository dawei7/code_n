"""Project Euler Problem 505: Bidirectional Recurrence.

Find A(10^12), where A(n) = y_n(1) for the bidirectional recurrence sequence.
"""

from typing import Dict, List, Tuple

MASK = (1 << 60) - 1


def _combine(a: int, b: int, c: int, d: int) -> int:
    return (a * b + c * d) & MASK


def _state_at(k: int) -> Tuple[int, int]:
    if k == 0:
        return 0, 0
    x = 1
    parent = 0
    for bit in range(k.bit_length() - 2, -1, -1):
        if (k >> bit) & 1:
            next_x = _combine(2, x, 3, parent)
        else:
            next_x = _combine(3, x, 2, parent)
        parent = x
        x = next_x
    return x, parent


def _get_cx_cp(depth: int) -> Tuple[int, int]:
    if depth == 0:
        return 1, 0
    cx, cp = 3, 2
    for d in range(1, depth):
        if d & 1:
            ncx = (2 * cx + cp) & MASK
            ncp = (3 * cx) & MASK
        else:
            ncx = (3 * cx + cp) & MASK
            ncp = (2 * cx) & MASK
        cx, cp = ncx, ncp
    return cx, cp


def _evaluate_subtree(k: int, depth: int) -> int:
    x, parent = _state_at(k)
    cx, cp = _get_cx_cp(depth)
    return (cx * x + cp * parent) & MASK


def _collect_blocks(
    start: int,
    depth: int,
    left_length: int,
    blocks: List[Tuple[int, int, bool]],
) -> None:
    size = 1 << depth
    if start + size <= left_length:
        blocks.append((start, depth, False))
        return
    if start >= left_length:
        blocks.append((start, depth, True))
        return

    half = size >> 1
    _collect_blocks(start, depth - 1, left_length, blocks)
    _collect_blocks(start + half, depth - 1, left_length, blocks)


def _block_value(start: int, depth: int, right_side: bool, base: int) -> int:
    leaf_start = base + start
    if not right_side:
        return _evaluate_subtree(leaf_start >> depth, depth)
    if depth == 0:
        x_val, _ = _state_at(leaf_start >> 1)
        return MASK - x_val
    return MASK - _evaluate_subtree(leaf_start >> depth, depth - 1)


def solve(n: int = 10**12) -> int:
    """Compute A(n) using block tree frontier decomposition and linear recurrence minimax folding."""
    if n <= 0:
        raise ValueError("n must be positive")
    if n == 1:
        return 1

    total_nodes = 2 * n - 1
    height = total_nodes.bit_length() - 1
    base = 1 << height
    boundary = 2 * n
    left_length = boundary - base

    blocks: List[Tuple[int, int, bool]] = []
    _collect_blocks(0, height, left_length, blocks)

    values: Dict[int, int] = {}
    for start, depth, right_side in blocks:
        values[(start << 6) | depth] = _block_value(
            start, depth, right_side, base
        )

    def fold(start: int, depth: int) -> int:
        key = (start << 6) | depth
        cached = values.get(key)
        if cached is not None:
            return cached

        half = 1 << (depth - 1)
        left = fold(start, depth - 1)
        right = fold(start + half, depth - 1)
        return max(left, right) if depth & 1 else min(left, right)

    value = fold(0, height)
    return MASK - value if height & 1 else value


if __name__ == "__main__":
    print(solve())
