import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    m = int(data[1])
    idx = 2
    grid = [bytearray(data[idx + i]) for i in range(n)]
    idx += n
    q = int(data[idx])
    idx += 1
    diff = [[0] * (m + 2) for _ in range(n + 2)]
    for _ in range(q):
        x1 = int(data[idx]) - 1
        y1 = int(data[idx + 1]) - 1
        x2 = int(data[idx + 2]) - 1
        y2 = int(data[idx + 3]) - 1
        idx += 4
        diff[x1][y1] ^= 1
        diff[x2 + 1][y1] ^= 1
        diff[x1][y2 + 1] ^= 1
        diff[x2 + 1][y2 + 1] ^= 1
    out = []
    for i in range(n):
        row = grid[i]
        for j in range(m):
            if i:
                diff[i][j] ^= diff[i - 1][j]
            if j:
                diff[i][j] ^= diff[i][j - 1]
            if i and j:
                diff[i][j] ^= diff[i - 1][j - 1]
            if diff[i][j]:
                row[j] = 49 if row[j] == 48 else 48
        out.append(row.decode())
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
