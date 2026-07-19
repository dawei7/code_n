from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        modulus = 1_000_000_007
        frequencies = {}
        answer = 0

        for value in nums:
            key = value - int(str(value)[::-1])
            answer = (answer + frequencies.get(key, 0)) % modulus
            frequencies[key] = frequencies.get(key, 0) + 1

        return answer
