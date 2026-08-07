## Description

Given an array `nums` of `n` integers, your task is to find the **maximum** value of `k` for which there exist **two** adjacent <span data-keyword="subarray-nonempty">subarrays</span> of length `k` each, such that both subarrays are **strictly** **increasing**. Specifically, check if there are **two** subarrays of length `k` starting at indices `a` and `b` (`a < b`), where:

	- Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly increasing**.

	- The subarrays must be **adjacent**, meaning `b = a + k`.

Return the **maximum** *possible* value of `k`.

A **subarray** is a contiguous **non-empty** sequence of elements within an array.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,5,7,8,9,2,3,4,3,1]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- The subarray starting at index 2 is `[7, 8, 9]`, which is strictly increasing.

	- The subarray starting at index 5 is `[2, 3, 4]`, which is also strictly increasing.

	- These two subarrays are adjacent, and 3 is the **maximum** possible value of `k` for which two such adjacent strictly increasing subarrays exist.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,4,4,4,5,6,7]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- The subarray starting at index 0 is `[1, 2]`, which is strictly increasing.

	- The subarray starting at index 2 is `[3, 4]`, which is also strictly increasing.

	- These two subarrays are adjacent, and 2 is the **maximum** possible value of `k` for which two such adjacent strictly increasing subarrays exist.

</div>

**Constraints:**

	- `2 <= nums.length <= 2 * 10^5`

	- `-10^9 <= nums[i] <= 10^9`
