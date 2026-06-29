def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    results = []

    def is_unique(n):
        s = str(n)
        return len(s) == len(set(s))
    index = 1
    for _ in range(t):
        x = int(data[index])
        index += 1
        y = x + 1
        while not is_unique(y):
            y += 1
        results.append(str(y))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
