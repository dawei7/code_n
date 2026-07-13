def solve(n: int, k: int) -> list[int]:
    result = list(range(1, n - k))
    low = n - k
    high = n
    while low <= high:
        result.append(low)
        low += 1
        if low <= high:
            result.append(high)
            high -= 1
    return result
