def parse(expression: str) -> tuple[int, int]:
    coefficient = 0
    constant = 0
    index = 0

    while index < len(expression):
        sign = 1
        if expression[index] in "+-":
            sign = 1 if expression[index] == "+" else -1
            index += 1

        value = 0
        has_digits = False
        while index < len(expression) and expression[index].isdigit():
            value = value * 10 + int(expression[index])
            has_digits = True
            index += 1

        if index < len(expression) and expression[index] == "x":
            coefficient += sign * (value if has_digits else 1)
            index += 1
        else:
            constant += sign * value

    return coefficient, constant


def solve(equation: str) -> str:
    left, right = equation.split("=")
    left_coefficient, left_constant = parse(left)
    right_coefficient, right_constant = parse(right)

    coefficient = left_coefficient - right_coefficient
    constant = right_constant - left_constant
    if coefficient == 0:
        return "Infinite solutions" if constant == 0 else "No solution"
    return f"x={constant // coefficient}"
