SPECIAL_CHARACTERS = frozenset("!@#$%^&*()-+")


def solve(password: str) -> bool:
    if len(password) < 8:
        return False

    categories = 0
    previous = None

    for character in password:
        if character == previous:
            return False
        previous = character

        if "a" <= character <= "z":
            categories |= 1
        elif "A" <= character <= "Z":
            categories |= 2
        elif "0" <= character <= "9":
            categories |= 4
        elif character in SPECIAL_CHARACTERS:
            categories |= 8

    return categories == 15
