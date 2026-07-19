class Solution:
    def numberOfUniqueGoodSubsequences(self, binary: str) -> int:
        modulus = 1_000_000_007
        ending_zero = 0
        ending_one = 0
        has_zero = 0

        for bit in binary:
            if bit == "1":
                ending_one = (ending_zero + ending_one + 1) % modulus
            else:
                ending_zero = (ending_zero + ending_one) % modulus
                has_zero = 1

        return (ending_zero + ending_one + has_zero) % modulus
