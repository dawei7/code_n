"""Proposed app-local solution for LeetCode 388."""


def solve(input: str) -> int:
    prefix_lengths = [0]
    longest = 0
    i = 0

    while i < len(input):
        depth = 0
        while i < len(input) and input[i] == "\t":
            depth += 1
            i += 1

        name_length = 0
        is_file = False
        while i < len(input) and input[i] != "\n":
            is_file = is_file or input[i] == "."
            name_length += 1
            i += 1

        if is_file:
            longest = max(longest, prefix_lengths[depth] + name_length)
        else:
            child_prefix = prefix_lengths[depth] + name_length + 1
            if len(prefix_lengths) == depth + 1:
                prefix_lengths.append(child_prefix)
            else:
                prefix_lengths[depth + 1] = child_prefix

        i += 1

    return longest
