from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        parts: List[str] = []
        previous = 0

        for index in spaces:
            parts.append(s[previous:index])
            parts.append(" ")
            previous = index

        parts.append(s[previous:])
        return "".join(parts)
