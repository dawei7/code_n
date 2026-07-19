## General
**A power of two has one set bit**

A positive power of two has exactly one set bit: `100...0`. Subtracting one clears that bit and sets every lower bit, producing `011...1`.

**Clear the least significant set bit**

For a positive integer, $n \mathbin{\&} (n - 1)$ is therefore zero exactly when `n` has one set bit. Check positivity separately because zero also satisfies the bit expression but is not a power of two.

The expression removes the least significant set bit from any positive `n`. For $n = 8$, binary $1000 \mathbin{\&} 0111$ is zero. For $n = 10$, $1010 \mathbin{\&} 1001$ leaves `1000`, proving another set bit remains.

If $n$ is a power of two, its sole set bit does not overlap any set bit of $n-1$, so the test succeeds. Conversely, if the test succeeds for positive $n$, removing the least significant set bit leaves zero, so no other set bit existed and $n$ is a power of two.

## Complexity detail
Fixed-width integer comparison, subtraction, and bitwise AND take $O(1)$ time and use $O(1)$ space.

## Alternatives and edge cases
- **Repeated division by two:** is correct but takes $O(\log n)$ time.
- **Logarithms:** introduce floating-point precision concerns.
- Negative values and zero return false; one is $2^{0}$ and returns true.
