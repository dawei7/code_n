from typing import List


class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        stack = [float("inf")]
        total = 0
        for value in arr:
            while stack[-1] <= value:
                middle = stack.pop()
                total += middle * min(stack[-1], value)
            stack.append(value)

        while len(stack) > 2:
            total += stack.pop() * stack[-1]
        return total
