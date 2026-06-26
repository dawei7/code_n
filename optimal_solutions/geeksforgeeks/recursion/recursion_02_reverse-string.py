"""Optimal solution for recursion_02: Reverse String.

Two-pointer swap; swap s[left] and s[right] in place, recurse
on the inner substring. Stop when left >= right. O(n) time,
O(n) recursion stack space.
"""


def solve(s, n):
    chars = list(s)

    def helper(left, right):
        if left >= right:
            return
        chars[left], chars[right] = chars[right], chars[left]
        helper(left + 1, right - 1)

    helper(0, n - 1)
    return "".join(chars)
