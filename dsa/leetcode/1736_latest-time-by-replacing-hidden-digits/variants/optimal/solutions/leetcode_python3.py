class Solution:
    def maximumTime(self, time: str) -> str:
        digits = list(time)

        if digits[0] == "?":
            digits[0] = (
                "2"
                if digits[1] == "?" or digits[1] <= "3"
                else "1"
            )
        if digits[1] == "?":
            digits[1] = "3" if digits[0] == "2" else "9"
        if digits[3] == "?":
            digits[3] = "5"
        if digits[4] == "?":
            digits[4] = "9"

        return "".join(digits)
