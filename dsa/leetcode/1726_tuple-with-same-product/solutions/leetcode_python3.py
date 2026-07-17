from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pair_count = defaultdict(int)
        answer = 0

        for right in range(len(nums)):
            for left in range(right):
                product = nums[left] * nums[right]
                answer += 8 * pair_count[product]
                pair_count[product] += 1

        return answer
