def solve(grid: list[list[int]]) -> list[list[int]]:
    rows = len(grid)
    columns = len(grid[0])
    answer = [[0] * columns for _ in range(rows)]

    for row in range(rows):
        seen = set()
        r, c = row, 0
        while r < rows and c < columns:
            answer[r][c] = len(seen)
            seen.add(grid[r][c])
            r += 1
            c += 1

    for column in range(1, columns):
        seen = set()
        r, c = 0, column
        while r < rows and c < columns:
            answer[r][c] = len(seen)
            seen.add(grid[r][c])
            r += 1
            c += 1

    for row in range(rows - 1, -1, -1):
        seen = set()
        r, c = row, columns - 1
        while r >= 0 and c >= 0:
            answer[r][c] = abs(answer[r][c] - len(seen))
            seen.add(grid[r][c])
            r -= 1
            c -= 1

    for column in range(columns - 2, -1, -1):
        seen = set()
        r, c = rows - 1, column
        while r >= 0 and c >= 0:
            answer[r][c] = abs(answer[r][c] - len(seen))
            seen.add(grid[r][c])
            r -= 1
            c -= 1

    return answer
