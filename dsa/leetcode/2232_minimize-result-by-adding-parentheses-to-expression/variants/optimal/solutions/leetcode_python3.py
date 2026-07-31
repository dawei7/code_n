class Solution:
    def minimizeResult(self, expression: str) -> str:
        plus = expression.index("+")
        best_value = float("inf")
        best_expression = ""

        for left in range(plus):
            for right in range(plus + 2, len(expression) + 1):
                outer_left = int(expression[:left]) if left else 1
                inner_left = int(expression[left:plus])
                inner_right = int(expression[plus + 1:right])
                outer_right = int(expression[right:]) if right < len(expression) else 1
                value = outer_left * (inner_left + inner_right) * outer_right
                if value < best_value:
                    best_value = value
                    best_expression = (
                        expression[:left]
                        + "("
                        + expression[left:right]
                        + ")"
                        + expression[right:]
                    )

        return best_expression
