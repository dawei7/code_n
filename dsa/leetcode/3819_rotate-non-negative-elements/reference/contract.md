## Function Contract

**Inputs**

- `nums`: A non-empty array of integers.
- `k`: A non-negative number of left-rotation positions.

Let $N=\lvert\texttt{nums}\rvert$, and let $M$ be the number of elements in `nums` whose value is at least zero. Read those $M$ values from left to right as a separate sequence. When $M>0$, a rotation by `k` has the same effect as a rotation by `k % M`; when $M=0$, no position is movable and the array remains unchanged.

For every index holding a negative value in the input, the output must contain that same value at that same index. The rotated non-negative sequence fills the remaining indices from left to right.

**Return value**

Return the array produced by rotating and reinserting only the non-negative values.
