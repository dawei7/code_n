class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        modulus = 1_000_000_007
        if k > m:
            return 0
        current = [[0] * (m + 1) for _ in range(k + 1)]
        for maximum in range(1, m + 1):
            current[1][maximum] = 1

        for _ in range(1, n):
            following = [[0] * (m + 1) for _ in range(k + 1)]
            for cost in range(1, k + 1):
                smaller_prefix = 0
                for maximum in range(1, m + 1):
                    following[cost][maximum] = (
                        current[cost][maximum] * maximum + smaller_prefix
                    ) % modulus
                    smaller_prefix = (
                        smaller_prefix + current[cost - 1][maximum]
                    ) % modulus
            current = following

        return sum(current[k]) % modulus
