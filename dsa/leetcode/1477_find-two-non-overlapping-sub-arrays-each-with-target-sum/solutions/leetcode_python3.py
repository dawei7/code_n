from typing import List


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        infinity = len(arr) + 1
        best_until = [infinity] * len(arr)
        best_length = infinity
        answer = infinity
        left = 0
        window_sum = 0

        for right, value in enumerate(arr):
            window_sum += value

            while window_sum > target:
                window_sum -= arr[left]
                left += 1

            if window_sum == target:
                current_length = right - left + 1
                if left > 0 and best_until[left - 1] != infinity:
                    answer = min(
                        answer,
                        current_length + best_until[left - 1],
                    )
                best_length = min(best_length, current_length)

            best_until[right] = best_length

        return -1 if answer == infinity else answer
