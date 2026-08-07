## Description

Given an array `nums` of `n` integers and an integer `k`, determine whether there exist **two** **adjacent** <span data-keyword="subarray-nonempty">subarrays</span> of length `k` such that both subarrays are **strictly** **increasing**. Specifically, check if there are **two** subarrays starting at indices `a` and `b` (`a < b`), where:

	- Both subarrays `nums[a..a + k - 1]` and `nums[b..b + k - 1]` are **strictly increasing**.

	- The subarrays must be **adjacent**, meaning `b = a + k`.

Return `true` if it is *possible* to find **two **such subarrays, and `false` otherwise.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,5,7,8,9,2,3,4,3,1], k = 3</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

	- The subarray starting at index `2` is `[7, 8, 9]`, which is strictly increasing.

	- The subarray starting at index `5` is `[2, 3, 4]`, which is also strictly increasing.

	- These two subarrays are adjacent, so the result is `true`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,4,4,4,5,6,7], k = 5</span>

**Output:** <span class="example-io">false</span>

</div>

**Constraints:**

	- `2 <= nums.length <= 100`

	- `1 < 2 * k <= nums.length`

	- `-1000 <= nums[i] <= 1000`
