import sys

def valid(a: list[int], b: list[int], x: int) -> bool:
    if x <= 0:
        return False
    i = j = skipped = 0
    n = len(a)
    while i < n and j < n - 1:
        value = a[i] + x
        if value == b[j]:
            i += 1
            j += 1
        else:
            skipped += 1
            if skipped > 1:
                return False
            i += 1
    return True

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        a = sorted(data[idx:idx + n])
        idx += n
        b = sorted(data[idx:idx + n - 1])
        idx += n - 1
        candidates = {b[0] - a[0], b[0] - a[1]}
        out.append(str(min((x for x in candidates if valid(a, b, x)))))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
