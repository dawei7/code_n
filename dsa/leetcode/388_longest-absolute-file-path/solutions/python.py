"""Optimal app-local solution for LeetCode 388: Longest Absolute File Path."""


def solve(input: str) -> int:
    prefix_lengths = [0]
    longest = 0
    index = 0

    while index < len(input):
        depth = 0
        while index < len(input) and input[index] == "\t":
            depth += 1
            index += 1

        name_length = 0
        is_file = False
        while index < len(input) and input[index] != "\n":
            is_file = is_file or input[index] == "."
            name_length += 1
            index += 1

        if is_file:
            longest = max(longest, prefix_lengths[depth] + name_length)
        else:
            child_prefix = prefix_lengths[depth] + name_length + 1
            if len(prefix_lengths) == depth + 1:
                prefix_lengths.append(child_prefix)
            else:
                prefix_lengths[depth + 1] = child_prefix

        index += 1

    return longest
