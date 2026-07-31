## Function Contract

**Inputs**

- `n`: A positive integer whose decimal digits determine the score.

Let $D=\lfloor\log_{10} n\rfloor+1$ be the number of decimal digits in `n`.

**Return value**

Return the sum of `d * freq(d)` over every distinct decimal digit `d` present in `n`.
