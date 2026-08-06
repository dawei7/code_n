def solve(s: str) -> int:
    total = 0
    term = 0
    x = 0
    operator = "+"

    for i, c in enumerate(s):
        if c.isdigit():
            x = x * 10 + int(c)

        if (not c.isdigit() and c != " ") or i == len(s) - 1:
            if operator == "+":
                total += term
                term = x
            elif operator == "-":
                total += term
                term = -x
            elif operator == "*":
                term *= x
            else:
                term = (abs(term) // x) * (-1 if term < 0 else 1)

            operator = c
            x = 0

    return total + term
