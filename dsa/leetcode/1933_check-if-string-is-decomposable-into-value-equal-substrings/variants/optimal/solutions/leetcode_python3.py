class Solution:
    def isDecomposable(self, s: str) -> bool:
        length_two_groups = 0
        index = 0

        while index < len(s):
            end = index + 1
            while end < len(s) and s[end] == s[index]:
                end += 1

            remainder = (end - index) % 3
            if remainder == 1:
                return False
            if remainder == 2:
                length_two_groups += 1

            index = end

        return length_two_groups == 1
