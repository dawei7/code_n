class Solution:
    def validSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        peaks = [
            i
            for i in range(1, n - 1)
            if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]
        ]

        answer = 0

        for j, peak in enumerate(peaks):
            previous_peak = peaks[j - 1] if j > 0 else -1
            next_peak = peaks[j + 1] if j + 1 < len(peaks) else n

            leftmost = max(0, peak - k, previous_peak + 1)
            rightmost = min(n - 1, peak + k, next_peak - 1)

            left_choices = peak - leftmost + 1
            right_choices = rightmost - peak + 1
            answer += left_choices * right_choices

        return answer
