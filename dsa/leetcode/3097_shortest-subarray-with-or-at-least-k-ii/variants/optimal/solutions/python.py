def solve(nums: list[int], k: int) -> int:
    if k == 0:
        return 1

    counts = [0] * 30
    current = 0
    left = 0
    answer = len(nums) + 1

    for right, number in enumerate(nums):
        current |= number
        for bit in range(30):
            if number & (1 << bit):
                counts[bit] += 1

        while current >= k:
            answer = min(answer, right - left + 1)
            removed = nums[left]
            left += 1

            for bit in range(30):
                mask = 1 << bit
                if removed & mask:
                    counts[bit] -= 1
                    if counts[bit] == 0:
                        current &= ~mask

    return -1 if answer > len(nums) else answer
