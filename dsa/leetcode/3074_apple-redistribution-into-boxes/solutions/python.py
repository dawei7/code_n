from typing import List

def solve(apple: List[int], capacity: List[int]) -> int:
    """
    Calculates the minimum number of boxes required to store all apples.
    """
    total_apples = sum(apple)
    # Sort capacities in descending order to pick the largest boxes first
    sorted_capacity = sorted(capacity, reverse=True)

    boxes_used = 0
    current_capacity = 0

    for cap in sorted_capacity:
        if current_capacity >= total_apples:
            break
        current_capacity += cap
        boxes_used += 1

    return boxes_used
