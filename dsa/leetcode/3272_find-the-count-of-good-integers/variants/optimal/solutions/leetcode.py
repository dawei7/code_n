from collections import Counter
from math import factorial


class Solution:
    def countGoodIntegers(self, n: int, k: int) -> int:
        half_length = (n + 1) // 2
        signatures = set()

        for half in range(10 ** (half_length - 1), 10**half_length):
            left = str(half)
            palindrome = left + left[-1 - (n % 2) :: -1]
            if int(palindrome) % k == 0:
                signatures.add("".join(sorted(palindrome)))

        answer = 0
        for signature in signatures:
            counts = Counter(signature)
            permutations = factorial(n)
            for count in counts.values():
                permutations //= factorial(count)

            if counts["0"] > 0:
                leading_zero = factorial(n - 1) // factorial(counts["0"] - 1)
                for digit, count in counts.items():
                    if digit != "0":
                        leading_zero //= factorial(count)
                permutations -= leading_zero

            answer += permutations

        return answer
