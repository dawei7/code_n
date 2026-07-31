from functools import lru_cache


def solve(nums: list[int], numSlots: int) -> int:
    powers = [3**slot for slot in range(numSlots)]

    @lru_cache(None)
    def best(index: int, mask: int) -> int:
        if index == len(nums):
            return 0
        return max((nums[index] & slot) + best(index + 1, mask + power) for slot, power in enumerate(powers, start=1) if (mask // power) % 3 < 2)

    return best(0, 0)
