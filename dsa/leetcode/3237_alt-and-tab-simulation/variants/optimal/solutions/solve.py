def solve(windows: list[int], queries: list[int]) -> list[int]:
    seen: set[int] = set()
    result: list[int] = []

    for window in reversed(queries):
        if window not in seen:
            seen.add(window)
            result.append(window)

    result.extend(window for window in windows if window not in seen)
    return result
