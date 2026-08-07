## Description

You are given an integer array `nums` and an integer digit `x`.

A <span data-keyword="subarray-nonempty">**subarray**</span> `nums[l..r]` is considered **valid** if the sum of its elements satisfies both of the following conditions:

	- The first digit of the sum is equal to `x`.

	- The last digit of the sum is equal to `x`.

Return the number of valid subarrays.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,100,1], x = 1</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

The valid subarrays are:

	- `nums[0..0]`: `sum = 1`

	- `nums[0..1]`: `sum = 1 + 100 = 101`

	- `nums[1..2]`: `sum = 100 + 1 = 101`

	- `nums[2..2]`: `sum = 1`

Thus, the answer is 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1], x = 2</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

The only subarray is `nums[0..0]` with a sum of 1, which does not satisfy the conditions.

Thus, the answer is 0.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^9`

	- `1 <= x <= 9`
