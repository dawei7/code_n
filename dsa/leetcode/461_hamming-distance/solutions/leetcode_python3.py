class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        difference = x ^ y
        distance = 0
        while difference:
            difference &= difference - 1
            distance += 1
        return distance
