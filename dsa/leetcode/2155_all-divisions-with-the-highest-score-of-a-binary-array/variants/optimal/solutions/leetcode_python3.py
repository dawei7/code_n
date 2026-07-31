from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        score = sum(nums)
        best = score
        answer = [0]

        for index, value in enumerate(nums, start=1):
            score += 1 if value == 0 else -1
            if score > best:
                best = score
                answer = [index]
            elif score == best:
                answer.append(index)

        return answer
