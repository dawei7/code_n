def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    res = []
    idx = 1
    for _ in range(t):
        s = data[idx]
        idx += 1
        lo, hi = (0, 0)
        valid = True
        for ch in s:
            if ch == '(':
                lo += 1
                hi += 1
            elif ch == ')':
                lo -= 1
                hi -= 1
            else:
                lo -= 1
                hi += 1
            if hi < 0:
                valid = False
                break
            if lo < 0:
                lo = 0
        res.append('1' if valid and lo == 0 else '0')
    sys.stdout.write(''.join(res))


if __name__ == "__main__":
    solve()
