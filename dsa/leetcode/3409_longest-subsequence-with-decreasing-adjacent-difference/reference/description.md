## Description

You are given an array of integers `nums`.

Your task is to find the length of the **longest** subsequence `seq` of `nums`, such that the **absolute differences** between* consecutive* elements form a **non-increasing sequence** of integers. In other words, for a subsequence $\text{seq}_{0}$, $\text{seq}_{1}$, $\text{seq}_{2}$, ..., $\text{seq}_{m}$ of `nums`, $|\text{seq}_{1} - \text{seq}_{0}| \ge |\text{seq}_{2} - \text{seq}_{1}| \ge ... \ge |\text{seq}_{m} - \text{seq}_{m} - 1|$.

Return the length of such a subsequence.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [16,6,3]

**Output:** 3

**Explanation:**

The longest subsequence is `[16, 6, 3]` with the absolute adjacent differences `[10, 3]`.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [6,5,3,4,2,1]

**Output:** 4

**Explanation:**

The longest subsequence is `[6, 4, 2, 1]` with the absolute adjacent differences `[2, 2, 1]`.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [10,20,10,19,10,20]

**Output:** 5

**Explanation:**

The longest subsequence is `[10, 20, 10, 19, 10]` with the absolute adjacent differences `[10, 10, 9, 9]`.

</div>
### Constraints

- $2 \le \text{nums.length} \le 10^{4}$

- $1 \le \text{nums}[i] \le 300$