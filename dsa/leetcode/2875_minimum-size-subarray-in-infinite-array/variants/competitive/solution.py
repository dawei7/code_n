class Solution:
    def minSizeSubarray(self, nums: List[int], target: int) -> int:
        n = len(nums)
        total = sum(nums)
        full_cycles, remainder = divmod(target, total)

        if remainder == 0:
            return full_cycles * n

        left = 0
        window_sum = 0
        best = 2 * n + 1

        for right in range(2 * n):
            window_sum += nums[right % n]
            while window_sum > remainder:
                window_sum -= nums[left % n]
                left += 1
            if window_sum == remainder:
                best = min(best, right - left + 1)

        if best == 2 * n + 1:
            return -1
        return full_cycles * n + best
