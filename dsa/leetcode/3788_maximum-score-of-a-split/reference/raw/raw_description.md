## Description

You are given an integer array `nums` of length `n`.

Choose an index `i` such that `0 <= i < n - 1`.

For a chosen split index `i`:

	- Let `prefixSum(i)` be the sum of `nums[0] + nums[1] + ... + nums[i]`.

	- Let `suffixMin(i)` be the minimum value among `nums[i + 1], nums[i + 2], ..., nums[n - 1]`.

The **score** of a split at index `i` is defined as:

`score(i) = prefixSum(i) - suffixMin(i)`

Return an integer denoting the **maximum** score over all valid split indices.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [10,-1,3,-4,-5]</span>

**Output:** <span class="example-io">17</span>

**Explanation:**

The optimal split is at `i = 2`, `score(2) = prefixSum(2) - suffixMin(2) = (10 + (-1) + 3) - (-5) = 17`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [-7,-5,3]</span>

**Output:** <span class="example-io">-2</span>

**Explanation:**

The optimal split is at `i = 0`, `score(0) = prefixSum(0) - suffixMin(0) = (-7) - (-5) = -2`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,1]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The only valid split is at `i = 0`, `score(0) = prefixSum(0) - suffixMin(0) = 1 - 1 = 0`.

</div>

**Constraints:**

	- `2 <= nums.length <= 10^5`

	- `-10^9​​​​​​​ <= nums[i] <= 10^9`
