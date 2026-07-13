def solve(arr, k):
    mod = 1_000_000_007

    def kadane(values):
        best = current = 0
        for value in values:
            current = max(0, current + value)
            best = max(best, current)
        return best

    if k == 1:
        return kadane(arr) % mod
    best_twice = kadane(arr * 2)
    total = sum(arr)
    if total > 0:
        best_twice += (k - 2) * total
    return best_twice % mod
