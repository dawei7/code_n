from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums) - k
        left, right = 0, len(nums) - 1
        while True:
            pivot = nums[(left + right) // 2]
            lower, scan, upper = left, left, right
            while scan <= upper:
                if nums[scan] < pivot:
                    nums[lower], nums[scan] = nums[scan], nums[lower]
                    lower += 1
                    scan += 1
                elif nums[scan] > pivot:
                    nums[scan], nums[upper] = nums[upper], nums[scan]
                    upper -= 1
                else:
                    scan += 1
            if target < lower:
                right = lower - 1
            elif target > upper:
                left = upper + 1
            else:
                return pivot
