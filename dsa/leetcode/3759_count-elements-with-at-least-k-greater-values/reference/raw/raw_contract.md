## Function Contract

**Inputs**

- `nums`: A nonempty integer array whose occurrences are tested independently.
- `k`: The minimum number of strictly greater array elements required for qualification.

Let $n=\lvert\texttt{nums}\rvert$. Comparisons are against every element of the same array; equality never contributes to the strictly-greater count.

**Return value**

Return the number of occurrences in `nums` for which at least `k` other array values are strictly greater.
