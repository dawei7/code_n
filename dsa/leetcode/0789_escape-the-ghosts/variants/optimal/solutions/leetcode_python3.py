from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        player_distance = abs(target[0]) + abs(target[1])
        return all(
            abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            > player_distance
            for ghost in ghosts
        )
