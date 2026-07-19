from math import gcd


class Solution:
    def fractionAddition(self, expression: str) -> str:
        numerator = 0
        denominator = 1
        index = 0

        while index < len(expression):
            sign = 1
            if expression[index] in "+-":
                if expression[index] == "-":
                    sign = -1
                index += 1

            term_numerator = 0
            while expression[index].isdigit():
                term_numerator = (
                    term_numerator * 10 + int(expression[index])
                )
                index += 1

            index += 1
            term_denominator = 0
            while (
                index < len(expression)
                and expression[index].isdigit()
            ):
                term_denominator = (
                    term_denominator * 10 + int(expression[index])
                )
                index += 1

            term_numerator *= sign
            numerator = (
                numerator * term_denominator
                + term_numerator * denominator
            )
            denominator *= term_denominator

            divisor = gcd(abs(numerator), denominator)
            numerator //= divisor
            denominator //= divisor

        return f"{numerator}/{denominator}"

