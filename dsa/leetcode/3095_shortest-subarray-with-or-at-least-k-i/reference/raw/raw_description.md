## Description

You are given an array `nums` of **non-negative** integers and an integer `k`.

An array is called **special** if the bitwise `OR` of all of its elements is **at least** `k`.

Return *the length of the **shortest** **special** **non-empty** <span data-keyword="subarray-nonempty">subarray</span> of* `nums`, *or return* `-1` *if no special subarray exists*.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2,3], k = 2</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The subarray `[3]` has `OR` value of `3`. Hence, we return `1`.

Note that `[2]` is also a special subarray.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,1,8], k = 10</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The subarray `[2,1,8]` has `OR` value of `11`. Hence, we return `3`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [1,2], k = 0</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The subarray `[1]` has `OR` value of `1`. Hence, we return `1`.

</div>

**Constraints:**

	- `1 <= nums.length <= 50`

	- `0 <= nums[i] <= 50`

	- `0 <= k < 64`
