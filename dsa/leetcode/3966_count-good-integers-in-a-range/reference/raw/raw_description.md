## Description

You are given three integers `l`, `r` and `k`.

A number is considered **good** if the **absolute difference** between every pair of **adjacent** digits is **at most** `k`.

Return the number of **good** integers in the range `[l, r]` (inclusive).

The **absolute difference** between values `x` and `y` is defined as `abs(x - y)`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">l = 10, r = 15, k = 1</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- The good integers in the range are 10, 11, and 12.

	- For 10, `abs(1 - 0) = 1`.

	- For 11, `abs(1 - 1) = 0`.

	- For 12, `abs(1 - 2) = 1`.

	- All these differences are at most `k = 1`. Thus, the answer is 3.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">l = 201, r = 204, k = 2</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- The good integers in the range are 201 and 202.

	- For 201, `abs(2 - 0) = 2` and `abs(0 - 1) = 1`.

	- For 202, `abs(2 - 0) = 2` and `abs(0 - 2) = 2`.

	- Thus, the answer is 2.

</div>

**Constraints:**

	- `10 <= l <= r <= 10^15`

	- `0 <= k <= 9`
