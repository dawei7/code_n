from collections import defaultdict
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [0] * n

        count = defaultdict(int)
        total = defaultdict(int)
        for i, value in enumerate(nums):
            answer[i] += count[value] * i - total[value]
            count[value] += 1
            total[value] += i

        count.clear()
        total.clear()
        for i in range(n - 1, -1, -1):
            value = nums[i]
            answer[i] += total[value] - count[value] * i
            count[value] += 1
            total[value] += i

        return answer
