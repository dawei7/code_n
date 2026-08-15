"""Project Euler Problem 477: Number Sequence Game.

Find F(10^8), the score of Player 1 under optimal minimax play on sequence S
defined by s_1 = 0, s_{i+1} = (s_i^2 + 45) mod 1_000_000_007.
"""

from typing import List

MOD = 1_000_000_007


def solve(n: int = 10**8) -> int:
    """Compute F(n) using online 3-element stack reduction and bitonic minimax sweep."""
    s = 0
    stack: List[int] = []
    total_sum = 0

    for _ in range(n):
        total_sum += s
        stack.append(s)
        while len(stack) >= 3 and stack[-3] <= stack[-2] >= stack[-1]:
            val = stack[-3] - stack[-2] + stack[-1]
            stack.pop()
            stack.pop()
            stack[-1] = val
        s = (s * s + 45) % MOD

    left = 0
    right = len(stack) - 1
    diff = 0
    turn = 1

    while left <= right:
        if stack[left] >= stack[right]:
            diff += turn * stack[left]
            left += 1
        else:
            diff += turn * stack[right]
            right -= 1
        turn = -turn

    return (total_sum + diff) // 2


if __name__ == "__main__":
    print(solve())
