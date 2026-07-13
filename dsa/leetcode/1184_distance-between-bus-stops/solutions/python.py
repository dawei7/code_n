def solve(distance, start, destination):
    if start > destination:
        start, destination = destination, start
    clockwise = sum(distance[start:destination])
    total = sum(distance)
    return min(clockwise, total - clockwise)
