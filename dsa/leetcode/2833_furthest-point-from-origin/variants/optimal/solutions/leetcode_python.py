class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        displacement = 0
        flexible = 0

        for move in moves:
            if move == "L":
                displacement -= 1
            elif move == "R":
                displacement += 1
            else:
                flexible += 1

        return abs(displacement) + flexible
