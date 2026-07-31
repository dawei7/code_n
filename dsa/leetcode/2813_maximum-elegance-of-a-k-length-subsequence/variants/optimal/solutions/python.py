from heapq import heappop, heappush


def solve(items: list[list[int]], k: int) -> int:
    items = sorted(items, reverse=True)
    selected_categories: set[int] = set()
    duplicate_profits: list[int] = []
    total_profit = 0
    for profit, category in items[:k]:
        total_profit += profit
        if category in selected_categories:
            heappush(duplicate_profits, profit)
        else:
            selected_categories.add(category)
    answer = total_profit + len(selected_categories) ** 2
    for profit, category in items[k:]:
        if category in selected_categories or not duplicate_profits:
            continue
        total_profit += profit - heappop(duplicate_profits)
        selected_categories.add(category)
        answer = max(answer, total_profit + len(selected_categories) ** 2)
    return answer
