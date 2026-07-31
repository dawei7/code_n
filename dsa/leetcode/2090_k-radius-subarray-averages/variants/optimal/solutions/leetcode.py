from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        length = len(nums)
        window_length = 2 * k + 1
        averages = [-1] * length

        if window_length > length:
            return averages

        window_sum = sum(nums[:window_length])
        averages[k] = window_sum // window_length

        for center in range(k + 1, length - k):
            window_sum += nums[center + k]
            window_sum -= nums[center - k - 1]
            averages[center] = window_sum // window_length

        return averages
