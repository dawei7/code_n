from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        minimum = arrays[0][0]
        maximum = arrays[0][-1]
        answer = 0

        for array in arrays[1:]:
            answer = max(answer, array[-1] - minimum, maximum - array[0])
            minimum = min(minimum, array[0])
            maximum = max(maximum, array[-1])
        return answer
