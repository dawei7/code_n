## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers.

Let $N=\lvert\texttt{nums}\rvert$. Uniqueness is determined from each value's frequency in the entire array, while priority is determined by the original index. The requested result is therefore the first array element `x` for which $x \bmod 2 = 0$ and the total count of `x` is one.

**Return value**

Return the earliest-by-index even integer that appears exactly once. Return `-1` when no such integer exists.
