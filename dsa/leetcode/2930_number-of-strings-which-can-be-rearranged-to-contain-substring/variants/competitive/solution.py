class Solution:
    def stringCount(self, n: int) -> int:
        modulus = 1_000_000_007
        return (
            pow(26, n, modulus)
            - 3 * pow(25, n, modulus)
            - n * pow(25, n - 1, modulus)
            + 3 * pow(24, n, modulus)
            + 2 * n * pow(24, n - 1, modulus)
            - pow(23, n, modulus)
            - n * pow(23, n - 1, modulus)
        ) % modulus
