from functools import lru_cache


def solve(cost: list[list[int]]) -> int:
    first = len(cost)
    second = len(cost[0])
    cheapest_to_second = [min(cost[i][j] for i in range(first)) for j in range(second)]

    @lru_cache(None)
    def search(i: int, mask: int) -> int:
        if i == first:
            return sum(
                cheapest_to_second[j]
                for j in range(second)
                if not mask & (1 << j)
            )
        return min(
            cost[i][j] + search(i + 1, mask | (1 << j))
            for j in range(second)
        )

    return search(0, 0)
