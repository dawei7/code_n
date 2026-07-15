def solve(num):
    value = int(num)
    characters = []
    letters = "ABCDEF"

    while value:
        value, digit = divmod(value, 16)
        if digit == 0:
            characters.append("O")
        elif digit == 1:
            characters.append("I")
        elif 10 <= digit <= 15:
            characters.append(letters[digit - 10])
        else:
            return "ERROR"

    return "".join(reversed(characters))
