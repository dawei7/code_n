from bisect import bisect_left
from typing import List


class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0]
        for number in nums:
            prefix.append(prefix[-1] + number)

        n = len(nums)
        answer = []
        for query in queries:
            split = bisect_left(nums, query)
            left_cost = query * split - prefix[split]
            right_cost = prefix[n] - prefix[split] - query * (n - split)
            answer.append(left_cost + right_cost)

        return answer
