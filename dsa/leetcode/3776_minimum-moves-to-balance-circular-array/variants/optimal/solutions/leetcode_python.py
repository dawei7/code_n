from typing import List


class Solution:
    def minMoves(self, balance: List[int]) -> int:
        if sum(balance) < 0:
            return -1

        negative_index = next(
            (index for index, amount in enumerate(balance) if amount < 0),
            None,
        )
        if negative_index is None:
            return 0

        n = len(balance)
        deficit = -balance[negative_index]
        donors = []
        for index, amount in enumerate(balance):
            if amount > 0:
                clockwise = (index - negative_index) % n
                counterclockwise = (negative_index - index) % n
                donors.append((min(clockwise, counterclockwise), amount))

        donors.sort()
        moves = 0
        for distance, amount in donors:
            transferred = min(deficit, amount)
            moves += transferred * distance
            deficit -= transferred
            if deficit == 0:
                return moves

        return -1
