def solve(arr: list[int]) -> int:
    length = len(arr)
    total = 0
    for index, value in enumerate(arr):
        containing = (index + 1) * (length - index)
        odd_containing = (containing + 1) // 2
        total += value * odd_containing
    return total
