"""Optimal solution for LeetCode 1011: Capacity To Ship Packages Within D Days."""


def solve(weights: list[int], days: int) -> int:
    def can_ship(capacity: int) -> bool:
        used_days = 1
        load = 0
        for weight in weights:
            if load + weight > capacity:
                used_days += 1
                load = 0
            load += weight
        return used_days <= days

    low = max(weights)
    high = sum(weights)
    while low < high:
        mid = (low + high) // 2
        if can_ship(mid):
            high = mid
        else:
            low = mid + 1
    return low
