## General
**Strip the only permitted prime factors**

Reject nonpositive inputs. For each prime in `2, 3, 5`, repeatedly divide while it is a factor. The remaining quotient reveals whether any disallowed prime factor exists.

At every step, the current quotient times the removed factors equals the original `n`. After processing one allowed prime, that prime no longer divides the quotient.

**The residual quotient is a complete certificate**

If the final quotient is one, the removed twos, threes, and fives reconstruct the original number, proving that no other prime factor is needed. If a quotient greater than one remains, unique prime factorization gives it some prime divisor. All factors `2`, `3`, and `5` were removed exhaustively, so that divisor is disallowed and the original number cannot be ugly.

## Complexity detail

For a positive input, every successful division reduces the quotient by at least a factor of two, so there are
$O(\log n)$ divisions in the worst case. A nonpositive input returns in $O(1)$ time. The factor tuple, current factor,
and quotient occupy $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Trial-divide by every possible factor:** does unnecessary work up to the square root.
- **One:** it is the empty product of allowed primes, so the unchanged residual quotient is accepted.
- **Zero and negative values:** the early guard rejects them before the divisibility loops.
