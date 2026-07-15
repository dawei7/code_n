def solve(colors: list[int], queries: list[list[int]]) -> list[int]:
    n = len(colors)
    nearest = [[n, n, n] for _ in range(n)]

    last = [-n, -n, -n]
    for index, color in enumerate(colors):
        last[color - 1] = index
        for target in range(3):
            nearest[index][target] = index - last[target]

    following = [2 * n, 2 * n, 2 * n]
    for index in range(n - 1, -1, -1):
        following[colors[index] - 1] = index
        for target in range(3):
            nearest[index][target] = min(
                nearest[index][target], following[target] - index
            )

    return [
        nearest[index][color - 1] if nearest[index][color - 1] < n else -1
        for index, color in queries
    ]
