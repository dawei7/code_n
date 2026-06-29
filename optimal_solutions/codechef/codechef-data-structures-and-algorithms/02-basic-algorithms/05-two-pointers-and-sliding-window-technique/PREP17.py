def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        a = set(data[index:index + n])
        index += n
        b = set(data[index:index + n])
        index += n
        common = a.intersection(b)
        results.append(str(len(common)))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
