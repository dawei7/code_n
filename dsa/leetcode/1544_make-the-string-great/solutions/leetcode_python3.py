class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for character in s:
            if stack and stack[-1] != character and stack[-1].lower() == character.lower():
                stack.pop()
            else:
                stack.append(character)

        return "".join(stack)

