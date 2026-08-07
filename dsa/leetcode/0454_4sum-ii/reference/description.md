## Description

Given four integer arrays `nums1`, `nums2`, `nums3`, and `nums4` all of length `n`, return the number of tuples `(i, j, k, l)` such that:

- $0 \le i, j, k, l < n$

- $\text{nums1}[i] + \text{nums2}[j] + \text{nums3}[k] + \text{nums4}[l] = 0$
### Function Contract

**Inputs**

- `nums1`: The first integer array of length $n$.
- `nums2`: The second integer array of length $n$.
- `nums3`: The third integer array of length $n$.
- `nums4`: The fourth integer array of length $n$.

**Return value**

- Return the number of index tuples `(i, j, k, l)` whose four selected values sum to zero.

All four arrays are nonempty and have the same length.

### Examples
#### Example 1

- **Input:** $nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]$
- **Output:** `2`
- **Explanation:**
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
#### Example 2

- **Input:** $nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]$
- **Output:** `1`
### Constraints

- $n = \text{nums1.length}$

- $n = \text{nums2.length}$

- $n = \text{nums3.length}$

- $n = \text{nums4.length}$

- $1 \le n \le 200$

- $-2^{28} \le \text{nums1}[i], \text{nums2}[i], \text{nums3}[i], \text{nums4}[i] \le 2^{28}$