from typing import List


def solve(heights: List[int]) -> int:
    n = len(heights)
    left = [0] * n
    stack: List[int] = []

    for i, height in enumerate(heights):
        while stack and heights[stack[-1]] > height:
            stack.pop()
        if stack:
            previous = stack[-1]
            left[i] = left[previous] + (i - previous) * height
        else:
            left[i] = (i + 1) * height
        stack.append(i)

    right = [0] * n
    stack.clear()
    answer = 0

    for i in range(n - 1, -1, -1):
        height = heights[i]
        while stack and heights[stack[-1]] > height:
            stack.pop()
        if stack:
            next_index = stack[-1]
            right[i] = right[next_index] + (next_index - i) * height
        else:
            right[i] = (n - i) * height
        answer = max(answer, left[i] + right[i] - height)
        stack.append(i)

    return answer
