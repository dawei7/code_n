class Solution:
    def kthLuckyNumber(self, k: int) -> str:
        return "".join("7" if bit == "1" else "4" for bit in bin(k + 1)[3:])
