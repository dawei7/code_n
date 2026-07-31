from typing import List


class Solution:
    def medianOfUniquenessArray(self, nums: List[int]) -> int:
        n = len(nums)
        total_subarrays = n * (n + 1) // 2
        target_rank = (total_subarrays + 1) // 2

        def reaches_target(limit: int) -> bool:
            frequencies = {}
            left = 0
            count = 0

            for right, value in enumerate(nums):
                frequencies[value] = frequencies.get(value, 0) + 1

                while len(frequencies) > limit:
                    outgoing = nums[left]
                    frequencies[outgoing] -= 1
                    if frequencies[outgoing] == 0:
                        del frequencies[outgoing]
                    left += 1

                count += right - left + 1
                if count >= target_rank:
                    return True

            return False

        low = 1
        high = len(set(nums))

        while low < high:
            middle = (low + high) // 2
            if reaches_target(middle):
                high = middle
            else:
                low = middle + 1

        return low
