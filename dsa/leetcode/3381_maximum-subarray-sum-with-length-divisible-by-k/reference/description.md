### 1. Description

You are given an array of integers `nums` and an integer `k`.

Return the **maximum** sum of a subarray of `nums`, such that the size of the subarray is **divisible** by `k`.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2], k = 1

**Output:** 3

**Explanation:**

The subarray `[1, 2]` with sum 3 has length equal to 2 which is divisible by 1.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-1,-2,-3,-4,-5], k = 4

**Output:** -10

**Explanation:**

The maximum sum subarray is `[-1, -2, -3, -4]` which has length equal to 4 which is divisible by 4.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [-5,1,2,-3,4], k = 2

**Output:** 4

**Explanation:**

The maximum sum subarray is `[1, 2, -3, 4]` which has length equal to 4 which is divisible by 2.

</div>

### 4. Constraints

- $1 \le k \le \text{nums.length} \le 2 * 10^{5}$

- $-10^{9} \le \text{nums}[i] \le 10^{9}$