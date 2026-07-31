def solve(s: str) -> int:
    frequencies = [0] * (len(s) + 1)
    longest_group = 0
    run_start = 0

    for index in range(1, len(s) + 1):
        if index < len(s) and s[index] == s[index - 1]:
            continue
        run_length = index - run_start
        frequencies[run_length] += 1
        longest_group = max(longest_group, frequencies[run_length])
        run_start = index

    return longest_group
