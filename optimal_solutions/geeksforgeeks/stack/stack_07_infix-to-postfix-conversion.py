"""Optimal solution for stack_07: Infix to Postfix Conversion.

Convert an infix arithmetic expression (operators
"""


def solve(expr, n):
    """Shunting-yard: infix -> postfix."""
    if n == 0:
        return ""
    prec = {"+": 1, "-": 1, "*": 2, "/": 2}
    stack = []
    out = []
    for ch in expr:
        if ch.isalnum():
            out.append(ch)
        elif ch == "(":
            stack.append(ch)
        elif ch == ")":
            while stack and stack[-1] != "(":
                out.append(stack.pop())
            if stack:
                stack.pop()  # pop the "("
        else:  # operator
            while stack and stack[-1] != "(" and prec.get(stack[-1], 0) >= prec[ch]:
                out.append(stack.pop())
            stack.append(ch)
    while stack:
        out.append(stack.pop())
    return "".join(out)
