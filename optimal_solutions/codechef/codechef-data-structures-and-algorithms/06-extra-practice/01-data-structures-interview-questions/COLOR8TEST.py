def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    index = 1
    result = []
    for _ in range(t):
        n = int(data[index])
        index += 1
        costs = list(map(int, data[index:index + 6]))
        index += 6
        liters_needed = (n + 1) // 2
        total_cost = liters_needed * sum(costs)
        result.append(str(total_cost))
    sys.stdout.write('\n'.join(result))


if __name__ == "__main__":
    solve()
