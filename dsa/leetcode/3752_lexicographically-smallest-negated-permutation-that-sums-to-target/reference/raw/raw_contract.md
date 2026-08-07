## Function Contract

**Inputs**

- `n`: The array length and the largest required absolute value.
- `target`: The required signed sum of all array elements.

Every magnitude in the inclusive range $1$ through $n$ must occur once. Lexicographic order compares the first unequal positions of two arrays by their ordinary signed integer values.

**Return value**

Return the lexicographically smallest valid signed permutation, or `[]` if no assignment of signs can produce `target`.
