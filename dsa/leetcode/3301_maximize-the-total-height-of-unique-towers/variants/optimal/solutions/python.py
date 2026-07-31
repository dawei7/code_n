def solve(maximumHeight: list[int]) -> int:
    maximumHeight.sort(reverse=True)
    next_height = 10**18
    total = 0

    for limit in maximumHeight:
        height = min(limit, next_height - 1)
        if height <= 0:
            return -1
        total += height
        next_height = height

    return total
