from typing import List

def solve(nums: List[int]) -> List[int]:
    """
    Transforms the array by placing all even numbers before all odd numbers.
    Uses a custom sort key where x % 2 returns 0 for even and 1 for odd,
    ensuring evens (0) come before odds (1).
    """
    return sorted(nums, key=lambda x: x % 2)
