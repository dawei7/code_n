"""Optimal solution for LeetCode 372: Super Pow."""


def solve(a: int, b: list[int]) -> int:
    modulus = 1337
    base = a % modulus
    result = 1

    for digit in b:
        result = pow(result, 10, modulus) * pow(base, digit, modulus) % modulus
    return result

