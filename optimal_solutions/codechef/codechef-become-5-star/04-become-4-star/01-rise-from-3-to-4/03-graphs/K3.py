import sys
from collections import deque

def shortest_digit_walk(grid: list[str], target: int) -> int:
    rows = len(grid)
    cols = len(grid[0])
    start = (-1, -1)
    for r, row in enumerate(grid):
        c = row.find('*')
        if c != -1:
            start = (r, c)
            break
    seen = [[[False] * (target + 1) for _ in range(cols)] for __ in range(rows)]
    queue = deque([(start[0], start[1], 0, 0)])
    directions = ((1, 0), (-1, 0), (0, 1), (0, -1))
    while queue:
        r, c, digit_sum, steps = queue.popleft()
        if r < 0 or r >= rows or c < 0 or (c >= cols):
            continue
        if grid[r][c] == '#' or seen[r][c][digit_sum]:
            continue
        seen[r][c][digit_sum] = True
        cell = grid[r][c]
        if '0' <= cell <= '9':
            digit_sum += ord(cell) - 48
            if digit_sum > target:
                continue
        if digit_sum == target:
            return steps
        for dr, dc in directions:
            queue.append((r + dr, c + dc, digit_sum, steps + 1))
    return -1

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        m = int(tokens[idx])
        n = int(tokens[idx + 1])
        idx += 2
        grid = [tokens[idx + row].decode() for row in range(m + 1)]
        idx += m + 1
        target = int(tokens[idx])
        idx += 1
        out.append(str(shortest_digit_walk(grid, target)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
