class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        modulus = 1_000_000_007
        catalan = 1
        for k in range(numPeople // 2):
            catalan = catalan * (2 * (2 * k + 1)) % modulus
            catalan = catalan * pow(k + 2, modulus - 2, modulus) % modulus
        return catalan
