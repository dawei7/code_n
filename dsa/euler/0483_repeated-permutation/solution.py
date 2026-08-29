"""Project Euler Problem 483: Repeated Permutation.

Find g(350) written in scientific notation rounded to 10 significant digits,
where g(n) is the average value of f^2(P) over all permutations P in S_n.
"""

from math import gcd
from typing import Dict, List, Tuple


def _lcm(a: int, b: int) -> int:
    return a // gcd(a, b) * b


def _largest_prime_factors(n: int) -> Tuple[List[int], List[int]]:
    lpf = [0] * (n + 1)
    primes: List[int] = []
    for p in range(2, n + 1):
        if lpf[p] != 0:
            continue
        primes.append(p)
        for m in range(p, n + 1, p):
            lpf[m] = p
    return lpf, primes


def _format_sci_10(x: float) -> str:
    s = f"{x:.9e}"
    mant, exp = s.split("e")
    return f"{mant}e{int(exp)}"


def solve(n: int = 350) -> str:
    """Compute g(n) using cycle-type partition DP with prime-power LCM state compression."""
    lpf, primes = _largest_prime_factors(n)
    by_lpf: List[List[int]] = [[] for _ in range(n + 1)]
    for c in range(2, n + 1):
        by_lpf[lpf[c]].append(c)

    dp: List[Dict[int, float]] = [dict() for _ in range(n + 1)]
    dp[0][1] = 1.0
    fixed_weight = 1.0
    for used in range(1, n + 1):
        fixed_weight /= used
        dp[used][1] = fixed_weight

    for p in reversed(primes):
        for c in by_lpf[p]:
            new_dp = [d.copy() for d in dp]

            factors: List[float] = []
            term = 1.0
            for m in range(1, n // c + 1):
                term /= c * m
                factors.append(term)

            for used in range(n - c + 1):
                d = dp[used]
                if not d:
                    continue
                max_m = (n - used) // c
                for l0, v0 in d.items():
                    l1 = _lcm(l0, c)
                    used1 = used
                    for m in range(max_m):
                        used1 += c
                        nd = new_dp[used1]
                        val = v0 * factors[m]
                        try:
                            nd[l1] += val
                        except KeyError:
                            nd[l1] = val

            dp = new_dp

        p2 = float(p * p)
        for used, d in enumerate(dp):
            if not d:
                continue
            compressed: Dict[int, float] = {}
            for l_val, v in d.items():
                cur_l = l_val
                val = v
                while cur_l % p == 0:
                    cur_l //= p
                    val *= p2
                try:
                    compressed[cur_l] += val
                except KeyError:
                    compressed[cur_l] = val
            dp[used] = compressed

    ans = sum(float(l_val * l_val) * v for l_val, v in dp[n].items())
    return _format_sci_10(ans)


if __name__ == "__main__":
    print(solve())
