## Function Contract

**Inputs**

- `nums1`: The number of leading `1` bits in each segment.
- `nums0`: The number of trailing `0` bits in each corresponding segment.

The arrays have the same non-zero length. Let $N=\texttt{nums1.length}$ and let

$$
L = \sum_{i=0}^{N-1}\bigl(\texttt{nums1[i]}+\texttt{nums0[i]}\bigr)
$$

be the total number of bits across all segments.

**Return value**

Return the maximum integer value obtainable by reordering and concatenating all segments, reduced modulo $10^9+7$.
