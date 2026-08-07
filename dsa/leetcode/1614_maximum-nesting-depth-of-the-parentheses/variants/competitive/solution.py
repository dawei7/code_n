class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        maximum = 0

        for character in s:
            if character == "(":
                depth += 1
                maximum = max(maximum, depth)
            elif character == ")":
                depth -= 1

        return maximum
