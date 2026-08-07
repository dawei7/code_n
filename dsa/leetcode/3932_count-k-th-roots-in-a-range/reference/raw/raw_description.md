## Description

You are given three integers `l`, `r`, and `k`.

An integer `y` is said to be a **perfect k^th power** if there exists an integer `x` such that `y = x^k`.

Return the number of integers `y` in the range `[l, r]` (inclusive) that are **perfect k^th powers**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">l = 1, r = 9, k = 3</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The perfect cubes in the range `[1, 9]` are:

	- `1 = 1^3`

	- `8 = 2^3`

Hence, the answer is 2.</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">l = 8, r = 30, k = 2</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

The perfect squares in the range `[8, 30]` are:

	- `9 = 3^2`

	- `16 = 4^2`

	- `25 = 5^2`

Hence, the answer is 3.</div>

**Constraints:**

	- `0 <= l <= r <= 10^9`

	- `1 <= k <= 30`
