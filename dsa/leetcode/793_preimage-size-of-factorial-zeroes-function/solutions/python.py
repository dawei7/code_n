def _trailing_zeroes(value: int) -> int:
    total = 0
    while value:
        value //= 5
        total += value
    return total


def solve(k: int) -> int:
    low = 0
    high = 5 * k + 5
    while low < high:
        middle = (low + high) // 2
        if _trailing_zeroes(middle) < k:
            low = middle + 1
        else:
            high = middle
    return 5 if _trailing_zeroes(low) == k else 0
