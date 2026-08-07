class Solution:
    def numSub(self, s: str) -> int:
        modulo = 1_000_000_007
        run = 0
        total = 0
        for character in s:
            if character == "1":
                run += 1
                total = (total + run) % modulo
            else:
                run = 0
        return total
