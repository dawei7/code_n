def solve(s: str, k: int) -> str:
    position_in_word = 0
    expanded_length = 0

    for character in s:
        if character == " ":
            expanded_length += 1
            position_in_word = 0
        else:
            position_in_word += 1
            expanded_length += position_in_word

        if k < expanded_length:
            return character

    return ""
