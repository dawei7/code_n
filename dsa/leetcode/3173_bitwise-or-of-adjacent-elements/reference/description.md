### 1. Description

Given an array `nums` of length `n`, return an array `answer` of length $n - 1$ such that $\text{answer}[i] = \text{nums}[i] | nums[i + 1]$ where `|` is the bitwise `OR` operation.

### 2. Function Contract

- Refer to method signature.

### 3. Examples

#### Example 1

<div class="example-block">
**Input:** nums = [1,3,7,15]

**Output:** [3,7,15]

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [8,4,2]

**Output:** [12,6]

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [5,4,9,11]

**Output:** [5,13,11]

</div>

### 4. Constraints

- $2 \le \text{nums.length} \le 100$

- $0 \le \text{nums}[i] \le 100$