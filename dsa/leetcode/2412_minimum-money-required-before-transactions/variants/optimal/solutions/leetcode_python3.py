from typing import List


class Solution:
    def minimumMoney(self, transactions: List[List[int]]) -> int:
        unavoidable_loss = sum(
            max(0, cost - cashback)
            for cost, cashback in transactions
        )
        final_bottleneck = max(
            min(cost, cashback)
            for cost, cashback in transactions
        )
        return unavoidable_loss + final_bottleneck
