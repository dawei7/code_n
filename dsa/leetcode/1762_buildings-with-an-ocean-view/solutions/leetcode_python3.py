from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        visible = []
        tallest_to_right = 0

        for index in range(len(heights) - 1, -1, -1):
            if heights[index] > tallest_to_right:
                visible.append(index)
                tallest_to_right = heights[index]

        visible.reverse()
        return visible
