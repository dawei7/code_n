## Description

You are given an integer array `nums` and an integer `k`. You can perform the following operation any number of times:

	- Select an index `i` and replace `nums[i]` with `nums[i] - 1`.

Return the **minimum** number of operations required to make the sum of the array divisible by `k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,9,7], k = 5</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- Perform 4 operations on `nums[1] = 9`. Now, `nums = [3, 5, 7]`.

	- The sum is 15, which is divisible by 5.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,1,3], k = 4</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- The sum is 8, which is already divisible by 4. Hence, no operations are needed.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,2], k = 6</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- Perform 3 operations on `nums[0] = 3` and 2 operations on `nums[1] = 2`. Now, `nums = [0, 0]`.

	- The sum is 0, which is divisible by 6.

</div>

**Constraints:**

	- `1 <= nums.length <= 1000`

	- `1 <= nums[i] <= 1000`

	- `1 <= k <= 100`
