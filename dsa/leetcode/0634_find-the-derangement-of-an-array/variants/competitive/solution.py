class Solution:
    def findDerangement(self, n: int) -> int:
        modulus = 1_000_000_007
        two_back = 1
        one_back = 0
        for size in range(2, n + 1):
            two_back, one_back = one_back, (size - 1) * (one_back + two_back) % modulus
        return one_back
