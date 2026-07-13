def solve(mat):
    if not mat:
        return 0
    grid = []
    width = 0
    for row in mat:
        values = list(row) if isinstance(row, (list, str)) else [row]
        width = max(width, len(values))
        grid.append(values)
    heights = [0] * width
    answer = 0
    for row in grid:
        row = row + [0] * (width - len(row))
        stack = []
        row_sum = 0
        for col, value in enumerate(row):
            heights[col] = heights[col] + 1 if value in (1, "1", "A", True) else 0
            count = 1
            while stack and stack[-1][0] >= heights[col]:
                height, previous_count = stack.pop()
                row_sum -= height * previous_count
                count += previous_count
            stack.append((heights[col], count))
            row_sum += heights[col] * count
            answer += row_sum
    return answer
