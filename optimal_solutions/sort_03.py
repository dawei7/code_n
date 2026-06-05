"""Optimal solution for sort_03: Insertion Sort.

For each element, shift larger elements right to make room, then
drop the element into the gap. O(n^2) worst case, O(n) on nearly
sorted data.
"""


def solve(data, n):
    for i in range(1, n):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data
