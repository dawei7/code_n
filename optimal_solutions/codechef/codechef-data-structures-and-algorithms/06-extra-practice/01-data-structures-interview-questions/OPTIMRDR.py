def solve():
    import sys
    data = sys.stdin.read().split()
    if not data:
        return
    n = int(data[0])
    pos = list(map(int, data[1:1 + n]))
    safe_pos = list(map(int, data[1 + n:1 + 2 * n]))
    soldiers = sorted([(pos[i], i) for i in range(n)])
    safe_sorted = sorted(safe_pos)
    res = [0] * n
    for i in range(n):
        _, orig_index = soldiers[i]
        res[orig_index] = safe_sorted[i]
    sys.stdout.write(' '.join(map(str, res)))


if __name__ == "__main__":
    solve()
