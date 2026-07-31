def solve(arr: list[int]) -> int:
    arr.sort()
    maximum = 0
    for value in arr:
        maximum = min(value, maximum + 1)
    return maximum
