from collections import Counter, defaultdict
from typing import List


class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        counts = defaultdict(Counter)
        foods = set()
        for _, table_text, food in orders:
            table = int(table_text)
            counts[table][food] += 1
            foods.add(food)

        ordered_foods = sorted(foods)
        display = [["Table", *ordered_foods]]
        for table in sorted(counts):
            display.append([str(table), *(str(counts[table][food]) for food in ordered_foods)])
        return display
