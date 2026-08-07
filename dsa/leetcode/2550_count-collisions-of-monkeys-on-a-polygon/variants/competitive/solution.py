class Solution:
    def monkeyMove(self, n: int) -> int:
        modulus = 1_000_000_007
        return (pow(2, n, modulus) - 2) % modulus
