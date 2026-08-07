## Description

You are given an integer array `nums` of length `n` and an integer `k`.

An index `i` is a **peak** if:

	- `0 < i < n - 1`

	- `nums[i] > nums[i - 1]` and `nums[i] > nums[i + 1]`

A subarray `[l, r]` is **valid** if:

	- It contains **exactly one** peak at index `i` from `nums`

	- `i - l <= k` and `r - i <= k`

Return an integer denoting the number of **valid subarrays** in `nums`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,3,2], k = 1</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

	- Index `i = 1` is a peak because `nums[1] = 3` is greater than `nums[0] = 1` and `nums[2] = 2`.

	- Any valid subarray must include index 1, and the distance from the peak to both ends of the subarray must not exceed `k = 1`.

	- The valid subarrays are `[3]`, `[1, 3]`, `[3, 2]`, and `[1, 3, 2]`, so the answer is 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [7,8,9], k = 2</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

	- There is no index `i` such that `nums[i]` is greater than both `nums[i - 1]` and `nums[i + 1]`.

	- Therefore, the array contains no peak. Thus, the number of valid subarrays is 0.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,3,5,1], k = 2</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

	- Index `i = 2` is a peak because `nums[2] = 5` is greater than `nums[1] = 3` and `nums[3] = 1`.

	- Any valid subarray must contain this peak, and the distance from the peak to both ends of the subarray must not exceed `k = 2`.

	- The valid subarrays are `[5]`, `[3, 5]`, `[5, 1]`, `[3, 5, 1]`, `[4, 3, 5]`, and `[4, 3, 5, 1]`, so the answer is 6.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `-10^5 <= nums[i] <= 10^5`

	- `1 <= k <= n`
