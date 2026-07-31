from bisect import bisect_left


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        first = bisect_left(nums, target)
        majority_offset = first + len(nums) // 2
        return majority_offset < len(nums) and nums[majority_offset] == target
