from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        visited = [False] * len(nums)
        longest = 0

        for start in range(len(nums)):
            if visited[start]:
                continue

            length = 0
            index = start
            while not visited[index]:
                visited[index] = True
                length += 1
                index = nums[index]

            longest = max(longest, length)

        return longest

