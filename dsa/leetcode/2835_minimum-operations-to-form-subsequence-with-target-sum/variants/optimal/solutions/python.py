from typing import List

def solve(nums: List[int], target: int) -> int:
    if sum(nums) < target:
        return -1

    max_bit = max(max(nums).bit_length(), target.bit_length()) + 1
    counts = [0] * (max_bit + 1)
    for x in nums:
        counts[x.bit_length() - 1] += 1

    ops = 0

    for i in range(max_bit):
        if (target >> i) & 1:
            if counts[i] > 0:
                counts[i] -= 1
            else:
                j = i + 1
                while j < max_bit and counts[j] == 0:
                    j += 1
                if j == max_bit:
                    return -1

                while j > i:
                    counts[j] -= 1
                    counts[j - 1] += 2
                    ops += 1
                    j -= 1
                counts[i] -= 1

        counts[i + 1] += counts[i] // 2

    return ops
