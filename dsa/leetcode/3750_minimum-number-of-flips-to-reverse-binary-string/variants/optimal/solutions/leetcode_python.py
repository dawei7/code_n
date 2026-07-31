class Solution:
    def minimumFlips(self, n: int) -> int:
        bits = bin(n)[2:]
        return sum(left != right for left, right in zip(bits, reversed(bits)))
