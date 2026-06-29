import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, maximum, average = data[idx:idx + 3]
        idx += 3
        if average == maximum:
            out.append("0")
        else:
            out.append(str((n * average) // (average + 1)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
