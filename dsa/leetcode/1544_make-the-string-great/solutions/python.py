def solve(s):
    stack = []

    for character in s:
        if stack and stack[-1] != character and stack[-1].lower() == character.lower():
            stack.pop()
        else:
            stack.append(character)

    return "".join(stack)

