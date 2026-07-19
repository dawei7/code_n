def solve(s: str, knowledge: list[list[str]]) -> str:
    values = dict(knowledge)
    result = []
    index = 0

    while index < len(s):
        if s[index] != "(":
            result.append(s[index])
            index += 1
            continue

        closing = s.find(")", index + 1)
        key = s[index + 1 : closing]
        result.append(values.get(key, "?"))
        index = closing + 1

    return "".join(result)
