import sys


def main() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    n, k, p = data[0], data[1], data[2]
    positions = data[3:3 + n]
    idx = 3 + n
    order = sorted((x, i) for i, x in enumerate(positions))
    group = [0] * n
    current = 0
    group[order[0][1]] = current
    for i in range(1, n):
        if order[i][0] - order[i - 1][0] > k:
            current += 1
        group[order[i][1]] = current
    out = []
    for _ in range(p):
        a, b = data[idx] - 1, data[idx + 1] - 1
        idx += 2
        out.append("Yes" if group[a] == group[b] else "No")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
