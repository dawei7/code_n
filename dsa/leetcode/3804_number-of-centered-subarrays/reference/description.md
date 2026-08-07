## Description

You are given an integer array `nums`.

A **subarray** of `nums` is called **centered** if the sum of its elements is **equal to at least one** element within that **same subarray**.

Return the number of **centered subarrays** of `nums`.
### Function Contract

**Inputs**

- `nums`: A nonempty array of integers.

A subarray is contiguous and nonempty. Equal values at different positions do not create separate counts for one fixed interval; each qualifying pair of endpoints contributes one centered subarray.

**Return value**

Return an integer equal to the number of contiguous intervals whose element sum occurs as a value somewhere inside that interval.

### Examples

#### Example 1

<div class="example-block">
**Input:** nums = [-1,1,0]

**Output:** 5

**Explanation:**

- All single-element subarrays (`[-1]`, `[1]`, `[0]`) are centered.

- The subarray `[1, 0]` has a sum of 1, which is present in the subarray.

- The subarray `[-1, 1, 0]` has a sum of 0, which is present in the subarray.

- Thus, the answer is 5.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [2,-3]

**Output:** 2

**Explanation:**

Only single-element subarrays (`[2]`, `[-3]`) are centered.

</div>
### Constraints

- $1 \le \text{nums.length} \le 500$

- $-10^{5} \le \text{nums}[i] \le 10^{5}$