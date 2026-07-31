class Solution:
    def minSubarraySort(self, nums: list[int], k: int) -> list[int]:
        answers: list[int] = []
        for start in range(len(nums) - k + 1):
            window = nums[start : start + k]
            left = 0
            while left + 1 < k and window[left] <= window[left + 1]:
                left += 1
            if left == k - 1:
                answers.append(0)
                continue
            right = k - 1
            while window[right - 1] <= window[right]:
                right -= 1
            core_minimum = min(window[left : right + 1])
            core_maximum = max(window[left : right + 1])
            while left > 0 and window[left - 1] > core_minimum:
                left -= 1
            while right + 1 < k and window[right + 1] < core_maximum:
                right += 1
            answers.append(right - left + 1)
        return answers
