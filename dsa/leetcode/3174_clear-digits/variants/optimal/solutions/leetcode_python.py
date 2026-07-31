class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []

        for character in s:
            if character.isdigit():
                stack.pop()
            else:
                stack.append(character)

        return "".join(stack)
