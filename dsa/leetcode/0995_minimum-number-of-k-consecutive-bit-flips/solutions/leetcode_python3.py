from typing import List


class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        active_parity = 0
        flips = 0

        for index in range(len(nums)):
            if index >= k and nums[index - k] == 2:
                active_parity ^= 1

            if nums[index] == active_parity:
                if index + k > len(nums):
                    return -1
                nums[index] = 2
                active_parity ^= 1
                flips += 1

        return flips
