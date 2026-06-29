import sys


def build(n):
    perm = [0] * n
    used = [False] * (n + 1)
    current = 1
    perm[n - 1] = current
    used[current] = True
    for step in range(n - 1, 0, -1):
        plus = current + step
        if plus <= n and not used[plus]:
            current = plus
        else:
            current -= step
        perm[step - 1] = current
        used[current] = True
    return perm


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        out.append(" ".join(map(str, build(n))))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
