### 1. Description

You are given an integer array `nums`. Each element in `nums` is 1, 2 or 3. In each operation, you can remove an element from `nums`. Return the **minimum** number of operations to make `nums` **non-decreasing**.

### 2. Function Contract

- `n`: Input parameter.
- Returns expected result.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,1,3,2,1]

**Output:** 3

**Explanation:**

One of the optimal solutions is to remove $\text{nums}[0]$, $\text{nums}[2]$ and $\text{nums}[3]$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [1,3,2,1,3,3]

**Output:** 2

**Explanation:**

One of the optimal solutions is to remove $\text{nums}[1]$ and $\text{nums}[2]$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [2,2,2,2,3,3]

**Output:** 0

**Explanation:**

`nums` is already non-decreasing.

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 100$

- $1 \le \text{nums}[i] \le 3$

### 5. Follow-up

Can you come up with an algorithm that runs in `O(n)` time complexity?