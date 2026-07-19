def solve(s: str) -> int:
    seen_b = 0
    deletions = 0

    for character in s:
        if character == "b":
            seen_b += 1
        else:
            deletions = min(deletions + 1, seen_b)

    return deletions
