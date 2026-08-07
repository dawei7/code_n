from typing import List


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        answer = []
        next_uncovered = 0

        for index, value in enumerate(nums):
            if value != key:
                continue

            start = max(next_uncovered, index - k)
            end = min(len(nums) - 1, index + k)
            if start <= end:
                answer.extend(range(start, end + 1))
                next_uncovered = end + 1

        return answer
