def solve(matrix: list[list[str]]) -> int:
    heights = [0] * len(matrix[0])
    best = 0
    for row in matrix:
        for column, value in enumerate(row):
            heights[column] = heights[column] + 1 if value == "1" else 0

        stack: list[tuple[int, int]] = []
        for i, height in enumerate(heights + [0]):
            start = i
            while stack and stack[-1][1] > height:
                start, previous_height = stack.pop()
                best = max(best, previous_height * (i - start))
            stack.append((start, height))
    return best
