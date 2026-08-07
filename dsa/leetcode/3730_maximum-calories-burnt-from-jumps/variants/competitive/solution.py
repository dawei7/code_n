class Solution:
    def maxCaloriesBurnt(self, heights: list[int]) -> int:
        heights.sort()
        left = 0
        right = len(heights) - 1
        previous = 0
        result = 0

        while left <= right:
            current = heights[right]
            right -= 1
            result += (previous - current) ** 2
            previous = current

            if left <= right:
                current = heights[left]
                left += 1
                result += (previous - current) ** 2
                previous = current

        return result
