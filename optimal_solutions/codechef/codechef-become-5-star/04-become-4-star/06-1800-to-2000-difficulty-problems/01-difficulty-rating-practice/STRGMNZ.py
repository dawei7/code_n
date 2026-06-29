import sys

def smallest_factor(n: int) -> int:
    if n % 2 == 0:
        return 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return d
        d += 2
    return n

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    out = []
    for n in data[1:1 + t]:
        factor = smallest_factor(n)
        if factor == n:
            out.append(str(n + 1))
        else:
            out.append(str(n + n // factor))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
