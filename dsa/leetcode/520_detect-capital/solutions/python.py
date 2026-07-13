"""Single capitalization-count scan for LeetCode 520."""


def solve(word: str) -> bool:
    uppercase_count = sum(character.isupper() for character in word)
    return (
        uppercase_count == 0
        or uppercase_count == len(word)
        or (uppercase_count == 1 and word[0].isupper())
    )
