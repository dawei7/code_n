"""Optimal solution for stack_03: Stock Span Problem.

For each day i, the span is the number of consecutive days
just before i with a price <= arr[i] (plus today). Monotonic
stack: walk left to right, popping while the top's price is
<= today's. The span is i - (top index after popping), or
i + 1 if the stack is empty. O(n).
"""


def solve(arr, n):
    spans = [0] * n
    stack = []  # indices
    for i in range(n):
        while stack and arr[stack[-1]] <= arr[i]:
            stack.pop()
        if stack:
            spans[i] = i - stack[-1]
        else:
            spans[i] = i + 1
        stack.append(i)
    return spans
