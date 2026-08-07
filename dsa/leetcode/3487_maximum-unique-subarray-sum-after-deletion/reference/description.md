## Description

You are given an integer array `nums`.

You are allowed to delete any number of elements from `nums` without making it **empty**. After performing the deletions, select a subarray of `nums` such that:

- All elements in the subarray are **unique**.

- The sum of the elements in the subarray is **maximized**.

Return the **maximum sum** of such a subarray.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,4,5]

**Output:** 15

**Explanation:**

Select the entire array without deleting any element to obtain the maximum sum.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,1,0,1,1]

**Output:** 1

**Explanation:**

Delete the element $\text{nums}[0] = 1$, $\text{nums}[1] = 1$, $\text{nums}[2] = 0$, and $\text{nums}[3] = 1$. Select the entire array `[1]` to obtain the maximum sum.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,2,-1,-2,1,0,-1]

**Output:** 3

**Explanation:**

Delete the elements $\text{nums}[2] = -1$ and $\text{nums}[3] = -2$, and select the subarray `[2, 1]` from `[1, 2, 1, 0, -1]` to obtain the maximum sum.

</div>
### Constraints

- $1 \le \text{nums.length} \le 100$

- $-100 \le \text{nums}[i] \le 100$