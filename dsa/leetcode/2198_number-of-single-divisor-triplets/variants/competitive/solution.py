from collections import Counter
from typing import List


class Solution:
    def singleDivisorTriplet(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        values = sorted(frequency)
        answer = 0

        for i, first in enumerate(values):
            for j in range(i, len(values)):
                second = values[j]
                for k in range(j, len(values)):
                    third = values[k]
                    total = first + second + third
                    divisible = (total % first == 0) + (total % second == 0) + (total % third == 0)
                    if divisible != 1:
                        continue

                    if first == third:
                        ways = frequency[first] * (frequency[first] - 1) * (frequency[first] - 2)
                    elif first == second:
                        ways = 3 * frequency[first] * (frequency[first] - 1) * frequency[third]
                    elif second == third:
                        ways = 3 * frequency[first] * frequency[second] * (frequency[second] - 1)
                    else:
                        ways = 6 * frequency[first] * frequency[second] * frequency[third]
                    answer += ways

        return answer
