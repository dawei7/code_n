def solve(num: str, target: int) -> list[str]:
    expressions: list[str] = []
    path: list[str] = []

    def search(i: int, value: int, last: int) -> None:
        if i == len(num):
            if value == target:
                expressions.append("".join(path))
            return
        for end in range(i + 1, len(num) + 1):
            if end > i + 1 and num[i] == "0":
                break
            token = num[i:end]
            operand = int(token)
            if i == 0:
                path.append(token)
                search(end, operand, operand)
                path.pop()
            else:
                path.extend(("+", token))
                search(end, value + operand, operand)
                path[-2] = "-"
                search(end, value - operand, -operand)
                path[-2] = "*"
                search(end, value - last + last * operand, last * operand)
                path.pop()
                path.pop()

    search(0, 0, 0)
    return expressions
