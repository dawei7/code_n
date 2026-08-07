from typing import List


class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        player_count = len(receiver)
        positions = list(range(player_count))
        scores = list(range(player_count))
        jump = receiver[:]
        gain = receiver[:]

        remaining = k
        while remaining:
            if remaining & 1:
                for start in range(player_count):
                    current = positions[start]
                    scores[start] += gain[current]
                    positions[start] = jump[current]

            remaining >>= 1
            if remaining == 0:
                break

            next_jump = [0] * player_count
            next_gain = [0] * player_count
            for player in range(player_count):
                middle = jump[player]
                next_jump[player] = jump[middle]
                next_gain[player] = gain[player] + gain[middle]

            jump = next_jump
            gain = next_gain

        return max(scores)
