## Function Contract

**Inputs**

- `n`: The number of elements in the sequence.
- `s`: The required value of the first element.
- `m`: The maximum permitted absolute difference between adjacent elements.

All sequence elements are integers. Alternation is strict, so adjacent values cannot be equal even though their absolute difference is allowed to be less than or equal to `m`.

**Return value**

Return the maximum integer that can appear in any valid length-`n` alternating sequence beginning with `s` and respecting the adjacent-difference limit.
