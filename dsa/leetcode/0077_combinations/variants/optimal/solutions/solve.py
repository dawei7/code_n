def solve(n: int, k: int) -> list[list[int]]:
    result: list[list[int]] = []
    path: list[int] = []

    def choose(start: int) -> None:
        if len(path) == k:
            result.append(path[:])
            return
        remaining = k - len(path)
        last_start = n - remaining + 1
        for value in range(start, last_start + 1):
            path.append(value)
            choose(value + 1)
            path.pop()

    choose(1)
    return result
