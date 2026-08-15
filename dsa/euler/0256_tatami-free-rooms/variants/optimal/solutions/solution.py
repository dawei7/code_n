"""Project Euler 256: Tatami-Free Rooms

Find the smallest room-size s for which T(s) = 200, where T(s) is the number
of tatami-free rectangular rooms of even size s.
"""

from __future__ import annotations


def is_tileable(a: int, b: int) -> bool:
    """Returns True if an a x b rectangular room (a <= b, a*b even) can be covered

    with 1x2 tatami mats without 4 corners meeting at any internal point.
    """
    if a <= 2:
        return True
    if a % 2 == 1:
        # For odd a: tileable iff there exists k >= 1 such that k*(a-1) <= b <= k*(a+1)
        return (b + a) // (a + 1) <= b // (a - 1)
    else:
        # For even a: tileable iff there exists k >= 1 such that k*(a-1) - 1 <= b <= k*(a+1) + 1
        return (b - 1 + a) // (a + 1) <= (b + 1) // (a - 1)


def count_free_rooms(divs: list[int], s: int) -> int:
    """Counts the number of tatami-free divisor pairs (a, s//a) with a <= b."""
    cnt = 0
    for a in divs:
        if a * a > s:
            break
        b = s // a
        if not is_tileable(a, b):
            cnt += 1
    return cnt


def solve(target: int = 200) -> str:
    """Finds the smallest room-size s for which T(s) == target using pruned DFS

    over prime factorizations.
    """
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    best_s = 100_000_000

    def dfs(
        p_idx: int, current_val: int, current_divs: list[int], num_divs: int
    ) -> None:
        nonlocal best_s
        if current_val >= best_s:
            return

        # Prune if the number of divisors is insufficient to reach target
        if num_divs >= 2 * target:
            cnt = count_free_rooms(sorted(current_divs), current_val)
            if cnt == target:
                if current_val < best_s:
                    best_s = current_val

        if p_idx >= len(primes):
            return

        p = primes[p_idx]

        # Branch 1: Exponent 0 (skip prime p, valid for p > 2 since s must be even)
        if p_idx > 0:
            dfs(p_idx + 1, current_val, current_divs, num_divs)

        # Branch 2: Exponents e >= 1
        val = current_val
        mult = p
        new_divs = list(current_divs)

        max_e = 20 if p == 2 else (10 if p == 3 else 6)
        for e in range(1, max_e + 1):
            val *= p
            if val >= best_s:
                break

            curr_layer = [d * mult for d in current_divs]
            new_divs.extend(curr_layer)
            mult *= p

            dfs(p_idx + 1, val, new_divs, num_divs * (e + 1))

    dfs(0, 1, [1], 1)
    return str(best_s)


if __name__ == "__main__":
    print(solve())
