class Solution:
    def numTilings(self, n: int) -> int:
        modulus = 1_000_000_007
        if n == 1:
            return 1
        if n == 2:
            return 2

        three_back = 1
        two_back = 1
        one_back = 2
        for _ in range(3, n + 1):
            current = (2 * one_back + three_back) % modulus
            three_back, two_back, one_back = two_back, one_back, current
        return one_back
