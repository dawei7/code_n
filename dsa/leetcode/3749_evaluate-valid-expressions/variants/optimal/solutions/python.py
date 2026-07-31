def solve(expression: str) -> int:
    frames: list[list[str | int | None]] = []
    current: int | None = None
    index = 0

    while index < len(expression):
        character = expression[index]
        if character.isalpha():
            frames.append([expression[index : index + 3], None])
            index += 4
        elif character == ",":
            frames[-1][1] = current
            current = None
            index += 1
        elif character == ")":
            operator, left = frames.pop()
            right = current
            if operator == "add":
                current = left + right
            elif operator == "sub":
                current = left - right
            elif operator == "mul":
                current = left * right
            else:
                current = left // right
            index += 1
        else:
            end = index + (character == "-")
            while end < len(expression) and expression[end].isdigit():
                end += 1
            current = int(expression[index:end])
            index = end

    return current
