def solve(n: int) -> str:
    groups = [str(seed) for seed in range(1, n + 1)]

    while len(groups) > 1:
        count = len(groups)
        groups = [f"({groups[i]},{groups[count - 1 - i]})" for i in range(count // 2)]

    return groups[0]
