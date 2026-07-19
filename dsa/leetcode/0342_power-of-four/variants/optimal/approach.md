## General
**First isolate powers of two**

Every power of four is also a power of two, but only every second power of two qualifies:

$4^{x} = 2^{(2x)}$.

First require $n > 0$. A positive power of two has exactly one set bit, which is recognized by $n \mathbin{\&} (n - 1) = 0$: subtracting one changes that lone `1` and all lower zeros, so the bitwise AND clears everything. This test alone would also accept `2`, `8`, and other powers of two with odd exponents.

**Then keep only even bit positions**

Number bit positions from zero at the least-significant bit. Powers of four place their only set bit at positions `0, 2, 4, ..., 30`. Within the signed 32-bit domain, hexadecimal mask `0x55555555` has `1` bits at precisely those even positions. Requiring `n & 0x55555555 != 0` therefore distinguishes powers of four from the remaining powers of two.

**Why the three filters are exact**

The three conditions are jointly sufficient. Positivity excludes zero and negatives; the one-bit test proves $n = 2^{p}$; and the mask proves that `p` is even. Hence $n = 2^{(2x)} = 4^{x}$. They are also necessary because every valid power of four is positive and has exactly one bit in an even position.

**Check the domain boundaries**

The value `1` is accepted: it is $4^{0}$ and its bit occupies position zero. The largest valid signed-32-bit value is $4^{15} = 2^{30} = 1,073,741,824$, whose set bit is also covered by the mask.

## Complexity detail
The input width is fixed at 32 bits. The method performs a constant number of comparisons and bitwise operations, so it takes $O(1)$ time and $O(1)$ space.

## Alternatives and edge cases
- **Repeated division by four:** is exact and easy to follow but takes $O(\log_{4} n)$ iterations.
- **Logarithm test:** is compact but risks floating-point rounding near integer exponents.
- **Modulo-three identity:** combines the power-of-two test with $n \bmod 3 = 1$ in constant time, although the bit-position mask expresses the structural reason more directly.
- Zero and negative integers are always false.
- Powers of two such as `2` or $2^{29}$ are counterexamples to the one-bit test alone because their set bit occupies an odd position.
