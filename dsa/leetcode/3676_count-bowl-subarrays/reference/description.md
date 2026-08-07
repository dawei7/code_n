### 1. Description

You are given an integer array `nums` with **distinct** elements.

A subarray `nums[l...r]` of `nums` is called a **bowl** if:

- The subarray has length at least 3. That is, $r - l + 1 \ge 3$.

- The **minimum** of its two ends is **strictly greater** than the **maximum** of all elements in between. That is, $min(\text{nums}[l], \text{nums}[r]) > max(nums[l + 1], ..., nums[r - 1])$.

Return the number of **bowl** subarrays in `nums`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,5,3,1,4]

**Output:** 2

**Explanation:**

The bowl subarrays are `[3, 1, 4]` and `[5, 3, 1, 4]`.

- `[3, 1, 4]` is a bowl because $min(3, 4) = 3 > max(1) = 1$.

- `[5, 3, 1, 4]` is a bowl because $min(5, 4) = 4 > max(3, 1) = 3$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [5,1,2,3,4]

**Output:** 3

**Explanation:**

The bowl subarrays are `[5, 1, 2]`, `[5, 1, 2, 3]` and `[5, 1, 2, 3, 4]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1000000000,999999999,999999998]

**Output:** 0

**Explanation:**

No subarray is a bowl.

</div>

### 4. Constraints

- $3 \le \text{nums.length} \le 10^{5}$

- $1 \le \text{nums}[i] \le 10^{9}$

- `nums` consists of distinct elements.