"""Inert review candidate for LeetCode 420: Strong Password Checker."""


def solve(password: str) -> int:
    n = len(password)
    missing_types = (
        int(not any(character.islower() for character in password))
        + int(not any(character.isupper() for character in password))
        + int(not any(character.isdigit() for character in password))
    )

    replacements = 0
    remainder_zero = 0
    remainder_one = 0
    i = 0
    while i < n:
        j = i + 1
        while j < n and password[j] == password[i]:
            j += 1
        length = j - i
        if length >= 3:
            replacements += length // 3
            remainder_zero += int(length % 3 == 0)
            remainder_one += int(length % 3 == 1)
        i = j

    if n < 6:
        return max(6 - n, missing_types)

    if n <= 20:
        return max(missing_types, replacements)

    deletions = n - 20
    remaining_deletions = deletions

    used = min(remaining_deletions, remainder_zero)
    replacements -= used
    remaining_deletions -= used

    used = min(remaining_deletions // 2, remainder_one)
    replacements -= used
    remaining_deletions -= 2 * used

    replacements -= min(replacements, remaining_deletions // 3)
    return deletions + max(missing_types, replacements)
