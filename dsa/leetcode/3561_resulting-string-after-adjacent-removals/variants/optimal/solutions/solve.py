def solve(s: str) -> str:
    stack: list[str] = []
    for char in s:
        if stack and abs(ord(stack[-1]) - ord(char)) in (1, 25):
            stack.pop()
        else:
            stack.append(char)
    return "".join(stack)
