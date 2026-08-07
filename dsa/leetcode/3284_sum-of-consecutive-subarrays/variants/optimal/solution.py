from typing import List


class Solution:
    def getSum(self, nums: List[int]) -> int:
        modulus = 1_000_000_007
        increasing_count = decreasing_count = 1
        increasing_sum = decreasing_sum = nums[0]
        answer = nums[0]

        for index in range(1, len(nums)):
            value = nums[index]

            if value - nums[index - 1] == 1:
                increasing_count += 1
                increasing_sum += increasing_count * value
            else:
                increasing_count = 1
                increasing_sum = value

            if value - nums[index - 1] == -1:
                decreasing_count += 1
                decreasing_sum += decreasing_count * value
            else:
                decreasing_count = 1
                decreasing_sum = value

            increasing_sum %= modulus
            decreasing_sum %= modulus
            answer = (answer + increasing_sum + decreasing_sum - value) % modulus

        return answer
