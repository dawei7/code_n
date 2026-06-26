"""Optimal solution for sort_10: Shell Sort.

Auto-generated from challenges/algorithms/sorting.py:SPECS.
O(n²) time.
"""


def solve(data, n):
    gap = 1
    while gap < n // 3:
        gap = 3 * gap + 1
    while gap >= 1:
        for i in range(gap, n):
            temp = data[i]
            j = i
            while j >= gap and data[j - gap] > temp:
                data[j] = data[j - gap]
                j -= gap
            data[j] = temp
        gap //= 3
    return data
