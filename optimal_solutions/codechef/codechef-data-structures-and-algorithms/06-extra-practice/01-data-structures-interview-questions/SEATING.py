def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    out = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        mn = min(arr)
        mx = max(arr)
        out.append(str(4 * (mx - mn)))
    sys.stdout.write('\n'.join(out))


if __name__ == "__main__":
    solve()
