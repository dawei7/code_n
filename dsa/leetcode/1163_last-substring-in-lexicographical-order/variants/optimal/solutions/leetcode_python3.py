class Solution:
    def lastSubstring(self, s: str) -> str:
        length = len(s)
        best = 0
        candidate = 1
        offset = 0
        while candidate + offset < length:
            if s[best + offset] == s[candidate + offset]:
                offset += 1
            elif s[best + offset] < s[candidate + offset]:
                best = max(best + offset + 1, candidate)
                candidate = best + 1
                offset = 0
            else:
                candidate = candidate + offset + 1
                offset = 0
        return s[best:]
