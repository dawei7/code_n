from bisect import bisect_left
from typing import List


class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        def subset_sums(values: List[int]) -> List[int]:
            sums = [0]
            for value in values:
                sums += [current + value for current in sums]
            return sums

        middle = len(nums) // 2
        left_sums = subset_sums(nums[:middle])
        right_sums = sorted(subset_sums(nums[middle:]))
        answer = abs(goal)

        for left_sum in left_sums:
            target = goal - left_sum
            index = bisect_left(right_sums, target)

            if index < len(right_sums):
                answer = min(answer, abs(target - right_sums[index]))
            if index > 0:
                answer = min(answer, abs(target - right_sums[index - 1]))
            if answer == 0:
                return 0

        return answer
