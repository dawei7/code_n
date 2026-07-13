from typing import List


class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        modulus = 1337
        base = a % modulus
        result = 1

        for digit in b:
            result = (
                pow(result, 10, modulus)
                * pow(base, digit, modulus)
                % modulus
            )
        return result

