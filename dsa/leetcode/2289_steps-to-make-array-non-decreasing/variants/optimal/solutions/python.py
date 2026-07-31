from typing import List


def solve(nums: List[int]) -> int:
    stack = []
    answer = 0

    for value in reversed(nums):
        rounds = 0
        while stack and value > stack[-1][0]:
            _, right_rounds = stack.pop()
            rounds = max(rounds + 1, right_rounds)
        answer = max(answer, rounds)
        stack.append((value, rounds))

    return answer
