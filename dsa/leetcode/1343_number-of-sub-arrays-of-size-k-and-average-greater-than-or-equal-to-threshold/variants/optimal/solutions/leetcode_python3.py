from typing import List


class Solution:
    def numOfSubarrays(
        self, arr: List[int], k: int, threshold: int
    ) -> int:
        target = k * threshold
        window_sum = sum(arr[:k])
        qualifying = int(window_sum >= target)

        for right in range(k, len(arr)):
            window_sum += arr[right] - arr[right - k]
            if window_sum >= target:
                qualifying += 1

        return qualifying
