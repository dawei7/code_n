def solve(s: str, x: str, y: str) -> str:
    count_x = 0
    count_y = 0
    middle = []

    for character in s:
        if character == x:
            count_x += 1
        elif character == y:
            count_y += 1
        else:
            middle.append(character)

    return y * count_y + "".join(middle) + x * count_x
