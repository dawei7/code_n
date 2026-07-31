from math import comb


class Solution:
    MODULO = 1_000_000_007

    def countNumbers(self, l: str, r: str, b: int) -> int:
        def count_up_to(value: int) -> int:
            if value < 0:
                return 0

            digits = []
            current = value
            if current == 0:
                digits.append(0)
            while current:
                digits.append(current % b)
                current //= b
            digits.reverse()

            if value == 0:
                return 1

            total = 1
            length = len(digits)
            for shorter in range(1, length):
                total += comb(shorter + b - 2, b - 2)

            minimum = 1
            for index, digit in enumerate(digits):
                remaining = length - index - 1
                for chosen in range(minimum, digit):
                    total += comb(
                        remaining + b - chosen - 1,
                        b - chosen - 1,
                    )
                if digit < minimum:
                    break
                minimum = digit
            else:
                total += 1

            return total % self.MODULO

        lower = int(l) - 1
        upper = int(r)
        return (count_up_to(upper) - count_up_to(lower)) % self.MODULO
