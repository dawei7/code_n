class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulus = 1_000_000_007
        even_positions = (n + 1) // 2
        odd_positions = n // 2
        return (
            pow(5, even_positions, modulus)
            * pow(4, odd_positions, modulus)
            % modulus
        )
