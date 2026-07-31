from math import gcd
from typing import List


class Solution:
    def maxGcdSum(self, nums: List[int], k: int) -> int:
        states = {}
        answer = 0

        for right, value in enumerate(nums):
            next_states = {value: (right, value)}

            for current_gcd, (left, total) in states.items():
                extended_gcd = gcd(current_gcd, value)
                extended_total = total + value
                previous = next_states.get(extended_gcd)
                if previous is None or left < previous[0]:
                    next_states[extended_gcd] = (left, extended_total)

            for current_gcd, (left, total) in next_states.items():
                if right - left + 1 >= k:
                    answer = max(answer, current_gcd * total)

            states = next_states

        return answer
