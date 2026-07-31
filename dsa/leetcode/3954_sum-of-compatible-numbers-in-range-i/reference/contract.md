## Function Contract

**Inputs**

- `n`: The positive integer whose distance and set bits define compatibility.
- `k`: The inclusive maximum allowed absolute difference from `n`.

**Return value**

Return the integer sum of all positive values `x` satisfying both `abs(n - x) <= k` and `(n & x) == 0`. Return `0` when no such value exists.
