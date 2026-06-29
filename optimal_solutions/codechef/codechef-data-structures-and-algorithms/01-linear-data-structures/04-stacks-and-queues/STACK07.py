


def solve():
    def get_precedence(op):
        if op in {'+', '-'}:
            return 1
        elif op in {'*', '/'}:
            return 2
        elif op == '^':
            return 3
        else:
            return 0

    def infix_to_postfix(infix):
        operator_stack = []
        postfix = []

        for c in infix:
            precedence = get_precedence(c)

            if c.isalnum():
                postfix.append(c)
            elif c == '(':
                operator_stack.append(c)
            elif c == ')':
                while operator_stack and operator_stack[-1] != '(':
                    postfix.append(operator_stack.pop())
                operator_stack.pop()  # Remove the '('
            else:
                while operator_stack and precedence <= get_precedence(operator_stack[-1]):
                    postfix.append(operator_stack.pop())
                operator_stack.append(c)

        while operator_stack:
            postfix.append(operator_stack.pop())

        return ''.join(postfix)

    t = int(input())
    for _ in range(t):
        infix_expression = input()
        postfix_expression = infix_to_postfix(infix_expression)
        print(postfix_expression)


if __name__ == "__main__":
    solve()
