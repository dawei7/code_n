"""Optimal solution for dc_19: Maximum Subarray Sum (Divide and Conquer).

Given an array of n integers (with at least one
"""


def solve(arr, n):
    """Maximum subarray sum via divide and conquer."""

    def rec(lo, hi):
        if lo == hi:
            return arr[lo]
        mid = (lo + hi) // 2
        # Best fully in the left half.
        left_best = rec(lo, mid)
        # Best fully in the right half.
        right_best = rec(mid + 1, hi)
        # Best crossing the middle: extend leftward from mid,
        # then rightward from mid+1, and combine.
        s = 0
        left_sum = arr[mid]
        for i in range(mid, lo - 1, -1):
            s += arr[i]
            if s > left_sum:
                left_sum = s
        s = 0
        right_sum = arr[mid + 1]
        for i in range(mid + 1, hi + 1):
            s += arr[i]
            if s > right_sum:
                right_sum = s
        cross = left_sum + right_sum
        return max(left_best, right_best, cross)

    return rec(0, n - 1)
