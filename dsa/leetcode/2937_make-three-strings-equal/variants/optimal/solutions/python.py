def solve(s1: str, s2: str, s3: str) -> int:
    prefix = 0
    for char1, char2, char3 in zip(s1, s2, s3):
        if char1 != char2 or char1 != char3:
            break
        prefix += 1

    if prefix == 0:
        return -1
    return len(s1) + len(s2) + len(s3) - 3 * prefix
