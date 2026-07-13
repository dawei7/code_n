from functools import lru_cache


def solve(n: int) -> float:
    if n >= 4800:
        return 1.0
    units = (n + 24) // 25

    @lru_cache(maxsize=None)
    def probability(soup_a: int, soup_b: int) -> float:
        if soup_a <= 0 and soup_b <= 0:
            return 0.5
        if soup_a <= 0:
            return 1.0
        if soup_b <= 0:
            return 0.0
        return 0.25 * (
            probability(soup_a - 4, soup_b)
            + probability(soup_a - 3, soup_b - 1)
            + probability(soup_a - 2, soup_b - 2)
            + probability(soup_a - 1, soup_b - 3)
        )

    return probability(units, units)
