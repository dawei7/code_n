def solve(s: str) -> list[list[int]]:
    groups: list[list[int]] = []
    run_start = 0

    for end in range(1, len(s) + 1):
        if end < len(s) and s[end] == s[run_start]:
            continue
        if end - run_start >= 3:
            groups.append([run_start, end - 1])
        run_start = end

    return groups
