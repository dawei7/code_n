import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, x = data[idx], data[idx + 1]
        idx += 2
        values = data[idx:idx + n]
        idx += n
        even_count = sum(1 for value in values if value % 2 == 0)
        if even_count == 0:
            out.append("0")
        elif x % 2 == 1:
            out.append(str((even_count + 1) // 2))
        elif even_count == n:
            out.append("-1")
        else:
            out.append(str(even_count))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
