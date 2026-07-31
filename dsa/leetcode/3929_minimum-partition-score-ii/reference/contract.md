## Function Contract

**Inputs**

- `nums`: A list of positive integers whose order must be preserved.
- `k`: The exact number of nonempty contiguous subarrays in the partition.

Let $N=\lvert\texttt{nums}\rvert$ and let

$$
S=\sum_{x\in\texttt{nums}}x.
$$

Each element is used exactly once. Cuts may be placed only between elements, and no resulting subarray may be empty.

**Return value**

Return an integer equal to the minimum possible sum of $T(s)=s(s+1)/2$ over the `k` subarray sums.
