from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losses = {}
        for winner, loser in matches:
            losses.setdefault(winner, 0)
            losses[loser] = losses.get(loser, 0) + 1
        return [
            sorted(player for player, count in losses.items() if count == 0),
            sorted(player for player, count in losses.items() if count == 1),
        ]
