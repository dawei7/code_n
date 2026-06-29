import sys


def kadane(values):
    best = current = values[0]
    for value in values[1:]:
        current = max(value, current + value)
        best = max(best, current)
    return best


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k = data[idx], data[idx + 1]
        idx += 2
        values = data[idx:idx + n]
        idx += n
        if k == 1:
            out.append(str(kadane(values)))
            continue
        total = sum(values)
        best_two = kadane(values * 2)
        out.append(str(best_two + max(0, k - 2) * max(0, total)))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
