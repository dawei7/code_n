class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        matched = 0

        for char in s:
            if matched < len(t) and char == t[matched]:
                matched += 1

        return len(t) - matched
