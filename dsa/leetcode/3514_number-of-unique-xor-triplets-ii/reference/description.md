## Description

You are given an integer array `nums`.

A **XOR triplet** is defined as the XOR of three elements $\text{nums}[i] XOR \text{nums}[j] XOR \text{nums}[k]$ where $i \le j \le k$.

Return the number of **unique** XOR triplet values from all possible triplets `(i, j, k)`.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [1,3]

**Output:** 2

**Explanation:**

The possible XOR triplet values are:

- $(0, 0, 0) → 1 XOR 1 XOR 1 = 1$

- $(0, 0, 1) → 1 XOR 1 XOR 3 = 3$

- $(0, 1, 1) → 1 XOR 3 XOR 3 = 1$

- $(1, 1, 1) → 3 XOR 3 XOR 3 = 3$

The unique XOR values are `{1, 3}`. Thus, the output is 2.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [6,7,8,9]

**Output:** 4

**Explanation:**

The possible XOR triplet values are `{6, 7, 8, 9}`. Thus, the output is 4.

</div>
### Constraints

- $1 \le \text{nums.length} \le 1500$

- $1 \le \text{nums}[i] \le 1500$