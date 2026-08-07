class Solution:
    def judgeCircle(self, moves: str) -> bool:
        horizontal = 0
        vertical = 0
        for move in moves:
            if move == "R":
                horizontal += 1
            elif move == "L":
                horizontal -= 1
            elif move == "U":
                vertical += 1
            else:
                vertical -= 1
        return horizontal == 0 and vertical == 0
