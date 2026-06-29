import sys

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n = data[idx]
        idx += 1
        arr = data[idx:idx + n]
        idx += n
        seen = {0}
        prefix = 0
        changes = 0
        for value in arr:
            prefix ^= value
            if prefix in seen:
                changes += 1
                seen = {0}
                prefix = 0
            else:
                seen.add(prefix)
        out.append(str(changes))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
