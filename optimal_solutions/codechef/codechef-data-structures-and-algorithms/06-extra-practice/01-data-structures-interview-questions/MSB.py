def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    t = int(data[0])
    pos = 1
    res = []
    for _ in range(t):
        A = int(data[pos])
        B = int(data[pos + 1])
        X = int(data[pos + 2])
        Y = int(data[pos + 3])
        pos += 4
        if A >= B:
            res.append('0')
            continue
        if X == 1 and Y == 1:
            res.append('-1')
            continue
        best = None
        if X == 1:
            d = 0
            b_val = B
            while b_val > A:
                b_val //= Y
                d += 1
                if b_val == 0:
                    break
            if A >= b_val:
                best = d
            else:
                best = -1
            res.append(str(best))
            continue
        if Y == 1:
            m = 0
            a_val = A
            while a_val < B:
                a_val *= X
                m += 1
                if m > 10 ** 6:
                    break
            best = m
            res.append(str(best))
            continue
        d = 0
        b_curr = B
        while True:
            m = 0
            a_val = A
            while a_val < b_curr:
                a_val *= X
                m += 1
                if m > 200:
                    break
            current_ops = m + d
            if best is None or current_ops < best:
                best = current_ops
            if b_curr == 0:
                break
            new_b = b_curr // Y
            if new_b == b_curr:
                break
            b_curr = new_b
            d += 1
        res.append(str(best) if best is not None else '-1')
    sys.stdout.write('\n'.join(res))


if __name__ == "__main__":
    solve()
