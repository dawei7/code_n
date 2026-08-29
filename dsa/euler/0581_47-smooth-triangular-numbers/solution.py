"""Project Euler Problem 581: 47-smooth Triangular Numbers.

Find the sum of all indices n such that T(n) = n(n+1)/2 is 47-smooth.
"""

from array import array
from typing import List

_PRIMES_UP_TO_47 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
_LIMIT_47 = 1_109_496_723_126


def solve(
    primes: List[int] = _PRIMES_UP_TO_47, max_limit: int = _LIMIT_47
) -> int:
    """Sum all indices n such that both n and n+1 are smooth w.r.t. primes."""
    smooth = array("Q", [1])

    k = len(primes)
    idx = [0] * k
    next_vals = [p for p in primes]

    prev = 1
    ans = 0

    while True:
        m = min(next_vals)
        if m > max_limit:
            break

        smooth.append(m)

        if m == prev + 1:
            ans += prev
        prev = m

        for j in range(k):
            if next_vals[j] == m:
                idx[j] += 1
                next_vals[j] = primes[j] * smooth[idx[j]]

    return ans


if __name__ == "__main__":
    print(solve())
