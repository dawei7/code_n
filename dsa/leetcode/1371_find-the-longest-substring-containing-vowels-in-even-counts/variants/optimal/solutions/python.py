"""Reference solution for LeetCode 1371."""


def solve(s):
    vowel_bits = {"a": 0, "e": 1, "i": 2, "o": 3, "u": 4}
    first_index = [-2] * 32
    first_index[0] = -1
    mask = 0
    longest = 0

    for index, char in enumerate(s):
        bit = vowel_bits.get(char)
        if bit is not None:
            mask ^= 1 << bit
        if first_index[mask] == -2:
            first_index[mask] = index
        else:
            longest = max(longest, index - first_index[mask])

    return longest
