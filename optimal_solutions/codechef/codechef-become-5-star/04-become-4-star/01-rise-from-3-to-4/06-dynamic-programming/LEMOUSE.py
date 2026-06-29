import sys
NEIGHBORS = ((0, 0), (1, 0), (-1, 0), (0, 1), (0, -1))

def neighborhood_mask(grid: list[bytes], row: int, col: int) -> set[tuple[int, int]]:
    n = len(grid)
    m = len(grid[0])
    cells = set()
    for dr, dc in NEIGHBORS:
        nr, nc = (row + dr, col + dc)
        if 0 <= nr < n and 0 <= nc < m and (grid[nr][nc] == 49):
            cells.add((nr, nc))
    return cells

def minimum_scared(grid: list[bytes]) -> int:
    n = len(grid)
    m = len(grid[0])
    masks = [[neighborhood_mask(grid, r, c) for c in range(m)] for r in range(n)]
    inf = 10 ** 9
    dp = [[[inf, inf] for _ in range(m)] for __ in range(n)]
    if n > 1:
        dp[1][0][0] = len(masks[0][0] | masks[1][0])
    if m > 1:
        dp[0][1][1] = len(masks[0][0] | masks[0][1])
    if n == 1 and m == 1:
        return len(masks[0][0])
    for r in range(n):
        for c in range(m):
            for direction in range(2):
                current = dp[r][c][direction]
                if current >= inf:
                    continue
                previous_cells = masks[r][c]
                if direction == 0 and r > 0:
                    previous_cells = previous_cells | masks[r - 1][c]
                elif direction == 1 and c > 0:
                    previous_cells = previous_cells | masks[r][c - 1]
                if r + 1 < n:
                    add = len(masks[r + 1][c] - previous_cells)
                    if current + add < dp[r + 1][c][0]:
                        dp[r + 1][c][0] = current + add
                if c + 1 < m:
                    add = len(masks[r][c + 1] - previous_cells)
                    if current + add < dp[r][c + 1][1]:
                        dp[r][c + 1][1] = current + add
    return min(dp[-1][-1])

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    t = int(tokens[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = int(tokens[idx])
        m = int(tokens[idx + 1])
        idx += 2
        grid = tokens[idx:idx + n]
        idx += n
        out.append(str(minimum_scared(grid)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
