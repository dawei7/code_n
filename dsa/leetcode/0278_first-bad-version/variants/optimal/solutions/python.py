def solve(n: int, bad: int) -> int:
    left = 1
    right = n
    while left < right:
        middle = left + (right - left) // 2
        if middle >= bad:
            right = middle
        else:
            left = middle + 1
    return left
