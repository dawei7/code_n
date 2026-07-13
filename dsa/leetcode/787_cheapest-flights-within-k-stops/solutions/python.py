def solve(n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
    costs = [float("inf")] * n
    costs[src] = 0

    for _ in range(k + 1):
        next_costs = costs.copy()
        for origin, destination, price in flights:
            if costs[origin] != float("inf"):
                next_costs[destination] = min(
                    next_costs[destination],
                    costs[origin] + price,
                )
        costs = next_costs

    return -1 if costs[dst] == float("inf") else int(costs[dst])
