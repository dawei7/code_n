import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        _, _, k = data[idx], data[idx + 1], data[idx + 2]
        idx += 3
        cells = set()
        perimeter = 0
        for _ in range(k):
            row, col = data[idx], data[idx + 1]
            idx += 2
            perimeter += 4
            for neighbor in ((row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)):
                if neighbor in cells:
                    perimeter -= 2
            cells.add((row, col))
        out.append(str(perimeter))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
