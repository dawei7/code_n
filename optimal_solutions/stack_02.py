"""Optimal solution for stack_02: Next Greater Element.

Monotonic stack: walk left to right, maintaining a stack of
indices whose next-greater hasn't been found yet. When arr[i]
is greater than the top, pop and record i as the answer for
the popped index. O(n).
"""


def solve(arr, n):
    result = [-1] * n
    stack = []  # indices
    for i in range(n):
        while stack and arr[i] > arr[stack[-1]]:
            idx = stack.pop()
            result[idx] = arr[i]
        stack.append(i)
    return result
