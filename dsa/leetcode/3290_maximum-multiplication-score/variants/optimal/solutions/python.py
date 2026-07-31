def solve(a: list[int], b: list[int]) -> int:
    negative_infinity = float("-inf")
    best = [0, negative_infinity, negative_infinity, negative_infinity, negative_infinity]

    for value in b:
        for chosen in range(3, -1, -1):
            best[chosen + 1] = max(
                best[chosen + 1],
                best[chosen] + a[chosen] * value,
            )

    return int(best[4])
