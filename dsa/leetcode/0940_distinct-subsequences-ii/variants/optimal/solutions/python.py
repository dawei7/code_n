"""Optimal app-local solution for LeetCode 940."""


MODULUS = 1_000_000_007


def solve(s):
    ending = [0] * 26
    for character in s:
        total = sum(ending) % MODULUS
        ending[ord(character) - ord("a")] = (total + 1) % MODULUS
    return sum(ending) % MODULUS
