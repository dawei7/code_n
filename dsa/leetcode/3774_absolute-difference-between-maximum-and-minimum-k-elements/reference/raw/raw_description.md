## Description

You are given an integer array `nums` and an integer `k`.

Find the absolute difference between:

	- the **sum** of the `k` **largest** elements in the array; and

	- the **sum** of the `k` **smallest** elements in the array.

Return an integer denoting this difference.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,2,2,4], k = 2</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- The `k = 2` largest elements are 4 and 5. Their sum is `4 + 5 = 9`.

	- The `k = 2` smallest elements are 2 and 2. Their sum is `2 + 2 = 4`.

	- The absolute difference is `abs(9 - 4) = 5`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [100], k = 1</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- The largest element is 100.

	- The smallest element is 100.

	- The absolute difference is `abs(100 - 100) = 0`.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 100`

	- `1 <= nums[i] <= 100`

	- `1 <= k <= n`
