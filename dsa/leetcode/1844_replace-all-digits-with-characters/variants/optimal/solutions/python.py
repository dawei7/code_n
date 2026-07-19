def solve(s: str) -> str:
    """Replace every odd-indexed digit with its shifted character."""
    characters = list(s)
    for index in range(1, len(characters), 2):
        characters[index] = chr(
            ord(characters[index - 1]) + int(characters[index])
        )
    return "".join(characters)
