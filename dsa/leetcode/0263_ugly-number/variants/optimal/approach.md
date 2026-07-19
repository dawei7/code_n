## General
**Strip the only permitted prime factors**

Reject nonpositive inputs. For each prime in `2, 3, 5`, repeatedly divide while it is a factor. The remaining quotient reveals whether any disallowed prime factor exists.

At every step, the current quotient times the removed factors equals the original `n`. After processing one allowed prime, that prime no longer divides the quotient.

**The residual quotient is a complete certificate**

If the final quotient is one, the removed twos, threes, and fives reconstruct the original number, proving that no other prime factor is needed. If a quotient greater than one remains, unique prime factorization gives it some prime divisor. All factors `2`, `3`, and `5` were removed exhaustively, so that divisor is disallowed and the original number cannot be ugly.

## Complexity detail
Every division reduces the positive quotient by at least a factor of two, so there are $O(\log n)$ divisions. Only the quotient and loop variables are stored.

## Alternatives and edge cases
- **Trial-divide by every possible factor:** does unnecessary work up to the square root.
- One is ugly as the empty product; zero and negative values are not.
