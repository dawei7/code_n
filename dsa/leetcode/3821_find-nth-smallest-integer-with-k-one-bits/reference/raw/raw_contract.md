## Function Contract

**Inputs**

- `n`: The positive, one-based rank of the requested integer.
- `k`: The exact number of one bits required in its binary representation.

Let $B=50$. Because the answer is less than $2^B$, every candidate can be viewed as a $B$-bit string with leading zeros. A candidate qualifies when exactly `k` of those positions contain `1`. Leading zeros do not change the represented positive integer or its one-bit count.

The source guarantee ensures that `n` does not exceed the number of qualifying values below $2^B$ for the supplied `k`.

**Return value**

Return the `n`th smallest positive integer whose binary representation contains exactly `k` ones.
