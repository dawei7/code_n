from collections import defaultdict
from typing import List


class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        occurrence_count = defaultdict(int)
        position_sum = defaultdict(int)
        occurrence_count[0] = 1

        prefix = 0
        answer = 0
        for index, value in enumerate(arr):
            prefix ^= value
            answer += occurrence_count[prefix] * index - position_sum[prefix]
            occurrence_count[prefix] += 1
            position_sum[prefix] += index + 1

        return answer
