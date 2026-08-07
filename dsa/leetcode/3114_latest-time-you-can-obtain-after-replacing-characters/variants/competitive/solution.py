class Solution:
    def findLatestTime(self, s: str) -> str:
        chars = list(s)

        if chars[0] == "?":
            chars[0] = "1" if chars[1] in {"?", "0", "1"} else "0"
        if chars[1] == "?":
            chars[1] = "1" if chars[0] == "1" else "9"
        if chars[3] == "?":
            chars[3] = "5"
        if chars[4] == "?":
            chars[4] = "9"

        return "".join(chars)
