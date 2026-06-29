import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, admins = data[idx], data[idx + 1]
        idx += 2
        capacities = data[idx:idx + n]
        idx += n
        answer = max(n, max((admins + capacity - 1) // capacity for capacity in capacities))
        out.append(str(answer))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
