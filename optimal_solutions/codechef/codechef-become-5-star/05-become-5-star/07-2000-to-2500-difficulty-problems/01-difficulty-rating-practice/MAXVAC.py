import sys

def solve() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    idx = 1
    out = []
    for _ in range(t):
        n = int(data[idx])
        x = int(data[idx + 1])
        s = data[idx + 2].decode()
        idx += 3
        blocks = []
        cur = 0
        for ch in s:
            if ch == '0':
                cur += 1
            else:
                blocks.append(cur)
                cur = 0
        blocks.append(cur)
        base = sum((length // x for length in blocks))
        best = base
        for i in range(1, len(blocks)):
            merged = blocks[i - 1] + 1 + blocks[i]
            cand = base - blocks[i - 1] // x - blocks[i] // x + merged // x
            best = max(best, cand)
        if '1' not in s:
            best = max(best, n // x)
        out.append(str(best))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
