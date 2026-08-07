from typing import List


class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        counts = [[0] * 11 for _ in range(n)]
        won = [False] * n
        winners = 0

        for player, color in pick:
            counts[player][color] += 1
            if not won[player] and counts[player][color] > player:
                won[player] = True
                winners += 1

        return winners
