def solve(k: int, n: int) -> list[list[int]]:
    results, path = [], []

    def search(next_value: int, remaining: int) -> None:
        if len(path) == k:
            if remaining == 0:
                results.append(path.copy())
            return
        for value in range(next_value, 10):
            if value > remaining:
                break
            path.append(value)
            search(value + 1, remaining - value)
            path.pop()

    search(1, n)
    return results
