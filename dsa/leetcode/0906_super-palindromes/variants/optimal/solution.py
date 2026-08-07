from math import isqrt


class Solution:
    def superpalindromesInRange(self, left: str, right: str) -> int:
        lower = int(left)
        upper = int(right)
        root_limit = isqrt(upper)
        count = 0

        for odd_length in (True, False):
            seed = 1
            while True:
                digits = str(seed)
                mirrored = digits[-2::-1] if odd_length else digits[::-1]
                root = int(digits + mirrored)
                if root > root_limit:
                    break

                square = root * root
                square_digits = str(square)
                if square >= lower and square_digits == square_digits[::-1]:
                    count += 1
                seed += 1

        return count
