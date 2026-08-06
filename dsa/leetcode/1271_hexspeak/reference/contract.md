## Function Contract

**Input**

- `num`: a string containing the base-ten representation of a positive integer $n$, without leading zeros.

Let $d = \lfloor \log_{16} n \rfloor + 1$ be the number of digits in the uppercase hexadecimal representation of $n$.

**Return value**

- Return the Hexspeak representation after mapping every hexadecimal `0` to `O` and every hexadecimal `1` to `I`, provided that all remaining digits are uppercase letters from `A` through `F`.
- Return `"ERROR"` when any hexadecimal digit is from `2` through `9`.
