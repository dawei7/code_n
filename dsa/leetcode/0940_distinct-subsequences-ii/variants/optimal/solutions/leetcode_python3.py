class Solution:
    def distinctSubseqII(self, s: str) -> int:
        modulus = 1_000_000_007
        ending = [0] * 26
        for character in s:
            total = sum(ending) % modulus
            ending[ord(character) - ord("a")] = (total + 1) % modulus
        return sum(ending) % modulus
