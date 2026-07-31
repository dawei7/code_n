def solve(n: int, roads: list[list[int]]) -> int:
    degrees = [0] * n
    for first, second in roads:
        degrees[first] += 1
        degrees[second] += 1

    degrees.sort()
    return sum(value * degree for value, degree in enumerate(degrees, start=1))
