"""Optimal solution for stack_08: Evaluate Reverse Polish Notation.

Evaluate a postfix (Reverse Polish Notation) arithmetic
"""


def solve(tokens, n):
    """Evaluate a postfix expression and return the integer result."""
    if n == 0:
        return 0
    stack = []
    for tok in tokens:
        if tok in "+-*/":
            b = stack.pop()
            a = stack.pop()
            if tok == "+":
                stack.append(a + b)
            elif tok == "-":
                stack.append(a - b)
            elif tok == "*":
                stack.append(a * b)
            else:  # "/"
                # Truncate toward zero (Python's int() does this).
                stack.append(int(a / b))
        else:
            stack.append(int(tok))
    return stack[-1]
