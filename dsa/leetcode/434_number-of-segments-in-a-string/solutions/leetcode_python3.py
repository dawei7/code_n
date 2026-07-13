class Solution:
    def countSegments(self, s: str) -> int:
        return sum(
            character != " " and (index == 0 or s[index - 1] == " ")
            for index, character in enumerate(s)
        )
