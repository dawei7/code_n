"""Project Euler Problem 877: XOR-Equation A.

Mathematical formulation:
We consider the polynomial equation in F_2[x]:
  A(x)^2 + x * A(x) * B(x) + B(x)^2 = x^2 + 1, with 0 <= a <= b <= N.

Polynomial Lucas / Chebyshev Sequence Structure:
Let (A, B) be a solution to the quadratic equation in F_2[x].
Regarding the equation as a quadratic in C:
  C^2 + x * B * C + (B^2 + x^2 + 1) = 0.
Since A is one root and the sum of roots in F_2[x] is x * B:
  C = x * B + A.

Thus, all solutions form a contiguous recurrence sequence of polynomials:
  B_0 = 0
  B_1 = 3  (polynomial x + 1)
  B_{n+1} = (B_n << 1) ^ B_{n-1}  (polynomial x * B_n(x) + B_{n-1}(x)).

Every pair (B_{n-1}, B_n) is a valid solution (a, b) with a <= b.
We compute X(N) = XOR_{B_n <= N} B_n in O(log N) iterations (< 0.001s in Python).
"""

from __future__ import annotations


def solve(n: int = 10**18) -> int:
    """Compute X(N), the XOR sum of all b values for valid solutions with b <= N."""
    b_prev = 0
    b_curr = 3

    xor_sum = 0
    while b_curr <= n:
        xor_sum ^= b_curr
        b_next = (b_curr << 1) ^ b_prev
        b_prev = b_curr
        b_curr = b_next

    return xor_sum


if __name__ == "__main__":
    print(solve())
