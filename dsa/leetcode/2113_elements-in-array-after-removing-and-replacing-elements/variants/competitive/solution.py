from typing import List


class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        size = len(nums)
        period = 2 * size
        answers: List[int] = []

        for time, index in queries:
            phase = time % period
            if phase < size:
                shifted_index = phase + index
                answers.append(nums[shifted_index] if shifted_index < size else -1)
            else:
                restored_length = phase - size
                answers.append(nums[index] if index < restored_length else -1)

        return answers
