class Solution:
    def isValid(self, s: str) -> bool:
        matching = {")": "(", "]": "[", "}": "{"}
        stack = []
        for bracket in s:
            if bracket in matching:
                if not stack or stack.pop() != matching[bracket]:
                    return False
            else:
                stack.append(bracket)
        return not stack
