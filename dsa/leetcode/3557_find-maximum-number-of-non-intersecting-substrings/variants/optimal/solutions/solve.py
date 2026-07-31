def solve(word: str) -> int:
    selected = 0
    first_position: dict[str, int] = {}

    for index, character in enumerate(word):
        if character in first_position and index - first_position[character] >= 3:
            selected += 1
            first_position = {}
        else:
            first_position.setdefault(character, index)

    return selected
