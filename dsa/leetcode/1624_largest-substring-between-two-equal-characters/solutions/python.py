def solve(s: str) -> int:
    first: dict[str, int] = {}
    longest = -1
    for index, character in enumerate(s):
        if character in first:
            longest = max(longest, index - first[character] - 1)
        else:
            first[character] = index
    return longest
