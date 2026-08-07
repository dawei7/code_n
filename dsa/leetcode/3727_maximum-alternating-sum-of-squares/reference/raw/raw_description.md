## Description

You are given an integer array `nums`. You may **rearrange the elements** in any order.

The **alternating score** of an array `arr` is defined as:

	- `score = arr[0]^2 - arr[1]^2 + arr[2]^2 - arr[3]^2 + ...`

Return an integer denoting the **maximum possible alternating score** of `nums` after rearranging its elements.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3]</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

A possible rearrangement for `nums` is `[2,1,3]`, which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

`score = 2^2 - 1^2 + 3^2 = 4 - 1 + 9 = 12`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,-1,2,-2,3,-3]</span>

**Output:** <span class="example-io">16</span>

**Explanation:**

A possible rearrangement for `nums` is `[-3,-1,-2,1,3,2]`, which gives the maximum alternating score among all possible rearrangements.

The alternating score is calculated as:

`score = (-3)^2 - (-1)^2 + (-2)^2 - (1)^2 + (3)^2 - (2)^2 = 9 - 1 + 4 - 1 + 9 - 4 = 16`

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `-4 * 10^4 <= nums[i] <= 4 * 10^4`
