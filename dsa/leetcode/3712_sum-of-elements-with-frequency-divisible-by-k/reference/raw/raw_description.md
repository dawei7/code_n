## Description

You are given an integer array `nums` and an integer `k`.

Return an integer denoting the **sum** of all elements in `nums` whose **<span data-keyword="frequency-array">frequency</span>** is divisible by `k`, or 0 if there are no such elements.

**Note:** An element is included in the sum **exactly** as many times as it appears in the array if its total frequency is divisible by `k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,2,3,3,3,3,4], k = 2</span>

**Output:** <span class="example-io">16</span>

**Explanation:**

	- The number 1 appears once (odd frequency).

	- The number 2 appears twice (even frequency).

	- The number 3 appears four times (even frequency).

	- The number 4 appears once (odd frequency).

So, the total sum is `2 + 2 + 3 + 3 + 3 + 3 = 16`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5], k = 2</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There are no elements that appear an even number of times, so the total sum is 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,4,4,1,2,3], k = 3</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

	- The number 1 appears once.

	- The number 2 appears once.

	- The number 3 appears once.

	- The number 4 appears three times.

So, the total sum is `4 + 4 + 4 = 12`.

</div>

**Constraints:**

	- `1 <= nums.length <= 100`

	- `1 <= nums[i] <= 100`

	- `1 <= k <= 100`
