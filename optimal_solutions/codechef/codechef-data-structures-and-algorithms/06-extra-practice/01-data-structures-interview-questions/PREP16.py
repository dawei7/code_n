def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        arr = list(map(int, data[index:index + n]))
        index += n
        total = 0
        for b in range(32):
            ones = 0
            for num in arr:
                if num & 1 << b:
                    ones += 1
            zeros = n - ones
            total += ones * zeros
        results.append(str(total))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
