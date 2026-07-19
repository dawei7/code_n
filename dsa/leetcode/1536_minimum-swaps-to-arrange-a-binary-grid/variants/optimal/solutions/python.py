def solve(grid):
    n = len(grid)
    trailing_zeros = []
    for row in grid:
        zeros = 0
        for value in reversed(row):
            if value == 1:
                break
            zeros += 1
        trailing_zeros.append(zeros)

    swaps = 0
    for position in range(n):
        required = n - position - 1
        candidate = position
        while candidate < n and trailing_zeros[candidate] < required:
            candidate += 1
        if candidate == n:
            return -1
        swaps += candidate - position
        chosen = trailing_zeros.pop(candidate)
        trailing_zeros.insert(position, chosen)
    return swaps
