def solve(modulus: int = 10000000000) -> int:
    """Find the last ten digits of 28433 * 2^7830457 + 1 using modular exponentiation.
    
    Time Complexity: O(log E)
    Space Complexity: O(1)
    """
    power = pow(2, 7830457, modulus)
    return (28433 * power + 1) % modulus
