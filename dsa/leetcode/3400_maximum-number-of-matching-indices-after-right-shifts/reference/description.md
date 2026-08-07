## Description

You are given two integer arrays, `nums1` and `nums2`, of the same length.

An index `i` is considered **matching** if $\text{nums1}[i] = \text{nums2}[i]$.

Return the **maximum** number of **matching** indices after performing any number of **right shifts** on `nums1`.

A **right shift** is defined as shifting the element at index `i` to index $(i + 1) \% n$, for all indices.
### Function Contract

- Refer to method signature.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums1 = [3,1,2,3,1,2], nums2 = [1,2,3,1,2,3]

**Output:** 6

**Explanation:**

If we right shift `nums1` 2 times, it becomes `[1, 2, 3, 1, 2, 3]`. Every index matches, so the output is 6.

</div>
#### Example 2

<div class="example-block">
**Input:** nums1 = [1,4,2,5,3,1], nums2 = [2,3,1,2,4,6]

**Output:** 3

**Explanation:**

If we right shift `nums1` 3 times, it becomes `[5, 3, 1, 1, 4, 2]`. Indices 1, 2, and 4 match, so the output is 3.

</div>
### Constraints

- $\text{nums1.length} = \text{nums2.length}$

- $1 \le \text{nums1.length}, \text{nums2.length} \le 3000$

- $1 \le \text{nums1}[i], \text{nums2}[i] \le 10^{9}$