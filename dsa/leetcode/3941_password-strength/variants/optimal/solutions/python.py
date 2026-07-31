def solve(password: str) -> int:
    strength = 0
    seen: set[str] = set()

    for character in password:
        if character in seen:
            continue
        seen.add(character)

        if "a" <= character <= "z":
            strength += 1
        elif "A" <= character <= "Z":
            strength += 2
        elif "0" <= character <= "9":
            strength += 3
        else:
            strength += 5

    return strength
