from math import comb
from typing import List


class Solution:
    def waysToFillArray(self, queries: List[List[int]]) -> List[int]:
        modulo = 1_000_000_007
        answers = []

        for length, product in queries:
            ways = 1
            divisor = 2
            remaining = product

            while divisor * divisor <= remaining:
                exponent = 0
                while remaining % divisor == 0:
                    remaining //= divisor
                    exponent += 1
                if exponent:
                    ways = (
                        ways
                        * comb(length + exponent - 1, exponent)
                        % modulo
                    )
                divisor += 1

            if remaining > 1:
                ways = ways * length % modulo
            answers.append(ways)

        return answers
