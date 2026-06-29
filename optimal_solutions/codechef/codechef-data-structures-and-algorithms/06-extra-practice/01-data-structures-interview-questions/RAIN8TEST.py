def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    results = []
    for _ in range(t):
        n = int(data[index])
        x = int(data[index + 1])
        index += 2
        days = list(map(int, data[index:index + n]))
        index += n
        cost = 0
        if days:
            if days[0] == 1:
                cost += x
        for i in range(1, n):
            if days[i] == 1 or days[i - 1] == 1:
                cost += x
        results.append(str(cost))
    sys.stdout.write('\n'.join(results))


if __name__ == "__main__":
    solve()
