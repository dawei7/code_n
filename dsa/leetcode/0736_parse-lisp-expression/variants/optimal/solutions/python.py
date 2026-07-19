from collections import defaultdict


def solve(expression: str) -> int:
    index = 0
    values = defaultdict(list)

    def skip_spaces():
        nonlocal index
        while index < len(expression) and expression[index] == " ":
            index += 1

    def read_token():
        nonlocal index
        start = index
        while index < len(expression) and expression[index] not in " ()":
            index += 1
        return expression[start:index]

    def evaluate():
        nonlocal index
        skip_spaces()

        if expression[index] != "(":
            token = read_token()
            if token[0] == "-" or token[0].isdigit():
                return int(token)
            return values[token][-1]

        index += 1
        operator = read_token()

        if operator == "add":
            result = evaluate() + evaluate()
        elif operator == "mult":
            result = evaluate() * evaluate()
        else:
            bound_names = []
            while True:
                skip_spaces()
                if expression[index] == "(" or expression[index] == "-" or expression[index].isdigit():
                    result = evaluate()
                    break

                name = read_token()
                skip_spaces()
                if expression[index] == ")":
                    result = values[name][-1]
                    break

                value = evaluate()
                values[name].append(value)
                bound_names.append(name)

            for name in reversed(bound_names):
                values[name].pop()

        skip_spaces()
        index += 1
        return result

    return evaluate()
