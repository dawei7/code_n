## Description

You are given an array `nums` of length `n`. You are also given an integer `k`.

You perform the following operation on `nums` **once**:

	- Select a <span data-keyword="subarray-nonempty">subarray</span> `nums[i..j]` where `0 <= i <= j <= n - 1`.

	- Select an integer `x` and add `x` to **all** the elements in `nums[i..j]`.

Find the **maximum** frequency of the value `k` after the operation.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3,4,5,6], k = 1</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

After adding -5 to `nums[2..5]`, 1 has a frequency of 2 in `[1, 2, -2, -1, 0, 1]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [10,2,3,4,5,5,4,3,2,2], k = 10</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

After adding 8 to `nums[1..9]`, 10 has a frequency of 4 in `[10, 10, 11, 12, 13, 13, 12, 11, 10, 10]`.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 50`

	- `1 <= k <= 50`
