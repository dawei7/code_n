from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MODULUS = 1_000_000_007
        root = complexity[0]
        if any(value <= root for value in complexity[1:]):
            return 0

        answer = 1
        for factor in range(2, len(complexity)):
            answer = answer * factor % MODULUS
        return answer
