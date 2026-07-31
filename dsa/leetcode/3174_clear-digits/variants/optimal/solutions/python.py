def solve(s: str) -> str:
    stack: list[str] = []

    for character in s:
        if character.isdigit():
            stack.pop()
        else:
            stack.append(character)

    return "".join(stack)
