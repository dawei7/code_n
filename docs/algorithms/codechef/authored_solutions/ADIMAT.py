import math
import sys
from collections import Counter, defaultdict


MOD = 1_000_000_007


def divisors(n: int) -> list[int]:
    result = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            result.append(d)
            if d * d != n:
                result.append(n // d)
    return sorted(result)


def mobius_upto(n: int) -> list[int]:
    mu = [1] * (n + 1)
    prime = [True] * (n + 1)
    for p in range(2, n + 1):
        if prime[p]:
            for k in range(p, n + 1, p):
                prime[k] = False
                mu[k] *= -1
            pp = p * p
            for k in range(pp, n + 1, pp):
                mu[k] = 0
    return mu


def partitions(total: int, max_part: int | None = None):
    if max_part is None or max_part > total:
        max_part = total
    if total == 0:
        yield []
        return
    for first in range(max_part, 0, -1):
        for rest in partitions(total - first, first):
            yield [first] + rest


def build_factorials(limit: int) -> tuple[list[int], list[int]]:
    fact = [1] * (limit + 1)
    for i in range(1, limit + 1):
        fact[i] = fact[i - 1] * i % MOD
    inv_fact = [1] * (limit + 1)
    inv_fact[limit] = pow(fact[limit], MOD - 2, MOD)
    for i in range(limit, 0, -1):
        inv_fact[i - 1] = inv_fact[i] * i % MOD
    return fact, inv_fact


def solve(rows: int, cols: int) -> int:
    small = min(rows, cols)
    large = max(rows, cols)
    fact, inv_fact = build_factorials(max(large + (1 << small), small))
    mu = mobius_upto(small)
    pow2 = [1] * (small + 1)
    for i in range(1, small + 1):
        pow2[i] = pow2[i - 1] * 2

    primitive: dict[int, dict[int, int]] = {}
    for length in range(1, small + 1):
        table = {}
        for period in divisors(length):
            count = 0
            for d in divisors(period):
                count += mu[period // d] * (1 << d)
            table[period] = count
        primitive[length] = table

    answer = 0
    for parts in partitions(small):
        counts = Counter(parts)
        perm_count = fact[small]
        for length, amount in counts.items():
            perm_count = perm_count * pow(pow(length, amount, MOD), MOD - 2, MOD) % MOD
            perm_count = perm_count * inv_fact[amount] % MOD

        element_by_orbit = {1: 1}
        for length in parts:
            next_counts = defaultdict(int)
            for current_lcm, current_count in element_by_orbit.items():
                for period, amount in primitive[length].items():
                    next_counts[math.lcm(current_lcm, period)] += current_count * amount
            element_by_orbit = dict(next_counts)

        orbit_counts = {period: amount // period for period, amount in element_by_orbit.items()}
        dp = [0] * (large + 1)
        dp[0] = 1
        for orbit_length, orbit_count in orbit_counts.items():
            ndp = dp[:]
            max_take = large // orbit_length
            coeffs = [1] * (max_take + 1)
            for take in range(1, max_take + 1):
                coeffs[take] = coeffs[take - 1] * (orbit_count + take - 1) % MOD
                coeffs[take] = coeffs[take] * pow(take, MOD - 2, MOD) % MOD
            for used in range(large + 1):
                base = dp[used]
                if not base:
                    continue
                for take in range(1, (large - used) // orbit_length + 1):
                    ndp[used + take * orbit_length] = (
                        ndp[used + take * orbit_length] + base * coeffs[take]
                    ) % MOD
            dp = ndp
        answer = (answer + perm_count * dp[large]) % MOD

    return answer * pow(fact[small], MOD - 2, MOD) % MOD


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    if not data:
        return
    print(solve(data[0], data[1]))


if __name__ == "__main__":
    main()
