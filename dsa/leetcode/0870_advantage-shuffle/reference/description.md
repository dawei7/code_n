### 1. Description

You are given two integer arrays `nums1` and `nums2` both of the same length. The **advantage** of `nums1` with respect to `nums2` is the number of indices `i` for which $\text{nums1}[i] > \text{nums2}[i]$.

Return *any permutation of *`nums1`* that maximizes its **advantage** with respect to *`nums2`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

- **Input:** $nums1 = [2,7,11,15], nums2 = [1,10,4,11]$
- **Output:** `[2,11,7,15]`
#### Example 2

- **Input:** $nums1 = [12,24,8,32], nums2 = [13,25,32,11]$
- **Output:** `[24,32,8,12]`

### 4. Constraints

- $1 \le \text{nums1.length} \le 10^{5}$

- $\text{nums2.length} = \text{nums1.length}$

- $0 \le \text{nums1}[i], \text{nums2}[i] \le 10^{9}$