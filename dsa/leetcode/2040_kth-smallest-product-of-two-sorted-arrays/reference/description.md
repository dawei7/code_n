### 1. Description

Given two **sorted 0-indexed** integer arrays `nums1` and `nums2` as well as an integer `k`, return *the *$k^{\text{th}}$* (**1-based**) smallest product of *$\text{nums1}[i] * \text{nums2}[j]$* where *$0 \le i < \text{nums1.length}$* and *$0 \le j < \text{nums2.length}$.

### 2. Function Contract

**Inputs**

- `nums1`: Input parameter (`List[int]`).
- `nums2`: Input parameter (`List[int]`).
- `k`: Input parameter (`int`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $nums1 = [2,5], nums2 = [3,4], k = 2$
- **Output:** `8`
- **Explanation:** The 2 smallest products are:
- nums1[0] * nums2[0] = 2 * 3 = 6
- nums1[0] * nums2[1] = 2 * 4 = 8
The 2^nd smallest product is 8.

#### Example 2

- **Input:** $nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6$
- **Output:** `0`
- **Explanation:** The 6 smallest products are:
- nums1[0] * nums2[1] = (-4) * 4 = -16
- nums1[0] * nums2[0] = (-4) * 2 = -8
- nums1[1] * nums2[1] = (-2) * 4 = -8
- nums1[1] * nums2[0] = (-2) * 2 = -4
- nums1[2] * nums2[0] = 0 * 2 = 0
- nums1[2] * nums2[1] = 0 * 4 = 0
The 6^th smallest product is 0.

#### Example 3

- **Input:** $nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3$
- **Output:** `-6`
- **Explanation:** The 3 smallest products are:
- nums1[0] * nums2[4] = (-2) * 5 = -10
- nums1[0] * nums2[3] = (-2) * 4 = -8
- nums1[4] * nums2[0] = 2 * (-3) = -6
The 3^rd smallest product is -6.

### 4. Constraints

- $1 \le \text{nums1.length}, \text{nums2.length} \le 5 * 10^{4}$

- $-10^{5} \le \text{nums1}[i], \text{nums2}[j] \le 10^{5}$

- $1 \le k \le \text{nums1.length} * \text{nums2.length}$

- `nums1` and `nums2` are sorted.
