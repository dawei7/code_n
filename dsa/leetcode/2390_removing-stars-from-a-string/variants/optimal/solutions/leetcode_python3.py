class Solution:
    def removeStars(self, s: str) -> str:
        remaining = []

        for character in s:
            if character == "*":
                remaining.pop()
            else:
                remaining.append(character)

        return "".join(remaining)
