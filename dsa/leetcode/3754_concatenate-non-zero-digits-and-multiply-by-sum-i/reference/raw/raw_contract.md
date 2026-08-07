## Function Contract

**Inputs**

- `n`: The nonnegative integer whose decimal digits are filtered.

Let $D$ be the number of decimal digits in `n`, treating `0` as a one-digit representation. Removing zeros must preserve the relative order of every retained digit.

**Return value**

Return the concatenation of all nonzero digits multiplied by the sum of those same digits. If there are no retained digits, both the concatenated value and the result are `0`.
