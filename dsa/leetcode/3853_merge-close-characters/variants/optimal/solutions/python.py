def solve(s: str, k: int) -> str:
    characters = list(s)

    while True:
        next_position = {}
        right_to_remove = -1

        for left in range(len(characters) - 1, -1, -1):
            character = characters[left]
            right = next_position.get(character)

            if right is not None and right - left <= k:
                right_to_remove = right

            next_position[character] = left

        if right_to_remove == -1:
            return "".join(characters)

        characters.pop(right_to_remove)
