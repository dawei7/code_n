def solve(s: str, k: int) -> str:
    characters = list(s)

    for index, character in enumerate(characters):
        value = ord(character) - ord("a")
        distance_to_a = min(value, 26 - value)

        if distance_to_a <= k:
            characters[index] = "a"
            k -= distance_to_a
        else:
            characters[index] = chr(ord(character) - k)
            break

    return "".join(characters)
