## Description

You are given an integer array `nums`, and an integer `k`.

For any <span data-keyword="subarray-nonempty">subarray</span> `nums[l..r]`, define its **cost** as:

`cost = (max(nums[l..r]) - min(nums[l..r])) * (r - l + 1)`.

Return an integer denoting the number of subarrays of `nums` whose cost is **less than or equal** to `k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,2], k = 4</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

We consider all subarrays of `nums`:

	- `nums[0..0]`: `cost = (1 - 1) * 1 = 0`

	- `nums[0..1]`: `cost = (3 - 1) * 2 = 4`

	- `nums[0..2]`: `cost = (3 - 1) * 3 = 6`

	- `nums[1..1]`: `cost = (3 - 3) * 1 = 0`

	- `nums[1..2]`: `cost = (3 - 2) * 2 = 2`

	- `nums[2..2]`: `cost = (2 - 2) * 1 = 0`

There are 5 subarrays whose cost is less than or equal to 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,5,5,5], k = 0</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

For any subarray of `nums`, the maximum and minimum values are the same, so the cost is always 0.

As a result, every subarray of `nums` has cost less than or equal to 0.

For an array of length 4, the total number of subarrays is `(4 * 5) / 2 = 10`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], k = 0</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The only subarrays of `nums` with cost 0 are the single-element subarrays, and there are 3 of them.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `0 <= k <= 10^15`
