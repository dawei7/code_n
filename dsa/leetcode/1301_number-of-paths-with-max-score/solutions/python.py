def solve(board):
    mod = 1_000_000_007
    n = len(board)
    score = [[-1] * n for _ in range(n)]
    ways = [[0] * n for _ in range(n)]
    score[n - 1][n - 1] = 0
    ways[n - 1][n - 1] = 1

    for r in range(n - 1, -1, -1):
        for c in range(n - 1, -1, -1):
            if board[r][c] == "X" or (r == n - 1 and c == n - 1):
                continue
            best = -1
            count = 0
            for nr, nc in ((r + 1, c), (r, c + 1), (r + 1, c + 1)):
                if nr < n and nc < n and score[nr][nc] >= 0:
                    if score[nr][nc] > best:
                        best = score[nr][nc]
                        count = ways[nr][nc]
                    elif score[nr][nc] == best:
                        count = (count + ways[nr][nc]) % mod
            if best >= 0:
                value = 0 if board[r][c] == "E" else int(board[r][c])
                score[r][c] = best + value
                ways[r][c] = count

    if ways[0][0] == 0:
        return [0, 0]
    return [score[0][0], ways[0][0] % mod]
