from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        counts = [0] * 1001
        for value in arr1:
            counts[value] += 1

        answer: List[int] = []
        for value in arr2:
            answer.extend([value] * counts[value])
            counts[value] = 0

        for value, frequency in enumerate(counts):
            answer.extend([value] * frequency)
        return answer
