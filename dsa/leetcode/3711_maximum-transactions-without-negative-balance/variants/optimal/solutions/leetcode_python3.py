from heapq import heappop, heappush
from typing import List


class Solution:
    def maxTransactions(self, transactions: List[int]) -> int:
        selected = []
        balance = 0

        for amount in transactions:
            heappush(selected, amount)
            balance += amount

            if balance < 0:
                balance -= heappop(selected)

        return len(selected)
