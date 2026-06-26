"""Optimal solution for stack_06: Trapping Rain Water.

Given a non-negative integer array heights where each
"""


def solve(heights, n):
    """Trapping Rain Water via monotonic stack."""
    if n <= 2:
        return 0
    stack = []  # indices with increasing heights
    water = 0
    for i in range(n):
        while stack and heights[i] > heights[stack[-1]]:
            top = stack.pop()
            if not stack:
                break
            # Distance between current and new top of stack.
            dist = i - stack[-1] - 1
            # Bounded by min of the two walls minus the popped bottom.
            bounded = min(heights[i], heights[stack[-1]]) - heights[top]
            water += dist * bounded
        stack.append(i)
    return water
