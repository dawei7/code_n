## Description

You are given an integer array `nums` and two integers `k` and `numOperations`.

You must perform an **operation** `numOperations` times on `nums`, where in each operation you:

	- Select an index `i` that was **not** selected in any previous operations.

	- Add an integer in the range `[-k, k]` to `nums[i]`.

Return the **maximum** possible <span data-keyword="frequency-array">frequency</span> of any element in `nums` after performing the **operations**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,4,5], k = 1, numOperations = 2</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

We can achieve a maximum frequency of two by:

	- Adding 0 to `nums[1]`, after which `nums` becomes `[1, 4, 5]`.

	- Adding -1 to `nums[2]`, after which `nums` becomes `[1, 4, 4]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,11,20,20], k = 5, numOperations = 1</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

We can achieve a maximum frequency of two by:

	- Adding 0 to `nums[1]`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `0 <= k <= 10^9`

	- `0 <= numOperations <= nums.length`
