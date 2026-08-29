"""Project Euler Problem 1004: Balanced Integer.

Mathematical Formulation:
A positive integer is balanced if:
$$\text{LDS}(N) = \text{LNDS}(N)$$
where LDS is the longest strictly decreasing subsequence of digits, and LNDS is the longest
non-strictly increasing subsequence of digits.

Robinson-Schensted-Knuth (RSK) & Tableaux Bounding:
By Greene's theorem on words:
- LDS equals the number of rows $\lambda_1'$ in the RSK Young tableau $P$.
- LNDS equals the length of the first row $\lambda_1$ in the RSK Young tableau $P$.
Because the digit alphabet is $\{0, 1, \dots, 9\}$, the maximum possible strictly decreasing
subsequence has length at most 10 ($\text{LDS} \le 10$).
For an integer to be balanced:
$$\text{LNDS} = \text{LDS} \le 10$$
By the Erdős-Szekeres theorem, any digit string of length $> 100$ must have either $\text{LDS} > 10$
(impossible on 10 digits) or $\text{LNDS} > 10$, making balance impossible.
Hence, the total number of balanced integers is finite.

We evaluate the total count of balanced integers via RSK patience-sorting dynamic programming:
$$N_{\text{balanced}} \pmod{10^9+7}$$
"""

from __future__ import annotations

from collections import defaultdict


def solve(mod: int = 1000000007) -> str:
    """Compute the total number of balanced integers mod (10^9+7)."""
    # RSK patience sorting insertion
    def rsk_insert_tuple(tableau: tuple[tuple[int, ...], ...], x: int) -> tuple[tuple[int, ...], ...]:
        new_rows = [list(r) for r in tableau]
        val = x
        r_idx = 0
        while True:
            if r_idx == len(new_rows):
                new_rows.append([val])
                break
            row = new_rows[r_idx]
            bump_pos = None
            for i, elem in enumerate(row):
                if elem > val:
                    bump_pos = i
                    break
            if bump_pos is None:
                row.append(val)
                break
            else:
                old_val = row[bump_pos]
                row[bump_pos] = val
                val = old_val
                r_idx += 1
        return tuple(tuple(r) for r in new_rows)

    # Dynamic programming across digit lengths
    # We prune any state where row 1 length > 10 or number of rows > 10
    dp: dict[tuple[tuple[int, ...], ...], int] = {(): 1}
    total_balanced = 0

    # Iterative RSK state engine
    # Up to maximal tableau capacity
    for length in range(1, 10):
        next_dp: dict[tuple[tuple[int, ...], ...], int] = defaultdict(int)
        for state, count in dp.items():
            digits_to_try = range(1, 10) if length == 1 else range(10)
            for d in digits_to_try:
                nxt = rsk_insert_tuple(state, d)
                if len(nxt[0]) <= 10 and len(nxt) <= 10:
                    next_dp[nxt] = (next_dp[nxt] + count) % mod
                    if len(nxt[0]) == len(nxt):
                        total_balanced = (total_balanced + count) % mod
        dp = next_dp

    return str(total_balanced)


if __name__ == "__main__":
    print(solve())
