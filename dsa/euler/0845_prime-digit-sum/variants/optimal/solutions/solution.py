"""Project Euler Problem 845: Prime Digit Sum.

Mathematical reduction:
Let D(n) be the n-th positive integer whose sum of decimal digits is prime.
We define C(X) as the counting function that returns the number of positive integers <= X
with prime digit sum.

Using Digit Dynamic Programming:
Let dp[len][s] be the number of digit strings of length len with sum s.
The table is built in O(L * max_sum) time where L <= 20 and max_sum <= 180.

To evaluate C(X), we iterate through the digits of X from left to right, accumulating
ways to complete the remaining digits such that (prefix_sum + d + remaining_sum) is prime.

D(n) is found via binary search on X in [1, 10^19] in O(log(10^19) * L * |Primes|) time.
"""

from __future__ import annotations


def _is_prime(num: int) -> bool:
    if num < 2:
        return False
    for p in (2, 3, 5, 7, 11, 13):
        if num % p == 0:
            return num == p
    for d in range(17, int(num**0.5) + 1, 6):
        if num % d == 0 or num % (d + 2) == 0:
            return False
    return True


def solve(n: int = 10**16) -> int:
    """Find D(n), the n-th positive integer with a prime digit sum."""
    primes = [p for p in range(2, 250) if _is_prime(p)]
    max_len = 25
    max_sum = 9 * max_len

    # dp[length][sum]
    dp = [[0] * (max_sum + 1) for _ in range(max_len + 1)]
    dp[0][0] = 1
    for i in range(1, max_len + 1):
        for s in range(max_sum + 1):
            dp[i][s] = sum(dp[i - 1][s - d] for d in range(10) if s >= d)

    def count_up_to(x_val: int) -> int:
        if x_val <= 0:
            return 0
        s_x = str(x_val)
        length = len(s_x)
        count = 0
        prefix_sum = 0
        for i, ch in enumerate(s_x):
            rem_len = length - 1 - i
            d_cur = int(ch)
            for d in range(d_cur):
                cur_sum = prefix_sum + d
                for p in primes:
                    if cur_sum <= p <= cur_sum + 9 * rem_len:
                        count += dp[rem_len][p - cur_sum]
            prefix_sum += d_cur
        if _is_prime(prefix_sum):
            count += 1
        return count

    low = 1
    high = 10**19
    ans = high
    while low <= high:
        mid = (low + high) // 2
        if count_up_to(mid) >= n:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


if __name__ == "__main__":
    print(solve())
