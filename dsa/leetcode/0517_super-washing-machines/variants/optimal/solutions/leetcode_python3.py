from typing import List


class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        if total % len(machines) != 0:
            return -1

        target = total // len(machines)
        prefix_balance = 0
        moves = 0
        for load in machines:
            excess = load - target
            prefix_balance += excess
            moves = max(moves, excess, abs(prefix_balance))
        return moves
