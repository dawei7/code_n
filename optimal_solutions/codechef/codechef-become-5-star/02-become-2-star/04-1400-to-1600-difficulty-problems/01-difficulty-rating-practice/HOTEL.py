import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arrivals = data[idx:idx + n]
        idx += n
        departures = data[idx:idx + n]
        idx += n
        events = [(time, 1) for time in arrivals] + [(time, -1) for time in departures]
        events.sort()
        current = best = 0
        for _, delta in events:
            current += delta
            best = max(best, current)
        out.append(str(best))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
