"""App-local reference solution for LeetCode 2835."""


def solve(nums: list[int], target: int) -> int:
    """Return the minimum number of power-of-two split operations."""
    if sum(nums) < target:
        return -1

    counts = [0] * 32
    for value in nums:
        counts[value.bit_length() - 1] += 1

    operations = 0

    for bit in range(31):
        if (target >> bit) & 1:
            if counts[bit] == 0:
                higher = bit + 1
                while counts[higher] == 0:
                    higher += 1

                while higher > bit:
                    counts[higher] -= 1
                    counts[higher - 1] += 2
                    operations += 1
                    higher -= 1

            counts[bit] -= 1

        counts[bit + 1] += counts[bit] // 2

    return operations
