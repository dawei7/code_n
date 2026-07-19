from typing import List

def solve(hours: List[int], target: int) -> int:
    """
    Calculates the number of employees who worked at least the target hours.
    """
    count = 0
    for h in hours:
        if h >= target:
            count += 1
    return count
