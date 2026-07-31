## General

**Keep only the two ends of the product**

Multiplying the entire range creates tens of thousands of digits even though
the answer needs at most ten of them. Maintain a floating leading significand
and divide it by ten whenever it reaches $10^{12}$. This preserves twelve
leading digits, more than the five ultimately reported.

Independently maintain the integer suffix modulo $10^{12}$. After multiplying
each range value, repeatedly divide out trailing factors of ten and increment
$C$, then discard digits beyond the last twelve. Because one multiplier is at
most $10^4$, it can introduce at most four new trailing zeros; the twelve-digit
buffer preserves more than enough low digits to remove them and still recover
the final five-digit suffix.

**Decide whether abbreviation is required**

Accumulate $\log_{10}(x)$ for every factor with compensated summation. After
subtracting $C$, the result is $\log_{10}$ of the zero-free product. A value
below $10$ means that product has at most ten digits, in which case the stored
twelve-digit suffix is the entire exact value.

Otherwise, scale the leading significand down to the interval
$[10^4, 10^5)$ and take its integer part as the first five digits. Format the
suffix modulo $10^5$ with exactly five positions and append `eC`.

The leading and suffix accumulators arise from the same full product.
Normalization changes only powers of ten, modular truncation preserves the low
digits, and every removed factor of ten is counted. They therefore produce the
required first digits, last digits, and exponent without materializing the
middle.

## Complexity detail

There are $N$ range values. Removing all factors of ten introduced by a value
requires at most $O(\log R)$ divisions, while all other updates are constant
time, for $O(N\log R)$ time. The accumulators have fixed size, so auxiliary
space is $O(1)$.

## Alternatives and edge cases

- **Construct the exact product:** Arbitrary-precision arithmetic makes this
  straightforward, but multiplication and decimal conversion grow with the
  product's digit count rather than remaining fixed-width.
- **Count factors two and five separately:** Canceling matched factors and
  multiplying the remaining residue modulo a power of ten also recovers the
  suffix, while logarithms provide the prefix.
- Exactly ten significant digits are not abbreviated; eleven digits are.
- A five-digit suffix beginning with zero must be padded, such as `05728`.
- A range containing a multiple of ten may still leave a very short product
  after its zeros are removed.
- Compensated logarithm accumulation reduces prefix and digit-boundary error
  over long ranges.
