def solve(position, m):
    points = sorted(set(position))
    if m <= 1 or len(points) <= 1:
        return 0
    if m > len(points):
        m = len(points)

    def can_place(distance):
        count = 1
        last = points[0]
        for point in points[1:]:
            if point - last >= distance:
                count += 1
                last = point
                if count >= m:
                    return True
        return False

    low = 0
    high = points[-1] - points[0]
    while low < high:
        mid = (low + high + 1) // 2
        if can_place(mid):
            low = mid
        else:
            high = mid - 1
    return low
