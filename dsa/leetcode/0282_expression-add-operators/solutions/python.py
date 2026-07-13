def solve(num: str, target: int) -> list[str]:
    expressions: list[str] = []

    def search(index: int, expression: str, value: int, last: int) -> None:
        if index == len(num):
            if value == target:
                expressions.append(expression)
            return
        for end in range(index + 1, len(num) + 1):
            if end > index + 1 and num[index] == "0":
                break
            token = num[index:end]
            operand = int(token)
            if index == 0:
                search(end, token, operand, operand)
            else:
                search(end, expression + "+" + token, value + operand, operand)
                search(end, expression + "-" + token, value - operand, -operand)
                search(
                    end,
                    expression + "*" + token,
                    value - last + last * operand,
                    last * operand,
                )

    search(0, "", 0, 0)
    return expressions
