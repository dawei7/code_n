## Description

You are given two integer arrays `nums1` and `nums2` sorted in **non-decreasing order** and an integer `k`.

Define a pair `(u, v)` which consists of one element from the first array and one element from the second array.

Return *the* `k` *pairs* $(u_{1}, v_{1}), (u_{2}, v_{2}), ..., (u_{k}, v_{k})$ *with the smallest sums*.
### Function Contract

**Inputs**

- `nums1`: The first non-decreasing integer array.
- `nums2`: The second non-decreasing integer array.
- `k`: The number of smallest-sum pairs to return.

**Return value**

Return `k` value pairs formed by one occurrence from each array whose sums are the `k` smallest available sums.

### Examples

#### Example 1

- **Input:** $nums1 = [1,7,11], nums2 = [2,4,6], k = 3$
- **Output:** `[[1,2],[1,4],[1,6]]`
- **Explanation:** The first 3 pairs are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]
#### Example 2

- **Input:** $nums1 = [1,1,2], nums2 = [1,2,3], k = 2$
- **Output:** `[[1,1],[1,1]]`
- **Explanation:** The first 2 pairs are returned from the sequence: [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]
### Constraints

- $1 \le \text{nums1.length}, \text{nums2.length} \le 10^{5}$

- $-10^{9} \le \text{nums1}[i], \text{nums2}[i] \le 10^{9}$

- `nums1` and `nums2` both are sorted in **non-decreasing order**.

- $1 \le k \le 10^{4}$

- $k \le \text{nums1.length} * \text{nums2.length}$