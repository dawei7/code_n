class Solution:
    def calculate(self, s: str) -> int:
        result = number = 0
        sign = 1
        stack = []
        for character in s:
            if character.isdigit():
                number = number * 10 + int(character)
            elif character in "+-":
                result += sign * number
                number = 0
                sign = 1 if character == "+" else -1
            elif character == "(":
                stack.extend((result, sign))
                result = number = 0
                sign = 1
            elif character == ")":
                result += sign * number
                number = 0
                previous_sign = stack.pop()
                previous_result = stack.pop()
                result = previous_result + previous_sign * result
        return result + sign * number
