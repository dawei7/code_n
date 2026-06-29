def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    results = []
    idx = 1
    for _ in range(t):
        H = int(data[idx])
        W = int(data[idx + 1])
        X = int(data[idx + 2])
        Y = int(data[idx + 3])
        K = int(data[idx + 4])
        idx += 5
        dx = W - X
        dy = H - Y
        if dx * dx + dy * dy < K * K:
            results.append('1')
        else:
            results.append('0')
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
