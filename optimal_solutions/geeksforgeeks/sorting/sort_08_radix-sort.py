"""Optimal solution for sort_08: Radix Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n) time.
"""


def solve(data, n):
    if n == 0:
        return data
    max_val = max(data)
    exp = 1
    while max_val // exp > 0:
        # Counting sort on the current digit.
        counts = [0] * 10
        for value in data:
            counts[(value // exp) % 10] += 1
        # Turn counts into a stable-position table.
        for i in range(1, 10):
            counts[i] += counts[i - 1]
        # Walk the input right-to-left so the sort stays stable.
        output = [0] * n
        for i in range(n - 1, -1, -1):
            digit = (data[i] // exp) % 10
            counts[digit] -= 1
            output[counts[digit]] = data[i]
        # Copy the per-digit sorted output back into data.
        for i in range(n):
            data[i] = output[i]
        exp *= 10
    return data
