## Function Contract

**Inputs**

- `nums`: A nonempty array of positive integers, kept in its original order.
- `k`: The exact number of nonempty contiguous subarrays in the partition.

Let $N = \lvert\texttt{nums}\rvert$ and $K = \texttt{k}$. A partition places $K-1$ cuts between adjacent elements, so every element belongs to exactly one subarray and no subarray is empty.

**Return value**

Return the minimum integer score over all partitions of `nums` into exactly $K$ subarrays. Each subarray contributes the triangular number determined by the sum of its elements.
