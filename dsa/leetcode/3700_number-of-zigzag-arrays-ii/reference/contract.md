## Function Contract

**Inputs**

- `n`: The required array length.
- `l`: The smallest permitted element value.
- `r`: The largest permitted element value.

Every element must lie in the inclusive integer interval `[l, r]`. Adjacent values cannot be equal, and the direction of successive adjacent comparisons cannot repeat.

**Return value**

Return the total number of valid length-`n` ZigZag arrays, reduced modulo $10^9+7$.
