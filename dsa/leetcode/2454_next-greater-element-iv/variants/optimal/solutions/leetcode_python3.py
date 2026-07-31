from typing import List


class Solution:
    def secondGreaterElement(self, nums: List[int]) -> List[int]:
        answer = [-1] * len(nums)
        waiting_first = []
        waiting_second = []

        for index, value in enumerate(nums):
            while waiting_second and nums[waiting_second[-1]] < value:
                answer[waiting_second.pop()] = value

            moved = []
            while waiting_first and nums[waiting_first[-1]] < value:
                moved.append(waiting_first.pop())
            while moved:
                waiting_second.append(moved.pop())

            waiting_first.append(index)

        return answer
