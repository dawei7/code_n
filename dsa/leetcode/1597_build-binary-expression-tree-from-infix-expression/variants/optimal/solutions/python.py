from types import SimpleNamespace


def _node(value: str, left=None, right=None):
    return SimpleNamespace(val=value, left=left, right=right)


def solve(s: str):
    nodes = []
    operators = []
    precedence = {"+": 1, "-": 1, "*": 2, "/": 2}

    def combine() -> None:
        operator = operators.pop()
        right = nodes.pop()
        left = nodes.pop()
        nodes.append(_node(operator, left, right))

    for token in s:
        if token.isdigit():
            nodes.append(_node(token))
        elif token == "(":
            operators.append(token)
        elif token == ")":
            while operators[-1] != "(":
                combine()
            operators.pop()
        else:
            while (
                operators
                and operators[-1] != "("
                and precedence[operators[-1]] >= precedence[token]
            ):
                combine()
            operators.append(token)

    while operators:
        combine()
    return nodes[-1]
