def solve(grid):
    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    r = rows - 1
    c = 0
    answer = 0
    while r >= 0 and c < cols:
        if grid[r][c] < 0:
            answer += cols - c
            r -= 1
        else:
            c += 1
    return answer
