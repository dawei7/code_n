## Description

You are given an integer array `rewardValues` of length `n`, representing the values of rewards.

Initially, your total reward `x` is 0, and all indices are **unmarked**. You are allowed to perform the following operation **any** number of times:

- Choose an **unmarked** index `i` from the range `[0, n - 1]`.

- If $\text{rewardValues}[i]$ is **greater** than your current total reward `x`, then add $\text{rewardValues}[i]$ to `x` (i.e., $x = x + \text{rewardValues}[i]$), and **mark** the index `i`.

Return an integer denoting the **maximum ***total reward* you can collect by performing the operations optimally.
### Function Contract

- `n`: Input parameter.
- Returns expected result.

### Examples
#### Example 1

<div class="example-block">
**Input:** rewardValues = [1,1,3,3]

**Output:** 4

**Explanation:**

During the operations, we can choose to mark the indices 0 and 2 in order, and the total reward will be 4, which is the maximum.

</div>
#### Example 2

<div class="example-block">
**Input:** rewardValues = [1,6,4,3,2]

**Output:** 11

**Explanation:**

Mark the indices 0, 2, and 1 in order. The total reward will then be 11, which is the maximum.

</div>
### Constraints

- $1 \le \text{rewardValues.length} \le 2000$

- $1 \le \text{rewardValues}[i] \le 2000$