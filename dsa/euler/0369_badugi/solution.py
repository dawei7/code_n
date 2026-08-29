"""Project Euler Problem 369: Badugi.

Find sum_{n=4..13} f(n), where f(n) is the number of n-card hands containing a 4-card Badugi subset.
"""

from math import factorial
from typing import List, Tuple


def solve(min_n: int = 4, max_n: int = 13) -> int:
    """Compute sum_{n=min_n..max_n} f(n) via Hall's Marriage Theorem and rank-pattern partition DFS."""
    if max_n < min_n or max_n < 4:
        return 0

    weights = [bin(v).count("1") for v in range(16)]

    # Precompute the 15 non-empty subsets of the 4 suits and their intersecting rank-patterns
    subsets_s: List[Tuple[int, List[int]]] = []
    for s_mask in range(1, 16):
        size_s = bin(s_mask).count("1")
        intersecting_indices = [
            v - 1 for v in range(1, 16) if (v & s_mask) > 0
        ]
        subsets_s.append((size_s, intersecting_indices))

    fact = [factorial(i) for i in range(14)]

    def get_multinomial_ways(c_tuple: Tuple[int, ...], k_ranks: int) -> int:
        res = fact[13] // fact[13 - k_ranks]
        for c in c_tuple:
            if c > 1:
                res //= fact[c]
        return res

    def satisfies_hall_condition(c_tuple: Tuple[int, ...]) -> bool:
        """Check Hall's Marriage Condition: for every subset of suits S, N(S) >= |S|."""
        for size_s, pattern_indices in subsets_s:
            cnt = 0
            for idx in pattern_indices:
                cnt += c_tuple[idx]
            if cnt < size_s:
                return False
        return True

    f_counts = [0] * (max_n + 1)

    # DFS over rank-pattern multiplicities c_1, ..., c_15
    def dfs(
        pattern_idx: int,
        curr_cards: int,
        curr_ranks: int,
        tuple_so_far: Tuple[int, ...],
    ) -> None:
        if pattern_idx == 16:
            if min_n <= curr_cards <= max_n:
                if satisfies_hall_condition(tuple_so_far):
                    ways = get_multinomial_ways(tuple_so_far, curr_ranks)
                    f_counts[curr_cards] += ways
            return

        w = weights[pattern_idx]
        max_c = (max_n - curr_cards) // w
        for c in range(max_c + 1):
            if curr_ranks + c <= 13:
                dfs(
                    pattern_idx + 1,
                    curr_cards + c * w,
                    curr_ranks + c,
                    tuple_so_far + (c,),
                )

    dfs(1, 0, 0, ())

    return sum(f_counts[min_n : max_n + 1])


if __name__ == "__main__":
    print(solve())
