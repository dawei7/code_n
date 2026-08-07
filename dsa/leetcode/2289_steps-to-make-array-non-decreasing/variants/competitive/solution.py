from typing import List


class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        stack = []
        answer = 0

        for value in nums:
            rounds = 0
            while stack and value >= stack[-1][0]:
                rounds = max(rounds, stack.pop()[1])

            if stack:
                rounds += 1
            else:
                rounds = 0

            answer = max(answer, rounds)
            stack.append((value, rounds))

        return answer
