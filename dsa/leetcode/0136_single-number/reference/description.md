### 1. Description

Given a **non-empty** array of integers `nums`, every element appears *twice* except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

### 2. Function Contract

**Inputs**

- `nums`: A non-empty integer array satisfying the pairs-plus-one frequency guarantee.

**Return value**

Return the unique element that occurs exactly once.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [2,2,1]

**Output:** 1

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [4,1,2,1,2]

**Output:** 4

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1]

**Output:** 1

</div>

### 4. Constraints

- $1 \le \text{nums.length} \le 3 * 10^{4}$

- $-3 * 10^{4} \le \text{nums}[i] \le 3 * 10^{4}$

- Each element in the array appears twice except for one element which appears only once.