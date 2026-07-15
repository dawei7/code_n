"""Optimal app-local solution for LeetCode 972."""

from fractions import Fraction


def solve(s, t):
    def parse(text):
        repeating = ""
        if "(" in text:
            main, repeating = text[:-1].split("(")
        else:
            main = text

        if "." in main:
            integer, non_repeating = main.split(".")
        else:
            integer, non_repeating = main, ""

        value = Fraction(int(integer), 1)
        finite_length = len(non_repeating)
        if non_repeating:
            value += Fraction(int(non_repeating), 10**finite_length)
        if repeating:
            value += Fraction(
                int(repeating),
                10**finite_length * (10 ** len(repeating) - 1),
            )
        return value

    return parse(s) == parse(t)
