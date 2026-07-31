def solve(
    maxTime: int,
    edges: list[list[int]],
    passingFees: list[int],
) -> int:
    city_count = len(passingFees)
    infinity = 10**18
    costs = [[infinity] * city_count for _ in range(maxTime + 1)]
    costs[0][0] = passingFees[0]

    for elapsed in range(1, maxTime + 1):
        current = costs[elapsed]
        for first, second, travel_time in edges:
            if travel_time > elapsed:
                continue
            previous = costs[elapsed - travel_time]
            if previous[first] != infinity:
                current[second] = min(
                    current[second],
                    previous[first] + passingFees[second],
                )
            if previous[second] != infinity:
                current[first] = min(
                    current[first],
                    previous[second] + passingFees[first],
                )

    answer = min(costs[elapsed][-1] for elapsed in range(maxTime + 1))
    return -1 if answer == infinity else answer
