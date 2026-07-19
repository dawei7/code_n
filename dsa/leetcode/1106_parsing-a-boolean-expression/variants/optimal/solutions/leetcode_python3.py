class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = []
        for token in expression:
            if token == ",":
                continue
            if token != ")":
                stack.append(token)
                continue

            values = []
            while stack[-1] != "(":
                values.append(stack.pop() == "t")
            stack.pop()
            operator = stack.pop()
            if operator == "!":
                result = not values[0]
            elif operator == "&":
                result = all(values)
            else:
                result = any(values)
            stack.append("t" if result else "f")

        return stack[-1] == "t"
