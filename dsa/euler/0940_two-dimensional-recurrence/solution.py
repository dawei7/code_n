"""Project Euler Problem 940: Two-Dimensional Recurrence.

Mathematical formulation:
f_0 = 0, f_1 = 1, f_{i+1} = f_i + f_{i-1}.
A(0, 0) = 0, A(0, 1) = 1.
A(m+1, n) = A(m, n+1) + A(m, n)
A(m+1, n+1) = 2A(m+1, n) + A(m, n)
S(k) = sum_{i=2}^k sum_{j=2}^k A(f_i, f_j).
Given:
  S(3) = 30
  S(5) = 10396

Characteristic Polynomial & Closed Form Expression:
The 2D recurrence decomposes into the characteristic system:
  x^2 - x - 3 = 0,
with roots lambda_{1, 2} = (1 +- sqrt(13)) / 2 and eigenvalues mu_{1, 2} = lambda_{1, 2} + 1 = (3 +- sqrt(13)) / 2.
The closed-form bivariate solution is:
  A(m, n) = (mu_1^m * lambda_1^n - mu_2^m * lambda_2^n) / sqrt(13).

Separation of Variables in Finite Field F_p:
Modulo p = 1123581313, 13 is a quadratic residue with sqrt(13) = 984161357.
The double sum separates linearly:
  S(k) = [ (sum_{i=2}^k mu_1^{f_i})(sum_{j=2}^k lambda_1^{f_j}) - (sum_{i=2}^k mu_2^{f_i})(sum_{j=2}^k lambda_2^{f_j}) ] / sqrt(13) (mod p).

Evaluates S(50) = 969134784 modulo 1123581313 in <0.001s in 100% pure Python.
"""

from __future__ import annotations


def solve(k_limit: int = 50, modulo: int = 1123581313) -> int:
    """Compute S(k) modulo 1123581313."""
    # Find modular square root of 13 modulo 1123581313 via Tonelli-Shanks
    p = modulo
    q = p - 1
    s = 0
    while q % 2 == 0:
        q //= 2
        s += 1
    z = 2
    while pow(z, (p - 1) // 2, p) != p - 1:
        z += 1
    c = pow(z, q, p)
    x = pow(13, (q + 1) // 2, p)
    t = pow(13, q, p)
    m = s
    while t != 1:
        i = 0
        temp = t
        while temp != 1:
            temp = (temp * temp) % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        x = (x * b) % p
        t = (t * b * b) % p
        c = (b * b) % p
        m = i

    sqrt13 = x
    inv2 = pow(2, -1, modulo)
    inv_sqrt13 = pow(sqrt13, -1, modulo)

    l1 = ((1 + sqrt13) * inv2) % modulo
    l2 = ((1 - sqrt13) * inv2) % modulo
    mu1 = (l1 + 1) % modulo
    mu2 = (l2 + 1) % modulo

    # Generate Fibonacci sequence
    f = [0, 1]
    for _ in range(k_limit + 5):
        f.append(f[-1] + f[-2])

    # Linear separation of variables
    sum_mu1 = sum(pow(mu1, f[i], modulo) for i in range(2, k_limit + 1)) % modulo
    sum_l1 = sum(pow(l1, f[j], modulo) for j in range(2, k_limit + 1)) % modulo

    sum_mu2 = sum(pow(mu2, f[i], modulo) for i in range(2, k_limit + 1)) % modulo
    sum_l2 = sum(pow(l2, f[j], modulo) for j in range(2, k_limit + 1)) % modulo

    ans = ((sum_mu1 * sum_l1 - sum_mu2 * sum_l2) % modulo * inv_sqrt13) % modulo
    return ans


if __name__ == "__main__":
    print(solve())
