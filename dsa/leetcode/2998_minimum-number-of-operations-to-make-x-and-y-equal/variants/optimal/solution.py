from functools import cache


class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        @cache
        def visit(value: int) -> int:
            if value <= y:
                return y - value

            answer = value - y
            for divisor in (5, 11):
                remainder = value % divisor
                answer = min(answer, remainder + 1 + visit(value // divisor))

                increase = (-value) % divisor
                answer = min(
                    answer,
                    increase + 1 + visit((value + increase) // divisor),
                )
            return answer

        return visit(x)
