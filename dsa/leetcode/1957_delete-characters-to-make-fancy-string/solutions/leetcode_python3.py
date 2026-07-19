class Solution:
    def makeFancyString(self, s: str) -> str:
        result = []

        for character in s:
            if len(result) >= 2 and result[-1] == result[-2] == character:
                continue
            result.append(character)

        return "".join(result)
