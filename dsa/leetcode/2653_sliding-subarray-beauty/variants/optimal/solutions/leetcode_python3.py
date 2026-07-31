from typing import List


class Solution:
    def getSubarrayBeauty(self, nums: List[int], k: int, x: int) -> List[int]:
        negative_counts = [0] * 51
        beauties = []

        for right, value in enumerate(nums):
            if value < 0:
                negative_counts[-value] += 1

            if right >= k:
                outgoing = nums[right - k]
                if outgoing < 0:
                    negative_counts[-outgoing] -= 1

            if right < k - 1:
                continue

            remaining = x
            beauty = 0
            for magnitude in range(50, 0, -1):
                remaining -= negative_counts[magnitude]
                if remaining <= 0:
                    beauty = -magnitude
                    break
            beauties.append(beauty)

        return beauties
