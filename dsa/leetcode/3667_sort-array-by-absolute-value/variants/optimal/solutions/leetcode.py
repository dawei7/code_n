from typing import List


class Solution:
    def sortByAbsoluteValue(self, nums: List[int]) -> List[int]:
        offset = 100
        frequency = [0] * 201
        for value in nums:
            frequency[value + offset] += 1

        answer = [0] * frequency[offset]
        for magnitude in range(1, 101):
            answer.extend([-magnitude] * frequency[offset - magnitude])
            answer.extend([magnitude] * frequency[offset + magnitude])

        return answer
