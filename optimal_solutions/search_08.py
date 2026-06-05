"""Optimal solution for search_08: Interpolation Search.

Auto-generated from challenges/algorithms/searching.py:SPECS.
O(n) time.
"""


def solve(data, target, n):
    low, high = 0, n - 1
    while low <= high and data[low] <= target <= data[high]:
        if data[high] == data[low]:
            if data[low] == target:
                return low
            return -1
        # Probe position estimated from the target's value.
        pos = low + (target - data[low]) * (high - low) // (data[high] - data[low])
        if pos < low or pos > high:
            return -1
        value = data[pos]
        if value == target:
            return pos
        if value < target:
            low = pos + 1
        else:
            high = pos - 1
    return -1
