### 1. Description

Given an integer array `nums`, return the number of subarrays of length 3 such that the sum of the first and third numbers equals *exactly* half of the second number.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,1,4,1]

**Output:** 1

**Explanation:**

Only the subarray `[1,4,1]` contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,1,1]

**Output:** 0

**Explanation:**

`[1,1,1]` is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.

</div>

### 4. Constraints

- $3 \le \text{nums.length} \le 100$

- $-100 \le \text{nums}[i] \le 100$