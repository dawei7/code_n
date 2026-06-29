import sys

def parse_matrix(tokens: list[str], idx: int, n: int) -> tuple[list[list[int]], int]:
    cells: list[int] = []
    while len(cells) < n * n:
        token = tokens[idx]
        idx += 1
        cells.extend((ord(ch) - 48 for ch in token if ch in '012'))
    matrix = [cells[row * n:(row + 1) * n] for row in range(n)]
    return (matrix, idx)

def still_possible(matrix: list[list[int]]) -> str:
    n = len(matrix)
    wins = [0] * n
    unplayed = [0] * n
    target = 0
    for i, row in enumerate(matrix):
        for value in row:
            if value == 1:
                wins[i] += 1
                if wins[i] > target:
                    target = wins[i]
            elif value == 2:
                unplayed[i] += 1
    for i in range(n):
        if wins[i] + unplayed[i] < target:
            continue
        for j, value in enumerate(matrix[i]):
            if value == 2 and wins[i] == target and (wins[j] == target):
                target += 1
    return ''.join(('1' if wins[i] + unplayed[i] >= target else '0' for i in range(n)))

def solve() -> None:
    tokens = sys.stdin.buffer.read().split()
    if not tokens:
        return
    decoded = [token.decode() for token in tokens]
    t = int(decoded[0])
    idx = 1
    out: list[str] = []
    for _ in range(t):
        n = int(decoded[idx])
        idx += 1
        matrix, idx = parse_matrix(decoded, idx, n)
        out.append(still_possible(matrix))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
