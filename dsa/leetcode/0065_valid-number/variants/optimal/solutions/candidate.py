def solve(s: str) -> bool:
    seen_digit = False
    seen_point = False
    seen_exponent = False
    digit_after_exponent = True

    for i, c in enumerate(s):
        if c.isdigit():
            seen_digit = True
            if seen_exponent:
                digit_after_exponent = True
        elif c in "+-":
            if i > 0 and s[i - 1] not in "eE":
                return False
        elif c == ".":
            if seen_point or seen_exponent:
                return False
            seen_point = True
        elif c in "eE":
            if seen_exponent or not seen_digit:
                return False
            seen_exponent = True
            digit_after_exponent = False
        else:
            return False

    return seen_digit and digit_after_exponent
