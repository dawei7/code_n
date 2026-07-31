def solve(nums: list[int], k: int) -> int:
    answer = 0

    for bit in range(31):
        mask = 1 << bit
        count = sum(1 for value in nums if value & mask)
        if count >= k:
            answer |= mask

    return answer
