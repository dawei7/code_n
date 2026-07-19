from collections import Counter


def solve(arr: list[str], k: int) -> str:
    counts = Counter(arr)
    for value in arr:
        if counts[value] == 1:
            k -= 1
            if k == 0:
                return value
    return ""
