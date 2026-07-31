from bisect import bisect_right


def solve(items: list[list[int]], queries: list[int]) -> list[int]:
    items.sort()
    prices = []
    prefix_beauty = []
    best = 0

    for price, beauty in items:
        best = max(best, beauty)
        prices.append(price)
        prefix_beauty.append(best)

    answer = []
    for query in queries:
        index = bisect_right(prices, query) - 1
        answer.append(prefix_beauty[index] if index >= 0 else 0)
    return answer
