def solve(colors: list[int], queries: list[list[int]]) -> list[int]:
    n = len(colors)
    nearest = [[n, n, n] for _ in range(n)]

    last = [-n, -n, -n]
    for i, color in enumerate(colors):
        last[color - 1] = i
        for target in range(3):
            nearest[i][target] = i - last[target]

    following = [2 * n, 2 * n, 2 * n]
    for i in range(n - 1, -1, -1):
        following[colors[i] - 1] = i
        for target in range(3):
            nearest[i][target] = min(nearest[i][target], following[target] - i)

    return [nearest[i][color - 1] if nearest[i][color - 1] < n else -1 for i, color in queries]
