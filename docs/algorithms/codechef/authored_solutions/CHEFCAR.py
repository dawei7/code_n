import sys


def min_cost(n, capacity):
    distance = n - 1
    if distance <= capacity:
        return distance
    last_paid_checkpoint = n - capacity
    return capacity + (last_paid_checkpoint * (last_paid_checkpoint + 1) // 2 - 1)


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, capacity = data[idx], data[idx + 1]
        idx += 2
        maximum = n * (n - 1) // 2
        minimum = min_cost(n, capacity)
        out.append(f"{maximum} {minimum}")
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
