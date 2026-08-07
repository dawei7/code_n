## Description

You are given two integer arrays `nums1` and `nums0`, each of size `n`.

- $\text{nums1}[i]$ represents the number of `'1'`s in the $$i^{\text{th}}$$ segment.

- $\text{nums0}[i]$ represents the number of `'0'`s in the $$i^{\text{th}}$$ segment.

For each index `i`, construct a binary segment consisting of:

- $\text{nums1}[i]$ occurrences of `'1'` followed by

- $\text{nums0}[i]$ occurrences of `'0'`.

You may **rearrange** the order of these **segments** in any way. After rearranging, **concatenate** all segments to form a single binary string.

Return the **maximum** possible integer value of the concatenated binary string.

Since the result can be very large, return the answer **modulo** $10^{9} + 7$.
### Function Contract

**Inputs**

- `nums1`: The number of leading `1` bits in each segment.
- `nums0`: The number of trailing `0` bits in each corresponding segment.

The arrays have the same non-zero length. Let $N=\texttt{nums1.length}$ and let

$L = \sum_{i=0}^{N-1}\bigl(\texttt{\text{nums1}[i]}+\texttt{\text{nums0}[i]}\bigr)$

be the total number of bits across all segments.

**Return value**

Return the maximum integer value obtainable by reordering and concatenating all segments, reduced modulo $10^9+7$.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums1 = [1,2], nums0 = [1,0]

**Output:** 14

**Explanation:**

- At index 0, $\text{nums1}[0] = 1$ and $\text{nums0}[0] = 1$, so the segment formed is `"10"`.

- At index 1, $\text{nums1}[1] = 2$ and $\text{nums0}[1] = 0$, so the segment formed is `"11"`.

- Reordering the segments as `"11"` followed by `"10"` produces the binary string `"1110"`.

- The binary number `"1110"` has value 14 which is the maximum possible value.

</div>
#### Example 2

<div class="example-block">
**Input:** nums1 = [3,1], nums0 = [0,3]

**Output:** 120

**Explanation:**

- At index 0, $\text{nums1}[0] = 3$ and $\text{nums0}[0] = 0$, so the segment formed is `"111"`.

- At index 1, $\text{nums1}[1] = 1$ and $\text{nums0}[1] = 3$, so the segment formed is `"1000"`.

- Reordering the segments as `"111"` followed by `"1000"` produces the binary string `"1111000"`.

- The binary number `"1111000"` has value 120 which is the maximum possible value.

</div>
### Constraints

- $1 \le n = \text{nums1.length} = \text{nums0.length} \le 10^{5}$

- $0 \le \text{nums1}[i], \text{nums0}[i] \le 10^{4}$

- $\text{nums1}[i] + \text{nums0}[i] > 0$

- The total sum of all elements in `nums1` and `nums0` does not exceed 2 * $10^{5}$.