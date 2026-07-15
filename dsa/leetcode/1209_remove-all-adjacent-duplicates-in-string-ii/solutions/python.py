def solve(s: str, k: int) -> str:
    stack: list[list[object]] = []
    for character in s:
        if stack and stack[-1][0] == character:
            stack[-1][1] = int(stack[-1][1]) + 1
            if stack[-1][1] == k:
                stack.pop()
        else:
            stack.append([character, 1])
    return "".join(str(character) * int(count) for character, count in stack)
