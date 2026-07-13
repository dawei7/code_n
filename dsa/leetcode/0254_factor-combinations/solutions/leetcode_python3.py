from typing import List


class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        combinations = []

        def search(remainder: int, minimum: int, path: List[int]) -> None:
            factor = minimum
            while factor * factor <= remainder:
                if remainder % factor == 0:
                    quotient = remainder // factor
                    combinations.append(path + [factor, quotient])
                    search(quotient, factor, path + [factor])
                factor += 1

        search(n, 2, [])
        return combinations
