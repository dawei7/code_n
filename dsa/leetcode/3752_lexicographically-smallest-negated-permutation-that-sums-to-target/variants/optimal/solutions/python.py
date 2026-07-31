def solve(n: int, target: int) -> list[int]:
    magnitude_sum = n * (n + 1) // 2
    difference = magnitude_sum - target
    if abs(target) > magnitude_sum or difference % 2:
        return []

    remaining = difference // 2
    negative_values: set[int] = set()
    for magnitude in range(n, 0, -1):
        if magnitude <= remaining:
            negative_values.add(magnitude)
            remaining -= magnitude

    result = [
        -magnitude
        for magnitude in range(n, 0, -1)
        if magnitude in negative_values
    ]
    result.extend(
        magnitude
        for magnitude in range(1, n + 1)
        if magnitude not in negative_values
    )
    return result
