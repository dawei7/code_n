def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    results = []
    for _ in range(t):
        n = int(data[idx])
        idx += 1
        arr = list(map(int, data[idx:idx + n]))
        idx += n
        partitions = 0
        curr_max = 0
        for i in range(n):
            if arr[i] > curr_max:
                curr_max = arr[i]
            if curr_max == i + 1:
                partitions += 1
        results.append(str(partitions))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
