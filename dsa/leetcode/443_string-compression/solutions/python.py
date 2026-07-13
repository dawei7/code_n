"""Optimal app-local solution for LeetCode 443."""


def solve(chars: list[str]) -> dict[str, object]:
    read = 0
    write = 0
    while read < len(chars):
        end = read + 1
        while end < len(chars) and chars[end] == chars[read]:
            end += 1

        chars[write] = chars[read]
        write += 1
        run_length = end - read
        if run_length > 1:
            for digit in str(run_length):
                chars[write] = digit
                write += 1
        read = end

    return {"length": write, "prefix": chars[:write]}
