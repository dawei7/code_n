## Description

You are given an integer array `capacity`.

A subarray `capacity[l..r]` is considered **stable** if:

- Its length is **at least** 3.

- The **first** and **last** elements are each equal to the **sum** of all elements **strictly between** them (i.e., $\text{capacity}[l] = \text{capacity}[r] = capacity[l + 1] + capacity[l + 2] + ... + capacity[r - 1]$).

Return an integer denoting the number of **stable subarrays**.
### Function Contract

**Inputs**

- `capacity`: The integer array in which stable contiguous ranges are counted.

Each candidate is a nonempty contiguous subarray identified by inclusive endpoints `l` and `r`. Only candidates with $r - l + 1 \ge 3$ qualify for consideration. Values and interior sums may be negative, zero, or positive.

**Return value**

Return the integer count of all endpoint pairs `(l, r)` whose subarray satisfies both stability conditions. Overlapping and nested stable subarrays are counted separately.

### Examples

#### Example 1

<div class="example-block">
**Input:** capacity = [9,3,3,3,9]

**Output:** 2

**Explanation:**

- `[9,3,3,3,9]` is stable because the first and last elements are both 9, and the sum of the elements strictly between them is $3 + 3 + 3 = 9$.

- `[3,3,3]` is stable because the first and last elements are both 3, and the sum of the elements strictly between them is 3.

</div>
#### Example 2

<div class="example-block">
**Input:** capacity = [1,2,3,4,5]

**Output:** 0

**Explanation:**

No subarray of length at least 3 has equal first and last elements, so the answer is 0.

</div>
#### Example 3

<div class="example-block">
**Input:** capacity = [-4,4,0,0,-8,-4]

**Output:** 1

**Explanation:**

`[-4,4,0,0,-8,-4]` is stable because the first and last elements are both -4, and the sum of the elements strictly between them is $4 + 0 + 0 + (-8) = -4$

</div>
### Constraints

- $3 \le \text{capacity.length} \le 10^{5}$

- $-10^{9} \le \text{capacity}[i] \le 10^{9}$