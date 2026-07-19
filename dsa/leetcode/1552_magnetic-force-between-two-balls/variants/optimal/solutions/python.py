def solve(position, m):
    points = sorted(position)

    def feasible(distance):
        placed = 1
        last = points[0]
        for point in points[1:]:
            if point - last >= distance:
                placed += 1
                last = point
                if placed == m:
                    return True
        return False

    low = 1
    high = (points[-1] - points[0]) // (m - 1)

    while low <= high:
        middle = (low + high) // 2
        if feasible(middle):
            low = middle + 1
        else:
            high = middle - 1

    return high
