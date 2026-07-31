from typing import List


class Solution:
    def minMergeCost(self, lists: List[List[int]]) -> int:
        list_count = len(lists)
        mask_count = 1 << list_count

        sizes = [0] * mask_count
        for mask in range(1, mask_count):
            lowest_bit = mask & -mask
            owner = lowest_bit.bit_length() - 1
            sizes[mask] = sizes[mask ^ lowest_bit] + len(lists[owner])

        ordered = sorted(
            (value, owner)
            for owner, values in enumerate(lists)
            for value in values
        )
        medians = [0] * mask_count
        for mask in range(1, mask_count):
            target = (sizes[mask] - 1) // 2
            seen = 0
            for value, owner in ordered:
                if mask & (1 << owner):
                    if seen == target:
                        medians[mask] = value
                        break
                    seen += 1

        dp = [0] * mask_count
        infinity = 10**30
        for mask in range(1, mask_count):
            if (mask & (mask - 1)) == 0:
                continue

            best = infinity
            anchor = mask & -mask
            left = (mask - 1) & mask
            while left:
                right = mask ^ left
                if right and left & anchor:
                    best = min(
                        best,
                        dp[left]
                        + dp[right]
                        + sizes[mask]
                        + abs(medians[left] - medians[right]),
                    )
                left = (left - 1) & mask
            dp[mask] = best

        return dp[-1]
