def solve(n: int, pick: int) -> int:
    def guess(num: int) -> int:
        if num == pick:
            return 0
        return -1 if num > pick else 1

    left = 1
    right = n

    while left <= right:
        middle = left + (right - left) // 2
        response = guess(middle)
        if response == 0:
            return middle
        if response < 0:
            right = middle - 1
        else:
            left = middle + 1

    return -1
