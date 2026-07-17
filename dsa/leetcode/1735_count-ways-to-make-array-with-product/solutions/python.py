from math import comb


MODULO = 1_000_000_007


def solve(queries: list[list[int]]) -> list[int]:
    answers: list[int] = []

    for length, product in queries:
        ways = 1
        divisor = 2
        remaining = product

        while divisor * divisor <= remaining:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            if exponent:
                ways = ways * comb(length + exponent - 1, exponent) % MODULO
            divisor += 1

        if remaining > 1:
            ways = ways * length % MODULO
        answers.append(ways)

    return answers
