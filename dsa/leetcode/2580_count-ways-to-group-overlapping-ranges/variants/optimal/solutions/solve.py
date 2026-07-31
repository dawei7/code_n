def solve(ranges: list[list[int]]) -> int:
    modulus = 1_000_000_007
    ranges.sort()
    ways = 1
    current_end = -1

    for start, end in ranges:
        if start > current_end:
            ways = ways * 2 % modulus
        current_end = max(current_end, end)

    return ways
