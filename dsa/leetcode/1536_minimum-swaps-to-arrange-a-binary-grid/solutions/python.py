def solve(grid):
    n = len(grid)
    trailing = []
    for row in grid:
        zeros = 0
        for value in reversed(row[:n]):
            if value == 0:
                zeros += 1
            else:
                break
        trailing.append(zeros)

    swaps = 0
    for i in range(n):
        need = n - i - 1
        j = i
        while j < n and trailing[j] < need:
            j += 1
        if j == n:
            return -1
        while j > i:
            trailing[j], trailing[j - 1] = trailing[j - 1], trailing[j]
            swaps += 1
            j -= 1
    return swaps
