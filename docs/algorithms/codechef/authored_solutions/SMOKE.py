import sys


def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, bus_smoke, car_smoke = data[idx:idx + 3]
        idx += 3
        best = 10 ** 18
        for buses in range((n + 99) // 100 + 1):
            remaining = max(0, n - 100 * buses)
            cars = (remaining + 3) // 4
            best = min(best, buses * bus_smoke + cars * car_smoke)
        out.append(str(best))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    solve()
