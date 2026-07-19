class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth = 0
        answer = []

        for character in s:
            if character == "(":
                if depth > 0:
                    answer.append(character)
                depth += 1
            else:
                depth -= 1
                if depth > 0:
                    answer.append(character)

        return "".join(answer)
