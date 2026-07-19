"""App-local reference solution for LeetCode 1829."""


def solve(nums: list[int], maximumBit: int) -> list[int]:
    current_xor = 0
    for value in nums:
        current_xor ^= value

    mask = (1 << maximumBit) - 1
    answer = []
    for value in reversed(nums):
        answer.append(current_xor ^ mask)
        current_xor ^= value
    return answer
