"""Project Euler Problem 722: Slowly Converging Series.

Find E_15(1 - 2^(-25)) formatted in scientific notation with 12 decimal places, where
E_k(q) = sum_{n=1}^inf sigma_k(n) q^n.
"""

from decimal import Decimal, getcontext


def solve(k: int = 15, p_pow: int = 25) -> str:
    """Compute E_k(1 - 2^(-p_pow)) using Eisenstein modular transformation asymptotic formula."""
    getcontext().prec = 120

    # Riemann zeta(k + 1)
    zeta_val = Decimal(0)
    for n in range(1, 200_000):
        term = Decimal(1) / (Decimal(n) ** (k + 1))
        zeta_val += term
        if term < Decimal("1e-50"):
            break

    # eps = 2^(-p_pow)
    eps = Decimal(1) / (Decimal(2) ** p_pow)

    # t = -ln(1 - eps) = sum_{i=1}^inf eps^i / i
    t = Decimal(0)
    cur = eps
    for i in range(1, 100):
        t += cur / Decimal(i)
        cur *= eps
        if cur < Decimal("1e-60"):
            break

    # k!
    fact_k = Decimal(1)
    for i in range(1, k + 1):
        fact_k *= Decimal(i)

    main_term = fact_k * zeta_val / (t ** (k + 1))

    # Format into standard scientific notation without '+' in exponent
    formatted = f"{main_term:.12e}".replace("e+", "e")
    return formatted


if __name__ == "__main__":
    print(solve())
