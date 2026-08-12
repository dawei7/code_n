import math


def solve(digits: int = 1000) -> int:
    """Find index of first Fibonacci number with given number of digits using logarithmic formula.
    
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    phi = (1 + math.sqrt(5)) / 2
    log10_phi = math.log10(phi)
    log10_sqrt5 = math.log10(5) / 2

    # We want log10(Fn) >= digits - 1
    return math.ceil((digits - 1 + log10_sqrt5) / log10_phi)
