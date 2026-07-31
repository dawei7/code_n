def solve(s: str, c: str) -> int:
    occurrences = 0
    for char in s:
        if char == c:
            occurrences += 1
    return occurrences * (occurrences + 1) // 2
