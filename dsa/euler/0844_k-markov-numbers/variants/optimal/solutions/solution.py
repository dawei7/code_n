"""Project Euler Problem 844: k-Markov Numbers.

Mathematical reduction:
A k-Markov equation is:
  sum_{i=1}^k x_i^2 = k prod_{i=1}^k x_i.

By Vieta jumping, all positive integer solutions form trees rooted at (1, 1, ..., 1).
From any solution tuple, replacing coordinate x_i produces:
  x_i' = k prod_{j != i} x_j - x_i.

For a given bound N = 10^18:
1. For k > sqrt(N) = 10^9:
   The only k-Markov numbers <= N are {1, k - 1}.
   Their sum is M_k(N) = k.
   The sum over k in (10^9, 10^{18}] is evaluated in O(1) by arithmetic progression sum.

2. For k in (10^6, 10^9]:
   The only k-Markov numbers <= N are {1, k - 1, k^2 - k - 1}.
   Their sum is M_k(N) = k^2 - 1.
   The sum over k in (10^6, 10^9] is evaluated in O(1) using sum of squares formula.

3. For k in [3, 10^6]:
   The Markov tree has sparse states (tuples represented solely by their non-1 elements).
   DFS traverses all reachable Markov numbers <= N in under 3 seconds.
"""

from __future__ import annotations


def solve(max_k: int = 10**18, max_n: int = 10**18, mod: int = 1405695061) -> int:
    """Compute S(max_k, max_n) modulo 1405695061."""
    # 1. Closed-form range 1: k in (k_cut, max_k]
    k_cut = 1000000000
    if max_k > k_cut:
        cnt1 = (max_k - k_cut) % mod
        sum_k_first = (k_cut + 1) % mod
        sum_k_last = max_k % mod
        sum_part1 = cnt1 * (sum_k_first + sum_k_last) % mod * pow(2, mod - 2, mod) % mod
    else:
        sum_part1 = 0
        k_cut = max_k

    # 2. Closed-form range 2: k in (k_3, k_cut]
    k_3 = 1000000

    def sum_sq(n: int) -> int:
        n %= mod
        return n * (n + 1) % mod * (2 * n + 1) % mod * pow(6, mod - 2, mod) % mod

    if k_cut > k_3:
        sum_sq_range = (sum_sq(k_cut) - sum_sq(k_3) + mod) % mod
        sum_1_range = (k_cut - k_3) % mod
        sum_part2 = (sum_sq_range - sum_1_range + mod) % mod
    else:
        sum_part2 = 0
        k_3 = min(max_k, k_3)

    # 3. Dynamic sparse DFS for k in [3, k_3]
    sum_part3 = 0
    for k in range(3, k_3 + 1):
        nums: set[int] = {1}
        stack: list[tuple[int, ...]] = [()]
        while stack:
            v = stack.pop()
            m = len(v)
            p = 1
            for x in v:
                p *= x

            # Jump on a 1 (if m < k)
            if m < k:
                x_new = k * p - 1
                max_v = v[-1] if m > 0 else 1
                if max_v < x_new <= max_n:
                    nums.add(x_new)
                    stack.append(tuple(sorted(v + (x_new,))))

            # Jump on existing non-1 coordinates
            for i in range(m):
                if i > 0 and v[i] == v[i - 1]:
                    continue
                x_new = k * (p // v[i]) - v[i]
                if x_new > v[-1] and x_new <= max_n:
                    nums.add(x_new)
                    stack.append(tuple(sorted(v[:i] + v[i + 1 :] + (x_new,))))

        sum_part3 = (sum_part3 + sum(nums)) % mod

    return (sum_part1 + sum_part2 + sum_part3) % mod


if __name__ == "__main__":
    print(solve())
