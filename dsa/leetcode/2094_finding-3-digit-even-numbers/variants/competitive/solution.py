from collections import Counter
from typing import List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        available = Counter(digits)
        answer = []

        for number in range(100, 1000, 2):
            required = Counter(map(int, str(number)))
            if all(required[digit] <= available[digit] for digit in required):
                answer.append(number)

        return answer
