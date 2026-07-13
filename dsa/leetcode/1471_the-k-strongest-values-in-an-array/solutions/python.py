def solve(arr, k):
    if not arr or k <= 0:
        return []
    ordered = sorted(arr)
    median = ordered[(len(ordered) - 1) // 2]
    return sorted(arr, key=lambda value: (abs(value - median), value), reverse=True)[:k]
