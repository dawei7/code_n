def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    t = int(data[0])
    index = 1
    out_lines = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        arr.sort()
        for i in range(0, n - 1, 2):
            arr[i], arr[i + 1] = (arr[i + 1], arr[i])
        out_lines.append(' '.join(map(str, arr)))
    sys.stdout.write('\n'.join(out_lines))


if __name__ == "__main__":
    solve()
