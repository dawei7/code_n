import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, m = data[idx], data[idx + 1]
        idx += 2
        alice = set(data[idx:idx + n])
        idx += n
        berta = set(data[idx:idx + m])
        idx += m
        out.append(str(len(alice & berta)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
