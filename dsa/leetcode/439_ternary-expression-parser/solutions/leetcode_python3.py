class Solution:
    def parseTernary(self, expression: str) -> str:
        stack = []
        for character in reversed(expression):
            if stack and stack[-1] == "?":
                stack.pop()
                true_value = stack.pop()
                stack.pop()
                false_value = stack.pop()
                stack.append(true_value if character == "T" else false_value)
            else:
                stack.append(character)
        return stack[-1]
