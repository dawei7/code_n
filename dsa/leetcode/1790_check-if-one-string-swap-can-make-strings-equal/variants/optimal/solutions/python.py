def solve(s1: str, s2: str) -> bool:
    mismatches = []

    for first, second in zip(s1, s2):
        if first != second:
            mismatches.append((first, second))
            if len(mismatches) > 2:
                return False

    return not mismatches or (
        len(mismatches) == 2
        and mismatches[0] == mismatches[1][::-1]
    )
