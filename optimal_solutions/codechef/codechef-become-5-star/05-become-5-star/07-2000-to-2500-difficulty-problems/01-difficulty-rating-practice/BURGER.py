import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        x, y = data[idx:idx + 2]
        idx += 2
        if y % x:
            out.append('-1')
            continue
        target = y // x
        best = None
        for streaks in range(1, 64):
            value = target + streaks
            if value.bit_count() != streaks:
                continue
            if value & 1:
                continue
            minutes = streaks - 1
            length = 0
            while value:
                if value & 1:
                    minutes += length
                if value & 1:
                    pass
                value >>= 1
                length += 1
            if best is None or minutes < best:
                best = minutes
        out.append(str(best if best is not None else -1))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
