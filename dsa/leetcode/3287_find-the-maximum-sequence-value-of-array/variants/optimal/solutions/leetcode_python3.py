from typing import List


class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        def possible_ors(values: List[int]) -> List[set[int]]:
            snapshots = []
            dp = [set() for _ in range(k + 1)]
            dp[0].add(0)

            for value in values:
                for count in range(k, 0, -1):
                    dp[count].update(current | value for current in dp[count - 1])
                snapshots.append(dp[k].copy())

            return snapshots

        prefix = possible_ors(nums)
        suffix = possible_ors(nums[::-1])[::-1]

        return max(
            left_or ^ right_or
            for split in range(k - 1, len(nums) - k)
            for left_or in prefix[split]
            for right_or in suffix[split + 1]
        )
