"""Optimal solution for LeetCode 1049: Last Stone Weight II."""


def solve(stones: list[int]) -> int:
    total = sum(stones)
    reachable = {0}

    for stone in stones:
        reachable |= {subtotal + stone for subtotal in reachable}

    best = max(subtotal for subtotal in reachable if subtotal <= total // 2)
    return total - 2 * best
