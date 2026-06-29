def solve():
    import sys
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    petrol = list(map(int, data[1:n + 1]))
    cost = list(map(int, data[n + 1:2 * n + 1]))
    total_tank = 0
    curr_tank = 0
    start = 0
    for i in range(n):
        diff = petrol[i] - cost[i]
        total_tank += diff
        curr_tank += diff
        if curr_tank < 0:
            start = i + 1
            curr_tank = 0
    if total_tank >= 0:
        print(start)
    else:
        print(-1)


if __name__ == "__main__":
    solve()
