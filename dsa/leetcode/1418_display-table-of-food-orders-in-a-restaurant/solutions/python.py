"""Optimal app-local solution for LeetCode 1418."""

from collections import Counter, defaultdict


def solve(orders: list[list[str]]) -> list[list[str]]:
    counts: dict[int, Counter[str]] = defaultdict(Counter)
    foods: set[str] = set()
    for _, table_text, food in orders:
        table = int(table_text)
        counts[table][food] += 1
        foods.add(food)

    ordered_foods = sorted(foods)
    display = [["Table", *ordered_foods]]
    for table in sorted(counts):
        display.append([str(table), *(str(counts[table][food]) for food in ordered_foods)])
    return display
