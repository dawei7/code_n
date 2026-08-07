### 1. Description

You are given an integer array `nums`. In one operation, you can add or subtract 1 from **any** element of `nums`.

Return the **minimum** number of operations to make all elements of `nums` divisible by 3.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,2,3,4]

**Output:** 3

**Explanation:**

All array elements can be made divisible by 3 using 3 operations:

- Subtract 1 from 1.

- Add 1 to 2.

- Subtract 1 from 4.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [3,6,9]

**Output:** 0

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 50$

- $1 \le \text{nums}[i] \le 50$