def solve(arr1, arr2):
    best = 0
    for s1, s2 in ((1, 1), (1, -1), (-1, 1), (-1, -1)):
        low = float("inf")
        high = float("-inf")
        for i, (a, b) in enumerate(zip(arr1, arr2)):
            value = s1 * a + s2 * b + i
            low = min(low, value)
            high = max(high, value)
        best = max(best, high - low)
    return best
