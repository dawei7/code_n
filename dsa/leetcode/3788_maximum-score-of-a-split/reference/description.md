## Description

You are given an integer array `nums` of length `n`.

Choose an index `i` such that $0 \le i < n - 1$.

For a chosen split index `i`:

- Let `prefixSum(i)` be the sum of $\text{nums}[0] + \text{nums}[1] + ... + \text{nums}[i]$.

- Let `suffixMin(i)` be the minimum value among $nums[i + 1], nums[i + 2], ..., nums[n - 1]$.

The **score** of a split at index `i` is defined as:

$score(i) = prefixSum(i) - suffixMin(i)$

Return an integer denoting the **maximum** score over all valid split indices.
### Function Contract

**Inputs**

- `nums`: An integer array containing at least two elements.

A valid split includes index `i` in the prefix and starts the suffix at `i + 1`. The suffix minimum is a value, not a sum. Scores and the maximum score may be negative.

**Return value**

Return the maximum of `sum(nums[0:i+1]) - min(nums[i+1:n])` over every `0 <= i < n - 1`.

### Examples
#### Example 1

<div class="example-block">
**Input:** nums = [10,-1,3,-4,-5]

**Output:** 17

**Explanation:**

The optimal split is at $i = 2$, $score(2) = prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17$.

</div>
#### Example 2

<div class="example-block">
**Input:** nums = [-7,-5,3]

**Output:** -2

**Explanation:**

The optimal split is at $i = 0$, $score(0) = prefixSum(0) - suffixMin(0) = (-7) - (-5) = -2$.

</div>
#### Example 3

<div class="example-block">
**Input:** nums = [1,1]

**Output:** 0

**Explanation:**

The only valid split is at $i = 0$, $score(0) = prefixSum(0) - suffixMin(0) = 1 - 1 = 0$.

</div>
### Constraints

- $2 \le \text{nums.length} \le 10^{5}$

- $-10^{9}​​​​​​​ \le \text{nums}[i] \le 10^{9}$