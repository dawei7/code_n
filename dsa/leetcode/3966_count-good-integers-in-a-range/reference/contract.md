## Function Contract

**Inputs**

- `l`: The inclusive lower endpoint of the integer range.
- `r`: The inclusive upper endpoint of the integer range.
- `k`: The greatest allowed absolute difference between adjacent decimal digits.

Let $D$ be the number of decimal digits in `r`.

**Return value**

Return the number of integers $x$ in the inclusive range $[l,r]$ for which every adjacent pair of digits has absolute difference at most `k`.
