def solve(s: str) -> str:
    if len(s) < 2:
        return ""

    characters = set(s)
    for index, character in enumerate(s):
        if character.swapcase() not in characters:
            left = solve(s[:index])
            right = solve(s[index + 1 :])
            return left if len(left) >= len(right) else right

    return s
