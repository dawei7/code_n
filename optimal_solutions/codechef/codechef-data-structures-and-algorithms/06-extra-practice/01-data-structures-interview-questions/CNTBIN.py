def solve():
    import sys
    data = sys.stdin.read().split()
    mod = 10 ** 9 + 7
    t = int(data[0])
    idx = 1
    res = []
    for _ in range(t):
        n = int(data[idx])
        s = data[idx + 1]
        idx += 2
        zero_count = 0
        ans = 0
        for ch in s:
            if ch == '0':
                zero_count += 1
            elif ch == '1':
                ans = (ans + zero_count) % mod
        res.append(str(ans))
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
