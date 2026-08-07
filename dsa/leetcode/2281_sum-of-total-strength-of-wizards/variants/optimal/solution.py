from itertools import accumulate
from typing import List


class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        modulo = 1_000_000_007
        size = len(strength)

        previous_smaller = [-1] * size
        stack = []
        for index, value in enumerate(strength):
            while stack and strength[stack[-1]] >= value:
                stack.pop()
            if stack:
                previous_smaller[index] = stack[-1]
            stack.append(index)

        next_smaller_or_equal = [size] * size
        stack.clear()
        for index in range(size - 1, -1, -1):
            while stack and strength[stack[-1]] > strength[index]:
                stack.pop()
            if stack:
                next_smaller_or_equal[index] = stack[-1]
            stack.append(index)

        prefix_of_prefix = list(accumulate(accumulate(strength, initial=0), initial=0))

        answer = 0
        for index, value in enumerate(strength):
            left = previous_smaller[index]
            right = next_smaller_or_equal[index]

            right_sums = prefix_of_prefix[right + 1] - prefix_of_prefix[index + 1]
            left_sums = prefix_of_prefix[index + 1] - prefix_of_prefix[left + 1]
            total_subarray_sums = right_sums * (index - left) - left_sums * (right - index)
            answer = (answer + value * total_subarray_sums) % modulo

        return answer
