import math


def is_pandigital_9(s: str) -> bool:
    return "".join(sorted(s)) == "123456789"


def solve() -> int:
    """Find index k of first Fibonacci number F_k where first 9 and last 9 digits are 1-9 pandigital.
    
    Time Complexity: O(k)
    Space Complexity: O(1)
    """
    a, b = 1, 1
    k = 2

    log10_phi = math.log10((1 + 5**0.5) / 2)
    log10_sqrt5 = math.log10(5**0.5)

    mod = 10**9

    while True:
        k += 1
        a, b = b, (a + b) % mod

        # Fast check: last 9 digits
        s_last = f"{b:09d}"
        if is_pandigital_9(s_last):
            # Check first 9 digits via Binet log approximation
            frac = (k * log10_phi - log10_sqrt5) % 1.0
            first9 = str(int(10 ** (frac + 8)))
            if is_pandigital_9(first9):
                return k
