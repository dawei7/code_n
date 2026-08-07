from collections import defaultdict
from typing import List


class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        total_count = defaultdict(int)
        total_index = defaultdict(int)

        for index, value in enumerate(arr):
            total_count[value] += 1
            total_index[value] += index

        left_count = defaultdict(int)
        left_index = defaultdict(int)
        answer = [0] * len(arr)

        for index, value in enumerate(arr):
            count_left = left_count[value]
            sum_left = left_index[value]
            count_right = total_count[value] - count_left - 1
            sum_right = total_index[value] - sum_left - index

            answer[index] = index * count_left - sum_left + sum_right - index * count_right
            left_count[value] += 1
            left_index[value] += index

        return answer
