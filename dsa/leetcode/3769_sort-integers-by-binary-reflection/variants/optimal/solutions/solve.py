from typing import List


def solve(nums: List[int]) -> List[int]:

    def reflection(value: int) -> int:
        reflected = 0
        while value:
            reflected = reflected << 1 | value & 1
            value >>= 1
        return reflected

    return sorted(nums, key=lambda value: (reflection(value), value))
