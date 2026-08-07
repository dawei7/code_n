from typing import List


class Solution:
    def minimumAddedCoins(self, coins: List[int], target: int) -> int:
        ordered = sorted(coins)
        index = 0
        reachable = 0
        added = 0

        while reachable < target:
            if index < len(ordered) and ordered[index] <= reachable + 1:
                reachable += ordered[index]
                index += 1
            else:
                reachable += reachable + 1
                added += 1

        return added
