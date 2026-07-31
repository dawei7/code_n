from bisect import bisect_left, bisect_right
from typing import List


class Solution:
    def minThreshold(self, nums: List[int], k: int) -> int:
        values = sorted(set(nums))
        size = len(values)

        def count_pairs(threshold: int) -> int:
            tree = [0] * (size + 1)

            def prefix_sum(index: int) -> int:
                total = 0
                while index > 0:
                    total += tree[index]
                    index -= index & -index
                return total

            pairs = 0
            for value in nums:
                pairs += (
                    prefix_sum(bisect_right(values, value + threshold))
                    - prefix_sum(bisect_right(values, value))
                )
                if pairs >= k:
                    return pairs

                index = bisect_left(values, value) + 1
                while index <= size:
                    tree[index] += 1
                    index += index & -index

            return pairs

        high = max(nums) - min(nums)
        if count_pairs(high) < k:
            return -1

        low = 1
        while low < high:
            middle = (low + high) // 2
            if count_pairs(middle) >= k:
                high = middle
            else:
                low = middle + 1

        return low
