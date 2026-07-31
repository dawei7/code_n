def solve(s: str, k: int) -> bool:
    run_start = 0
    for index in range(1, len(s) + 1):
        if index == len(s) or s[index] != s[run_start]:
            if index - run_start == k:
                return True
            run_start = index
    return False
