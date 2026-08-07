## Description

You are given two integers `n` and `x`. You have to construct an array of **positive** integers `nums` of size `n` where for every `0 <= i < n - 1`, `nums[i + 1]` is **greater than** `nums[i]`, and the result of the bitwise `AND` operation between all elements of `nums` is `x`.

Return the **minimum** possible value of `nums[n - 1]`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, x = 4</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

`nums` can be `[4,5,6]` and its last element is 6.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 2, x = 7</span>

**Output:** <span class="example-io">15</span>

**Explanation:**

`nums` can be `[7,15]` and its last element is 15.

</div>

**Constraints:**

	- `1 <= n, x <= 10^8`
