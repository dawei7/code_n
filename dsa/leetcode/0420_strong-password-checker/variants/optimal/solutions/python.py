"""Optimal app-local solution for LeetCode 420."""


def solve(password: str) -> int:
    missing_types = (
        int(not any(character.islower() for character in password))
        + int(not any(character.isupper() for character in password))
        + int(not any(character.isdigit() for character in password))
    )

    runs: list[int] = []
    index = 0
    while index < len(password):
        end = index + 1
        while end < len(password) and password[end] == password[index]:
            end += 1
        if end - index >= 3:
            runs.append(end - index)
        index = end

    if len(password) < 6:
        return max(6 - len(password), missing_types)

    replacements = sum(length // 3 for length in runs)
    if len(password) <= 20:
        return max(missing_types, replacements)

    deletions = len(password) - 20
    remaining_deletions = deletions

    remainder_zero = sum(1 for length in runs if length % 3 == 0)
    used = min(remaining_deletions, remainder_zero)
    replacements -= used
    remaining_deletions -= used

    remainder_one = sum(1 for length in runs if length % 3 == 1)
    used = min(remaining_deletions // 2, remainder_one)
    replacements -= used
    remaining_deletions -= 2 * used

    replacements -= min(replacements, remaining_deletions // 3)
    return deletions + max(missing_types, replacements)
