def solve(expression: str) -> int:
    values = []
    operators = []
    index = 0
    while index < len(expression):
        character = expression[index]
        if character.isalpha():
            operators.append(expression[index : index + 3])
            index += 3
        elif character == "-" or character.isdigit():
            end = index + (character == "-")
            while end < len(expression) and expression[end].isdigit():
                end += 1
            values.append(int(expression[index:end]))
            index = end
        elif character == ")":
            right = values.pop()
            left = values.pop()
            operator = operators.pop()
            if operator == "add":
                values.append(left + right)
            elif operator == "sub":
                values.append(left - right)
            elif operator == "mul":
                values.append(left * right)
            else:
                values.append(left // right)
            index += 1
        else:
            index += 1
    return values[0]
