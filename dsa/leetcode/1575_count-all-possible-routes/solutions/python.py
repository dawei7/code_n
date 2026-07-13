from functools import lru_cache


def solve(locations, start, finish, fuel):
    mod = 10**9 + 7
    n = len(locations)
    if n == 0:
        return 0
    start %= n
    finish %= n
    fuel = max(0, fuel)

    @lru_cache(maxsize=None)
    def dp(city, remaining):
        total = 1 if city == finish else 0
        for nxt in range(n):
            if nxt == city:
                continue
            cost = abs(locations[city] - locations[nxt])
            if cost == 0:
                continue
            if cost <= remaining:
                total += dp(nxt, remaining - cost)
        return total % mod

    return dp(start, fuel)
