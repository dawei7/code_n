class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ones_seen = 0
        flips = 0

        for character in s:
            if character == "1":
                ones_seen += 1
            else:
                flips = min(flips + 1, ones_seen)

        return flips

