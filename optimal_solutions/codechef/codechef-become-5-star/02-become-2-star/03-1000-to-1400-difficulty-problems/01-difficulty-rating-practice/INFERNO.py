import sys

def solve():
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, x = (data[idx], data[idx + 1])
        idx += 2
        health = data[idx:idx + n]
        idx += n
        single = sum(((h + x - 1) // x for h in health))
        multi = max(health)
        out.append(str(min(single, multi)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
