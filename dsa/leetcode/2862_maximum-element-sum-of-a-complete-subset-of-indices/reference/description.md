## Description

You are given a **1****-indexed** array `nums`. Your task is to select a **complete subset** from `nums` where every pair of selected indices multiplied is a perfect square,. i. e. if you select $a_{i}$ and $a_{j}$, $i * j$ must be a perfect square.

Return the *sum* of the complete subset with the *maximum sum*.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [8,7,3,5,7,2,4,9]

**Output:** 16

**Explanation:**

We select elements at indices 2 and 8 and $2 * 8$ is a perfect square.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [8,10,3,8,1,13,7,9,4]

**Output:** 20

**Explanation:**

We select elements at indices 1, 4, and 9. $1 * 4$, $1 * 9$, $4 * 9$ are perfect squares.

</div>
### Constraints

- $1 \le n = \text{nums.length} \le 10^{4}$

- $1 \le \text{nums}[i] \le 10^{9}$