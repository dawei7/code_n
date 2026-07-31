class Solution:
    def countAsterisks(self, s: str) -> int:
        outside = True
        answer = 0

        for character in s:
            if character == "|":
                outside = not outside
            elif character == "*" and outside:
                answer += 1

        return answer
