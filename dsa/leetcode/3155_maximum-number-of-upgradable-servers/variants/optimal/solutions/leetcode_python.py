from typing import List


class Solution:
    def maxUpgrades(
        self,
        count: List[int],
        upgrade: List[int],
        sell: List[int],
        money: List[int],
    ) -> List[int]:
        return [
            min(servers, (cash + servers * sale) // (cost + sale))
            for servers, cost, sale, cash in zip(count, upgrade, sell, money)
        ]

