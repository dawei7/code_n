def solve(g: list[int], s: list[int]) -> int:
    g.sort()
    s.sort()
    child = 0
    for cookie in s:
        if child < len(g) and cookie >= g[child]:
            child += 1
    return child
