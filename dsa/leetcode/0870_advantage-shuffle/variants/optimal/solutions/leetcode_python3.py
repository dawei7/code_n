from typing import List


class Solution:
    def advantageCount(
        self, nums1: List[int], nums2: List[int]
    ) -> List[int]:
        available = sorted(nums1)
        opponents = sorted(
            ((value, index) for index, value in enumerate(nums2)),
            reverse=True,
        )
        result = [0] * len(nums1)
        smallest = 0
        largest = len(available) - 1

        for opponent, index in opponents:
            if available[largest] > opponent:
                result[index] = available[largest]
                largest -= 1
            else:
                result[index] = available[smallest]
                smallest += 1

        return result
