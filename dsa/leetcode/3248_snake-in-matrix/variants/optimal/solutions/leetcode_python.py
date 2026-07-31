from typing import List


class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        movement = {
            "UP": -n,
            "RIGHT": 1,
            "DOWN": n,
            "LEFT": -1,
        }
        return sum(movement[command] for command in commands)
