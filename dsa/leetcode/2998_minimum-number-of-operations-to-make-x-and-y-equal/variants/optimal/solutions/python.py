from functools import cache


def solve(x, y):
    @cache
    def visit(value):
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
