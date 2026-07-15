from typing import List


class Solution:
    def findSolution(
        self, customfunction: "CustomFunction", z: int
    ) -> List[List[int]]:
        result = []
        x, y = 1, z
        while x <= z and y >= 1:
            value = customfunction.f(x, y)
            if value < z:
                x += 1
            elif value > z:
                y -= 1
            else:
                result.append([x, y])
                x += 1
                y -= 1
        return result
