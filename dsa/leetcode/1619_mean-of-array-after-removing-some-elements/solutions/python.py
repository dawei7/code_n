def solve(arr: list[int]) -> float:
    ordered = sorted(arr)
    trim = len(arr) // 20
    middle = ordered[trim : len(arr) - trim]
    return sum(middle) / len(middle)
