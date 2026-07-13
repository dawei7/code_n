import re


def solve(s: str) -> int:
    tokens = re.findall(r"\d+|[()+\-*/]", s)
    position = 0

    def truncate_division(dividend: int, divisor: int) -> int:
        quotient = abs(dividend) // abs(divisor)
        return -quotient if (dividend < 0) != (divisor < 0) else quotient

    def parse_expression() -> int:
        nonlocal position
        value = parse_term()
        while position < len(tokens) and tokens[position] in {"+", "-"}:
            operator = tokens[position]
            position += 1
            term = parse_term()
            value = value + term if operator == "+" else value - term
        return value

    def parse_term() -> int:
        nonlocal position
        value = parse_factor()
        while position < len(tokens) and tokens[position] in {"*", "/"}:
            operator = tokens[position]
            position += 1
            factor = parse_factor()
            value = value * factor if operator == "*" else truncate_division(value, factor)
        return value

    def parse_factor() -> int:
        nonlocal position
        sign = 1
        while position < len(tokens) and tokens[position] in {"+", "-"}:
            if tokens[position] == "-":
                sign = -sign
            position += 1

        token = tokens[position]
        position += 1
        if token == "(":
            value = parse_expression()
            position += 1
            return sign * value
        return sign * int(token)

    return parse_expression()
