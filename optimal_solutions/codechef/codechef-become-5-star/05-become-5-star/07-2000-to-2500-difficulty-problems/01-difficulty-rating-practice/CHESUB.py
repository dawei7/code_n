import sys
NEG = -10 ** 30

def solve() -> None:
    data = list(map(int, sys.stdin.buffer.read().split()))
    t = data[0]
    idx = 1
    out = []
    for _ in range(t):
        n, k = data[idx:idx + 2]
        idx += 2
        arr = data[idx:idx + n]
        idx += n
        done = [NEG] * (k + 1)
        open_sub = [NEG] * (k + 1)
        done[0] = 0
        for value in arr:
            for j in range(k, 0, -1):
                weighted = j * value
                open_sub[j] = max(open_sub[j] + weighted, done[j - 1] + weighted)
                done[j] = max(done[j], open_sub[j])
        out.append(str(done[k]))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
