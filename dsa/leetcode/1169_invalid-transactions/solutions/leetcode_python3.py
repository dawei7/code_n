from collections import defaultdict
from typing import List


class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        groups = defaultdict(list)
        invalid = [False] * len(transactions)
        for index, transaction in enumerate(transactions):
            name, time_text, amount_text, city = transaction.split(",")
            time = int(time_text)
            amount = int(amount_text)
            groups[name].append((time, city, index))
            if amount > 1000:
                invalid[index] = True

        for group in groups.values():
            group.sort()
            city_counts = defaultdict(int)
            left = 0
            right = 0
            for time, city, index in group:
                while right < len(group) and group[right][0] <= time + 60:
                    city_counts[group[right][1]] += 1
                    right += 1
                while group[left][0] < time - 60:
                    old_city = group[left][1]
                    city_counts[old_city] -= 1
                    left += 1
                if right - left > city_counts[city]:
                    invalid[index] = True

        return [transaction for index, transaction in enumerate(transactions) if invalid[index]]
