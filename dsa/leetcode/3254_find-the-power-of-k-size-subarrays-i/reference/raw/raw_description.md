## Description

You are given an array of integers `nums` of length `n` and a *positive* integer `k`.

The **power** of an array is defined as:

	- Its **maximum** element if *all* of its elements are **consecutive** and **sorted** in **ascending** order.

	- -1 otherwise.

You need to find the **power** of all <span data-keyword="subarray-nonempty">subarrays</span> of `nums` of size `k`.

Return an integer array `results` of size `n - k + 1`, where `results[i]` is the *power* of `nums[i..(i + k - 1)]`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,3,2,5], k = 3</span>

**Output:** [3,4,-1,-1,-1]

**Explanation:**

There are 5 subarrays of `nums` of size 3:

	- `[1, 2, 3]` with the maximum element 3.

	- `[2, 3, 4]` with the maximum element 4.

	- `[3, 4, 3]` whose elements are **not** consecutive.

	- `[4, 3, 2]` whose elements are **not** sorted.

	- `[3, 2, 5]` whose elements are **not** consecutive.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,2,2,2,2], k = 4</span>

**Output:** <span class="example-io">[-1,-1]</span>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,2,3,2,3,2], k = 2</span>

**Output:** <span class="example-io">[-1,3,-1,3,-1]</span>

</div>

**Constraints:**

	- `1 <= n == nums.length <= 500`

	- `1 <= nums[i] <= 10^5`

	- `1 <= k <= n`
