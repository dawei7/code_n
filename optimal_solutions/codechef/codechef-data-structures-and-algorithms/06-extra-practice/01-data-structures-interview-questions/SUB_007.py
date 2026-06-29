def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    res = []
    pos = 1
    for _ in range(t):
        s = data[pos]
        pos += 1
        count0 = 0
        count00 = 0
        count007 = 0
        for ch in s:
            if ch == '0':
                count00 += count0
                count0 += 1
            elif ch == '7':
                count007 += count00
        res.append(str(count007))
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
