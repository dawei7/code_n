## Description

You are given two integer arrays `nums1` and `nums2`, each of length `n`. You may perform the following **split-and-merge operation** on `nums1` any number of times:

- Choose a subarray `nums1[L..R]`.

- Remove that subarray, leaving the prefix `nums1[0..L-1]` (empty if $L = 0$) and the suffix `nums1[R+1..n-1]` (empty if $R = n - 1$).

- Re-insert the removed subarray (in its original order) at **any** position in the remaining array (i.e., between any two elements, at the very start, or at the very end).

Return the **minimum** number of **split-and-merge operations** needed to transform `nums1` into `nums2`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums1 = [3,1,2], nums2 = [1,2,3]

**Output:** 1

**Explanation:**

- Split out the subarray `[3]` ($L = 0$, $R = 0$); the remaining array is `[1,2]`.

- Insert `[3]` at the end; the array becomes `[1,2,3]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums1 = [1,1,2,3,4,5], nums2 = [5,4,3,2,1,1]

**Output: **3

**Explanation:**

- Remove `[1,1,2]` at indices $0 - 2$; remaining is `[3,4,5]`; insert `[1,1,2]` at position `2`, resulting in `[3,4,1,1,2,5]`.

- Remove `[4,1,1]` at indices $1 - 3$; remaining is `[3,2,5]`; insert `[4,1,1]` at position `3`, resulting in `[3,2,5,4,1,1]`.

- Remove `[3,2]` at indices $0 - 1$; remaining is `[5,4,1,1]`; insert `[3,2]` at position `2`, resulting in `[5,4,3,2,1,1]`.

</div>
### Constraints

- $2 \le n = \text{nums1.length} = \text{nums2.length} \le 6$

- $-10^{5} \le \text{nums1}[i], \text{nums2}[i] \le 10^{5}$

- `nums2` is a **permutation** of `nums1`.