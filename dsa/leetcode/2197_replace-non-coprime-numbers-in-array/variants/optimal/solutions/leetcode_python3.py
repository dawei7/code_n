from math import gcd
from typing import List


class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []

        for value in nums:
            stack.append(value)
            while len(stack) >= 2:
                common = gcd(stack[-2], stack[-1])
                if common == 1:
                    break
                right = stack.pop()
                stack[-1] = stack[-1] // common * right

        return stack
