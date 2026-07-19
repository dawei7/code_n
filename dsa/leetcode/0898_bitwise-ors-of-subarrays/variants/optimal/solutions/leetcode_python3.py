from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ending = set()
        results = set()

        for value in arr:
            ending = {value} | {previous | value for previous in ending}
            results.update(ending)

        return len(results)
