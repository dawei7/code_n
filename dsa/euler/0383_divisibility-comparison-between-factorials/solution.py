"""Project Euler Problem 383: Divisibility Comparison Between Factorials.

Find T_5(10^18), the number of integers 1 <= i <= 10^18 satisfying f_5((2i-1)!) < 2*f_5(i!).
"""

from functools import lru_cache
from typing import Dict, List, Tuple


def base5_digits_msd(n_val: int) -> List[int]:
    """Return base-5 digits of n as a list [MSD..LSD]."""
    if n_val <= 0:
        return [0]
    digs: List[int] = []
    while n_val > 0:
        digs.append(n_val % 5)
        n_val //= 5
    return digs[::-1]


def build_reverse_transitions() -> (
    Dict[Tuple[int, int, int], List[Tuple[int, int, int]]]
):
    """Precompute reverse transitions for the base-5 carry/borrow automaton."""
    rev: Dict[Tuple[int, int, int], List[Tuple[int, int, int]]] = {}
    for carry_in in (0, 1):
        for borrow_in in (0, 1):
            for d in range(5):
                raw0 = 2 * d + carry_in - borrow_in
                if raw0 < 0:
                    raw = raw0 + 5
                    borrow_out = 1
                else:
                    raw = raw0
                    borrow_out = 0
                e = raw % 5
                carry_out = raw // 5
                key = (carry_out, borrow_out, d)
                rev.setdefault(key, []).append((carry_in, borrow_in, e))
    return rev


def solve(limit: int = 10**18) -> int:
    """Compute T_5(limit) using backward-directed base-5 digit dynamic programming."""
    digits = base5_digits_msd(limit)
    length = len(digits)
    rev = build_reverse_transitions()

    @lru_cache(maxsize=None)
    def dfs(
        pos: int,
        tight: int,
        carry_next: int,
        borrow_next: int,
        delta: int,
    ) -> int:
        if pos == length:
            return (
                1
                if (carry_next == 0 and borrow_next == 1 and delta >= 0)
                else 0
            )

        lim = digits[pos] if tight else 4
        total = 0

        for d in range(lim + 1):
            tight2 = 1 if (tight and d == lim) else 0
            key = (carry_next, borrow_next, d)
            if key not in rev:
                continue
            for carry_prev, borrow_prev, e in rev[key]:
                total += dfs(
                    pos + 1,
                    tight2,
                    carry_prev,
                    borrow_prev,
                    delta + e - 2 * d,
                )
        return total

    ans = 0
    for carry_final in (0, 1):
        ans += dfs(0, 1, carry_final, 0, carry_final)

    return ans


if __name__ == "__main__":
    print(solve())
