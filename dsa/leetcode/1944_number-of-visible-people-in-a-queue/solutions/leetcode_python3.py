from typing import List


class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        answer = [0] * len(heights)
        stack = []

        for index in range(len(heights) - 1, -1, -1):
            while stack and heights[index] > stack[-1]:
                stack.pop()
                answer[index] += 1

            if stack:
                answer[index] += 1

            stack.append(heights[index])

        return answer
