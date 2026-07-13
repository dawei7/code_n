def solve(word1: str, word2: str) -> int:
    """Return the minimum deletions needed to make the strings equal."""
    if len(word1) < len(word2):
        longer, shorter = word2, word1
    else:
        longer, shorter = word1, word2

    previous = [0] * (len(shorter) + 1)
    for left_char in longer:
        current = [0] * (len(shorter) + 1)
        for column, right_char in enumerate(shorter, start=1):
            if left_char == right_char:
                current[column] = previous[column - 1] + 1
            else:
                current[column] = max(previous[column], current[column - 1])
        previous = current

    lcs_length = previous[-1]
    return len(word1) + len(word2) - 2 * lcs_length

