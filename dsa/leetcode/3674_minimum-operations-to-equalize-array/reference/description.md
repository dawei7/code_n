### 1. Description

You are given an integer array `nums` of length `n`.

In one operation, choose any subarray `nums[l...r]` ($0 \le l \le r < n$) and **replace** each element in that subarray with the **bitwise AND** of all elements.

Return the **minimum** number of operations required to make all elements of `nums` equal.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2]

**Output:** 1

**Explanation:**

Choose `nums[0...1]`: $(1 AND 2) = 0$, so the array becomes `[0, 0]` and all elements are equal in 1 operation.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,5,5]

**Output:** 0

**Explanation:**

`nums` is `[5, 5, 5]` which already has all elements equal, so 0 operations are required.

</div>

### 4. Constraints

- $1 \le n = \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 10^{5}$