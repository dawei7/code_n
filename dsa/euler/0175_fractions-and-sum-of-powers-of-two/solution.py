import math


def solve(p: int = 123456789, q: int = 987654321) -> str:
    """Find the Shortened Binary Expansion (SBE) of the smallest n for which f(n) / f(n-1) = p / q.

    Mathematical Principles Applied:
    --------------------------------
    1. Stern's Diatomic Sequence & Continued Fractions:
       Let f(n) be the number of hyperbinary representations of n.
       A fundamental theorem of the Stern-Brocot sequence states that the ratio
       f(n-1) / f(n) corresponds directly to the continued fraction expansion
       of the Shortened Binary Expansion of n in reverse:
       If n has binary representation 1^{a_1} 0^{a_2} 1^{a_3} ... 1^{a_k} (with k odd),
       then:
           f(n-1) / f(n) = [a_k; a_{k-1}, ..., a_2, a_1]

    2. Canonical Odd-Length Continued Fraction:
       Given f(n) / f(n-1) = p / q, we compute the continued fraction of q / p:
       q / p = [c_0; c_1, c_2, ..., c_m]
       Every rational fraction has two continued fraction representations:
       one of even length and one of odd length, via the identity:
           [..., c_m] == [..., c_m - 1, 1]
       Since the binary expansion of the smallest n must start with a 1 (MSB) and end with a 1 (LSB),
       the number of alternating bit-runs k must be ODD.
       If the Euclidean algorithm produces an even-length continued fraction, we expand the last term:
       c_m -> (c_m - 1, 1).

    3. Shortened Binary Expansion (SBE):
       Reversing the odd-length continued fraction gives the exact run-lengths of alternating
       1s and 0s from MSB to LSB:
           SBE(n) = (a_1, a_2, ..., a_k)

    Complexity:
    -----------
    - Time Complexity: O(log(min(p, q))) via Euclidean algorithm (~0.0001s).
    - Space Complexity: O(log(min(p, q))) memory for continued fraction array (~1 KB).
    """
    # Reduce fraction p/q by greatest common divisor
    g = math.gcd(p, q)
    p //= g
    q //= g

    # Compute Euclidean continued fraction of q / p
    cf = []
    a, b = q, p
    while b > 0:
        cf.append(a // b)
        a, b = b, a % b

    # Ensure canonical odd length so the bit runs start and end with '1's
    if len(cf) % 2 == 0:
        cf[-1] -= 1
        cf.append(1)

    # Reverse continued fraction to obtain MSB-to-LSB SBE run lengths
    cf.reverse()

    # Return comma-separated string representation
    return ",".join(map(str, cf))


if __name__ == "__main__":
    print(solve())
