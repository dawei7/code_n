## Description

You are given an integer array `nums` of length `n` and an integer `k`.

An element in `nums` is said to be **qualified** if there exist **at least** `k` elements in the array that are **strictly greater** than it.

Return an integer denoting the total number of qualified elements in `nums`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,1,2], k = 1</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The elements 1 and 2 each have at least `k = 1` element greater than themselves.

​​​​​​​No element is greater than 3. Therefore, the answer is 2.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,5,5], k = 2</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

Since all elements are equal to 5, no element is greater than the other. Therefore, the answer is 0.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `0 <= k < n`
