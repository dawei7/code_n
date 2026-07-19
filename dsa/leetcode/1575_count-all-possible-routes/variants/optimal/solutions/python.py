from functools import lru_cache


def solve(locations: list[int], start: int, finish: int, fuel: int) -> int:
    modulus = 1_000_000_007
    city_count = len(locations)

    @lru_cache(maxsize=None)
    def count_from(city: int, remaining: int) -> int:
        total = 1 if city == finish else 0

        for next_city in range(city_count):
            if next_city == city:
                continue

            cost = abs(locations[city] - locations[next_city])
            if cost <= remaining:
                total += count_from(next_city, remaining - cost)

        return total % modulus

    return count_from(start, fuel)
