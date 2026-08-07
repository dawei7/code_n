## Function Contract

**Inputs**

- `nums`: The integer array whose elements may be swapped.
- `forbidden`: An equally long array specifying the disallowed value at each index.

Let $N=\lvert\texttt{nums}\rvert=\lvert\texttt{forbidden}\rvert$. A swap must use distinct indices and changes only the order of `nums`; it does not alter `forbidden` or the multiset of values in `nums`.

**Return value**

Return the fewest swaps that produce `nums[i] != forbidden[i]` for every `0 <= i < N`. Return `-1` when no permutation of the available `nums` values can meet that condition.
