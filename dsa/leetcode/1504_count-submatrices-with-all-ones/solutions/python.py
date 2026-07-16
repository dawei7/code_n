"""Optimal app-local solution for LeetCode 1504."""


def solve(mat: list[list[int]]) -> int:
    """Count contiguous rectangular submatrices containing only ones."""
    columns = len(mat[0])
    heights = [0] * columns
    answer = 0

    for row in mat:
        stack: list[tuple[int, int]] = []
        ending_here = 0

        for column, value in enumerate(row):
            heights[column] = heights[column] + 1 if value else 0
            width = 1

            while stack and stack[-1][0] >= heights[column]:
                height, previous_width = stack.pop()
                ending_here -= height * previous_width
                width += previous_width

            stack.append((heights[column], width))
            ending_here += heights[column] * width
            answer += ending_here

    return answer
