"""Optimal solution for search_11: Count Occurrences (Sorted).

Sorted array; count how many times ``target`` appears. Two
binary searches: one for the first occurrence (lower_bound),
one for the last (upper_bound). Difference = count.
O(log n) time.
"""


def solve(data, target, n):
    if n == 0:
        return 0

    def lower_bound(lo, hi, t):
        while lo < hi:
            mid = (lo + hi) // 2
            if data[mid] < t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    def upper_bound(lo, hi, t):
        while lo < hi:
            mid = (lo + hi) // 2
            if data[mid] <= t:
                lo = mid + 1
            else:
                hi = mid
        return lo

    first = lower_bound(0, n, target)
    if first == n or data[first] != target:
        return 0
    last = upper_bound(first, n, target)
    return last - first
