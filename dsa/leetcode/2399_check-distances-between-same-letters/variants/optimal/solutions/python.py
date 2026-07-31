def solve(s: str, distance: list[int]) -> bool:
    first_positions = [-1] * 26

    for index, letter in enumerate(s):
        letter_index = ord(letter) - ord("a")
        if first_positions[letter_index] == -1:
            first_positions[letter_index] = index
        elif index - first_positions[letter_index] - 1 != distance[letter_index]:
            return False

    return True
