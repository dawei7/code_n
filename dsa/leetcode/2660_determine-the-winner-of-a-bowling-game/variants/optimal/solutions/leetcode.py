from typing import List


class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def score(rolls: List[int]) -> int:
            total = 0
            for index, pins in enumerate(rolls):
                doubled = (index >= 1 and rolls[index - 1] == 10) or (index >= 2 and rolls[index - 2] == 10)
                total += pins * (2 if doubled else 1)
            return total

        score1 = score(player1)
        score2 = score(player2)
        if score1 == score2:
            return 0
        return 1 if score1 > score2 else 2
