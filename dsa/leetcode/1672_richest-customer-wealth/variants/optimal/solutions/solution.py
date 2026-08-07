from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        for customer in accounts:
            wealth = 0
            for balance in customer:
                wealth += balance
            richest = max(richest, wealth)
        return richest
