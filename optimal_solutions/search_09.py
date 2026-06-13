"""Optimal solution for search_09: Fibonacci Search.

Sorted array; uses Fibonacci numbers to split the range.
Always shrinks by at least one Fibonacci number, so the loop
runs in O(log n) time. The split is by index, not value.
"""


def solve(data, target, n):
    if n == 0:
        return -1
    # Initialise the smallest Fibonacci >= n.
    fib2, fib1 = 0, 1
    fib = fib1 + fib2
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2
    offset = -1
    while fib > 1:
        i = min(offset + fib2, n - 1)
        if data[i] < target:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
        elif data[i] > target:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i
    if fib1 and offset + 1 < n and data[offset + 1] == target:
        return offset + 1
    return -1
