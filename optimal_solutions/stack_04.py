"""Optimal solution for stack_04: Largest Rectangle in Histogram.

Monotonic stack of bar indices with increasing heights. For each
bar popped, the rectangle extends from the previous-smaller on
the left to the current on the right. Track the max area across
all pops.
"""


def solve(heights, n):
    if n == 0:
        return 0
    stack = []
    best = 0
    for i in range(n + 1):
        cur_h = heights[i] if i < n else 0
        while stack and heights[stack[-1]] > cur_h:
            top = stack.pop()
            h = heights[top]
            left = stack[-1] + 1 if stack else 0
            right = i - 1
            area = h * (right - left + 1)
            if area > best:
                best = area
        stack.append(i)
    return best
