import sys


def divisors(n: int):
    small = []
    large = []
    d = 1
    while d * d <= n:
        if n % d == 0:
            small.append(d)
            if d * d != n:
                large.append(n // d)
        d += 1
    return small + large[::-1]


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        ones = [i for i, ch in enumerate(s) if ch == 49]
        total_ones = len(ones)
        best = min(n - total_ones, total_ones - 1 if total_ones else 1)
        for step in divisors(n):
            selected = n // step
            if abs(total_ones - selected) >= best:
                continue
            ones_by_residue = [0] * step
            for pos in ones:
                ones_by_residue[pos % step] += 1
            keep = max(ones_by_residue)
            best = min(best, total_ones + selected - 2 * keep)
        out.append(str(best))
    sys.stdout.write("\n".join(out))


if __name__ == "__main__":
    main()
