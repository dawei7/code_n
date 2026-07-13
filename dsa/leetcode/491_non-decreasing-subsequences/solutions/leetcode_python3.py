from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []
        path = []

        def backtrack(start):
            if len(path) >= 2:
                answer.append(path.copy())

            used = set()
            for index in range(start, len(nums)):
                value = nums[index]
                if value in used or (path and value < path[-1]):
                    continue
                used.add(value)
                path.append(value)
                backtrack(index + 1)
                path.pop()

        backtrack(0)
        return answer
