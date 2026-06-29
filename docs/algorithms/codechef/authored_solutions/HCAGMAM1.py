import sys


def solve():
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        x = int(data[idx])
        y = int(data[idx + 1])
        s = data[idx + 2]
        idx += 3
        worked = s.count(b"1")
        best = current = 0
        for ch in s:
            if ch == ord("1"):
                current += 1
                best = max(best, current)
            else:
                current = 0
        out.append(str(worked * x + best * y))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
