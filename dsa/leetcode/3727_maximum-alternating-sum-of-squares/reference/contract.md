## Function Contract

**Inputs**

- `nums`: The integer array whose elements may be placed in any order.

Let $n$ be the length of `nums`. An arrangement has $\lceil n/2 \rceil$ even-indexed terms that are added and $\lfloor n/2 \rfloor$ odd-indexed terms that are subtracted. Each term is squared before its sign in the alternating sum is applied, so an element's original sign does not change its contribution's magnitude.

**Return value**

Return the greatest integer score among all permutations of `nums`.
