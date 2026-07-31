class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        seen = set()
        for operations, value in enumerate(reversed(nums), 1):
            if value <= k:
                seen.add(value)
            if len(seen) == k:
                return operations
