## Function Contract

**Inputs**

- `s`: A nonempty movement string containing only `U`, `D`, `L`, and `R`.
- `k`: The exact length of the one contiguous substring that must be removed.

Every possible start position for a length-`k` substring is considered. The retained prefix and suffix are concatenated implicitly and executed in their original order from $(0,0)$.

**Return value**

Return the number of distinct endpoints produced by the valid substring removals.
