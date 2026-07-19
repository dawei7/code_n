class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"

        middle = 1 << (n - 1)
        if k == middle:
            return "1"
        if k < middle:
            return self.findKthBit(n - 1, k)

        mirrored = (1 << n) - k
        bit = self.findKthBit(n - 1, mirrored)
        return "1" if bit == "0" else "0"

