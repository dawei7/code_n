def solve(n, cuts):
    points = [0] + sorted(cuts) + [n]
    count = len(points)
    cost = [[0] * count for _ in range(count)]

    for width in range(2, count):
        for left in range(count - width):
            right = left + width
            cost[left][right] = min(
                cost[left][middle]
                + cost[middle][right]
                + points[right]
                - points[left]
                for middle in range(left + 1, right)
            )

    return cost[0][-1]
