class Solution:
    def resultingString(self, s: str) -> str:
        stack = []
        for char in s:
            if stack and abs(ord(stack[-1]) - ord(char)) in (1, 25):
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
