def solve(s: str) -> bool:
    seen_digit = False
    seen_point = False
    seen_exponent = False
    digit_after_exponent = True

    for index, character in enumerate(s):
        if character.isdigit():
            seen_digit = True
            if seen_exponent:
                digit_after_exponent = True
        elif character in "+-":
            if index > 0 and s[index - 1] not in "eE":
                return False
        elif character == ".":
            if seen_point or seen_exponent:
                return False
            seen_point = True
        elif character in "eE":
            if seen_exponent or not seen_digit:
                return False
            seen_exponent = True
            digit_after_exponent = False
        else:
            return False

    return seen_digit and digit_after_exponent
