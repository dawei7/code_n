def solve(s: str) -> bool:
    mismatches = 0
    for left in range(len(s) // 2):
        if s[left] != s[~left]:
            mismatches += 1
            if mismatches > 2:
                return False
    return True
