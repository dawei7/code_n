from typing import List


def solve(nums: List[int], k: int) -> int:
    modulus = 1_000_000_007
    bit_counts = [0] * 30

    for value in nums:
        for bit in range(30):
            bit_counts[bit] += (value >> bit) & 1

    answer = 0
    for _ in range(k):
        value = 0
        for bit in range(30):
            if bit_counts[bit]:
                value |= 1 << bit
                bit_counts[bit] -= 1
        answer = (answer + value * value) % modulus

    return answer
