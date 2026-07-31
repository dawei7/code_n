from collections import deque


def solve(s: str) -> str:
    result = deque()
    is_reversed = False

    for character in s:
        if character == "*":
            if result:
                if is_reversed:
                    result.popleft()
                else:
                    result.pop()
        elif character == "#":
            result.extend(list(result))
        elif character == "%":
            is_reversed = not is_reversed
        elif is_reversed:
            result.appendleft(character)
        else:
            result.append(character)

    if is_reversed:
        return "".join(reversed(result))
    return "".join(result)
