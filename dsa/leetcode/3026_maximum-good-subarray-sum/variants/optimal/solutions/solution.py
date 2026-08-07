from typing import List


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        minimum_prefix = {}
        prefix = 0
        answer = None

        for value in nums:
            prefix_after = prefix + value

            for endpoint in (value - k, value + k):
                if endpoint in minimum_prefix:
                    candidate = prefix_after - minimum_prefix[endpoint]
                    answer = candidate if answer is None else max(answer, candidate)

            if value not in minimum_prefix or prefix < minimum_prefix[value]:
                minimum_prefix[value] = prefix
            prefix = prefix_after

        return 0 if answer is None else answer
