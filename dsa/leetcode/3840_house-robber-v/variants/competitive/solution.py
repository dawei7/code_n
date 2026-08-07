from typing import List


class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        best_two_back = 0
        best_one_back = 0

        for index, money in enumerate(nums):
            if index > 0 and colors[index] != colors[index - 1]:
                take = best_one_back + money
            else:
                take = best_two_back + money

            best_two_back, best_one_back = best_one_back, max(best_one_back, take)

        return best_one_back
