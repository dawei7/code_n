class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        modulus = 1_000_000_007
        ways = [0] * (high + 1)
        ways[0] = 1
        answer = 0

        for length in range(1, high + 1):
            if length >= zero:
                ways[length] += ways[length - zero]
            if length >= one:
                ways[length] += ways[length - one]
            ways[length] %= modulus

            if length >= low:
                answer = (answer + ways[length]) % modulus

        return answer
