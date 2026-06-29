import sys

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    n = int(tokens[0])
    m = int(tokens[1])
    grid = tokens[2:2 + n]
    next_diag = [0] * (m + 1)
    answer = 0
    for r in range(n - 1, -1, -1):
        row = grid[r]
        current = [0] * (m + 1)
        ones_right = 0
        for c in range(m - 1, -1, -1):
            if row[c] == 49:
                ones_right += 1
                current[c] = min(ones_right, 1 + next_diag[c + 1])
                answer += current[c]
            else:
                ones_right = 0
        next_diag = current
    print(answer)


if __name__ == "__main__":
    solve()
