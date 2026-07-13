def solve(arr):
    n = len(arr)
    for candidate in (arr[n // 4], arr[n // 2], arr[(3 * n) // 4]):
        if arr.count(candidate) * 4 > n:
            return candidate
    return arr[0]
