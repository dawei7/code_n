from typing import List


def solve(nums: List[int], queries: List[int], x: int) -> List[int]:
    positions = [index for index, value in enumerate(nums) if value == x]

    return [positions[occurrence - 1] if occurrence <= len(positions) else -1 for occurrence in queries]
