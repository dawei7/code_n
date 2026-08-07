class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        first_distance = abs(x - z)
        second_distance = abs(y - z)
        if first_distance == second_distance:
            return 0
        if first_distance < second_distance:
            return 1
        return 2
