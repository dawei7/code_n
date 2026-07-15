class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        score = 0
        depth = 0
        previous = ""

        for character in s:
            if character == "(":
                depth += 1
            else:
                depth -= 1
                if previous == "(":
                    score += 1 << depth
            previous = character

        return score
