def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    out = []
    pos = 1
    for _ in range(t):
        A = int(data[pos])
        B = int(data[pos + 1])
        C = int(data[pos + 2])
        pos += 3
        if A == B + C or B == A + C or C == A + B:
            out.append('YES')
        else:
            out.append('NO')
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
