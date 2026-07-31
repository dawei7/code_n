from typing import List


class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        width = valueDiff + 1
        buckets = {}
        for index, value in enumerate(nums):
            bucket = value // width
            if bucket in buckets:
                return True
            if bucket - 1 in buckets and value - buckets[bucket - 1] <= valueDiff:
                return True
            if bucket + 1 in buckets and buckets[bucket + 1] - value <= valueDiff:
                return True
            buckets[bucket] = value
            if index >= indexDiff:
                buckets.pop(nums[index - indexDiff] // width, None)
        return False
