"""Project Euler Problem 391: Hopping Game.

Find sum_{n=1..1000} M(n)^3, where M(n) is the maximum winning first move in the binary popcount
hopping game.
"""

from typing import List, Optional, Union

# A Mapping represents a function f: {0..N} -> {0..N}
Mapping = Union[None, int, List[int]]


def _const_value(table: List[int]) -> Optional[int]:
    """Return the constant value if table is uniform; else None."""
    first = table[0]
    for x in table[1:]:
        if x != first:
            return None
    return first


def _apply_map(m: Mapping, s: int) -> int:
    """Apply mapping m to input s."""
    if m is None:
        return s
    if isinstance(m, int):
        return m
    return m[s]


def _compose(map_a: Mapping, map_b: Mapping) -> Mapping:
    """Return function composition map_a(map_b(s))."""
    if isinstance(map_a, int):
        return map_a
    if isinstance(map_b, int):
        return _apply_map(map_a, map_b)
    if map_a is None:
        return map_b
    if map_b is None:
        return map_a
    return [map_a[x] for x in map_b]


def compute_m(n_val: int) -> int:
    """Compute M(n) using divide-and-conquer popcount block transforms with early saturation."""
    max_k = 40
    width = max_k + 2

    # Base level k=0 maps for offsets off=0..max_k+1
    maps_prev: List[Mapping] = [0] * width
    maps_prev[0] = None

    for off in range(1, width):
        if off > n_val:
            maps_prev[off] = 0
        else:
            lim = n_val - off
            table = [0] * (n_val + 1)
            for s in range(lim + 1):
                table[s] = s + off
            maps_prev[off] = table

    # Iterative composition k=1..max_k until root mapping saturates
    for _ in range(1, max_k + 1):
        maps_curr: List[Mapping] = [0] * width
        for off in range(width - 1):
            maps_curr[off] = _compose(maps_prev[off], maps_prev[off + 1])
        maps_curr[width - 1] = 0

        root = maps_curr[0]
        if not isinstance(root, int) and root is not None:
            c = _const_value(root)
            if c is not None:
                maps_curr[0] = c
                root = c

        if isinstance(root, int):
            return root

        maps_prev = maps_curr

    return 0


def solve(limit: int = 1000) -> int:
    """Compute sum_{n=1..limit} M(n)^3."""
    total = 0
    for n in range(1, limit + 1):
        m_n = compute_m(n)
        total += m_n * m_n * m_n
    return total


if __name__ == "__main__":
    print(solve())
