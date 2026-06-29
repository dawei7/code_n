def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    results = []
    index = 1
    for _ in range(t):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        total_rectangles = n * (n + 1) // 2 * (m * (m + 1) // 2)
        invalid_rectangles = n * m
        results.append(str(total_rectangles - invalid_rectangles))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
