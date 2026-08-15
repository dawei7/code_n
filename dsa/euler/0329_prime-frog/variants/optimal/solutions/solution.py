"""Project Euler 329: Prime Frog

Find the probability that the prime frog croaks the sequence 'PPPPNNPPPNPPNPN',
given as a reduced fraction p/q.
"""

from __future__ import annotations

from fractions import Fraction
import math


def solve(target: str = "PPPPNNPPPNPPNPN", num_squares: int = 500) -> str:
    """Calculates the probability of observing the croak sequence target using the exact

    Hidden Markov Model (HMM) forward algorithm with Fraction rational arithmetic.
    """
    # 1. Sieve prime numbers up to num_squares
    is_prime = [False] * (num_squares + 1)
    for i in range(2, num_squares + 1):
        if all(i % d != 0 for d in range(2, int(math.isqrt(i)) + 1)):
            is_prime[i] = True

    # 2. Initial state distribution: uniform 1/num_squares on all squares
    prob: dict[int, Fraction] = {
        x: Fraction(1, num_squares) for x in range(1, num_squares + 1)
    }

    # 3. Exact HMM Forward Pass
    for step, croak in enumerate(target):
        next_prob: dict[int, Fraction] = {}
        for x, p in prob.items():
            # Emission probability
            if is_prime[x]:
                emit = Fraction(2, 3) if croak == "P" else Fraction(1, 3)
            else:
                emit = Fraction(1, 3) if croak == "P" else Fraction(2, 3)
            p_after_emit = p * emit

            # State transition to neighboring squares
            if step < len(target) - 1:
                if x == 1:
                    next_prob[2] = next_prob.get(2, Fraction(0)) + p_after_emit
                elif x == num_squares:
                    next_prob[num_squares - 1] = (
                        next_prob.get(num_squares - 1, Fraction(0))
                        + p_after_emit
                    )
                else:
                    half = Fraction(1, 2)
                    next_prob[x - 1] = (
                        next_prob.get(x - 1, Fraction(0)) + p_after_emit * half
                    )
                    next_prob[x + 1] = (
                        next_prob.get(x + 1, Fraction(0)) + p_after_emit * half
                    )
            else:
                next_prob[x] = (
                    next_prob.get(x, Fraction(0)) + p_after_emit
                )

        prob = next_prob

    total_prob = sum(prob.values())
    return f"{total_prob.numerator}/{total_prob.denominator}"


if __name__ == "__main__":
    print(solve())
