## Description

You are given a **1****-indexed** array `nums`. Your task is to select a **complete subset** from `nums` where every pair of selected indices multiplied is a <span data-keyword="perfect-square">perfect square,</span>. i. e. if you select `a_i` and `a_j`, `i * j` must be a perfect square.

Return the *sum* of the complete subset with the *maximum sum*.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [8,7,3,5,7,2,4,9]</span>

**Output:** <span class="example-io">16</span>

**Explanation:**

We select elements at indices 2 and 8 and `2 * 8` is a perfect square.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [8,10,3,8,1,13,7,9,4]</span>

**Output:** <span class="example-io">20</span>

**Explanation:**

We select elements at indices 1, 4, and 9. `1 * 4`, `1 * 9`, `4 * 9` are perfect squares.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^4`

	- `1 <= nums[i] <= 10^9`
