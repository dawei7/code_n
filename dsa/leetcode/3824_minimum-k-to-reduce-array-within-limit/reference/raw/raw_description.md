## Description

You are given a **positive** integer array `nums`.

For a positive integer `k`, define `nonPositive(nums, k)` as the **minimum** number of **operations** needed to make every element of `nums` **non-positive**. In one operation, you can choose an index `i` and reduce `nums[i]` by `k`.

Return an integer denoting the **minimum** value of `k` such that `nonPositive(nums, k) <= k^2`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,7,5]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

When `k = 3`, `nonPositive(nums, k) = 6 <= k^2`.

	- Reduce `nums[0] = 3` one time. `nums[0]` becomes `3 - 3 = 0`.

	- Reduce `nums[1] = 7` three times. `nums[1]` becomes `7 - 3 - 3 - 3 = -2`.

	- Reduce `nums[2] = 5` two times. `nums[2]` becomes `5 - 3 - 3 = -1`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

When `k = 1`, `nonPositive(nums, k) = 1 <= k^2`.

	- Reduce `nums[0] = 1` one time. `nums[0]` becomes `1 - 1 = 0`.

</div>

**Constraints:**

	- `1 <= nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`
