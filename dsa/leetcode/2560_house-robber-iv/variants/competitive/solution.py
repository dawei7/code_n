class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        low = min(nums)
        high = max(nums)

        while low < high:
            capability = (low + high) // 2
            robbed = 0
            index = 0

            while index < len(nums):
                if nums[index] <= capability:
                    robbed += 1
                    index += 2
                else:
                    index += 1

            if robbed >= k:
                high = capability
            else:
                low = capability + 1

        return low
