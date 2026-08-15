"""Project Euler Problem 543: Prime-Sum Numbers.

Find sum_{k=3..44} S(F(k)), where S(n) is the sum of all P(i, k) over 1 <= i, k <= n,
and P(i, k) = 1 if i is the sum of k primes.
"""

from __future__ import annotations

import math
from typing import Dict, List, Set


def solve(max_k: int = 44) -> int:
    """Compute sum_{k=3..max_k} S(F(k)) using Goldbach/Vinogradov classification and segmented pi sieve."""
    fib: List[int] = [0, 1]
    for _ in range(2, max_k + 1):
        fib.append(fib[-1] + fib[-2])

    targets: Set[int] = set()
    for k in range(3, max_k + 1):
        targets.add(fib[k])
        targets.add(fib[k] - 2)

    max_val = max(targets)
    chunk_size = 2_000_000
    sqrt_max = math.isqrt(max_val)

    base_prime = bytearray(b"\x01") * (sqrt_max + 1)
    base_prime[0] = base_prime[1] = 0
    for i in range(2, math.isqrt(sqrt_max) + 1):
        if base_prime[i]:
            base_prime[i * i : sqrt_max + 1 : i] = b"\x00" * (
                ((sqrt_max - i * i) // i) + 1
            )
    primes = [i for i in range(2, sqrt_max + 1) if base_prime[i]]

    sorted_targets = sorted(targets)
    target_idx = 0
    num_targets = len(sorted_targets)
    pi_dict: Dict[int, int] = {}

    running_pi = 0
    for low in range(0, max_val + 1, chunk_size):
        high = min(low + chunk_size - 1, max_val)
        length = high - low + 1
        seg = bytearray(b"\x01") * length
        if low == 0:
            seg[0] = seg[1] = 0

        for p in primes:
            start = ((low + p - 1) // p) * p
            if start < p * p:
                start = p * p
            if start <= high:
                seg[start - low : length : p] = b"\x00" * (
                    ((high - start) // p) + 1
                )

        seg_prefix = [0] * (length + 1)
        for i in range(length):
            seg_prefix[i + 1] = seg_prefix[i] + seg[i]

        while target_idx < num_targets and sorted_targets[target_idx] <= high:
            t_val = sorted_targets[target_idx]
            pi_dict[t_val] = running_pi + seg_prefix[t_val - low + 1]
            target_idx += 1

        running_pi += seg_prefix[length]

    def s_calc(n_val: int) -> int:
        if n_val < 2:
            return 0
        ans = pi_dict[n_val]
        if n_val >= 4:
            ans += n_val // 2 - 1
        if n_val >= 5:
            ans += pi_dict[n_val - 2] - 1
        if n_val >= 6:
            m = n_val // 2
            ans += (m - 2) * (n_val - m - 2)
        return ans

    return sum(s_calc(fib[k]) for k in range(3, max_k + 1))


if __name__ == "__main__":
    print(solve())
