### 1. Description

You are given an integer array `nums`. In one operation, you can select a subarray and replace it with a single element equal to its **maximum** value.

Return the **maximum possible size** of the array after performing zero or more operations such that the resulting array is **non-decreasing**.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [4,2,5,3,5]

**Output:** 3

**Explanation:**

One way to achieve the maximum size is:

- Replace subarray $nums[1..2] = [2, 5]$ with `5` → `[4, 5, 3, 5]`.

- Replace subarray $nums[2..3] = [3, 5]$ with `5` → `[4, 5, 5]`.

The final array `[4, 5, 5]` is non-decreasing with size 3.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,2,3]

**Output:** 3

**Explanation:**

No operation is needed as the array `[1,2,3]` is already non-decreasing.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 2 * 10^{5}$

- $1 \le \text{nums}[i] \le 2 * 10^{5}$