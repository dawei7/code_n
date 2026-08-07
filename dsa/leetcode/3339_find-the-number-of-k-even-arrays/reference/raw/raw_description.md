## Description

You are given three integers `n`, `m`, and `k`.

An array `arr` is called **k-even** if there are **exactly** `k` indices such that, for each of these indices `i` (`0 <= i < n - 1`):

	- `(arr[i] * arr[i + 1]) - arr[i] - arr[i + 1]` is *even*.

Return the number of possible **k-even** arrays of size `n` where all elements are in the range `[1, m]`.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, m = 4, k = 2</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

The 8 possible 2-even arrays are:

	- `[2, 2, 2]`

	- `[2, 2, 4]`

	- `[2, 4, 2]`

	- `[2, 4, 4]`

	- `[4, 2, 2]`

	- `[4, 2, 4]`

	- `[4, 4, 2]`

	- `[4, 4, 4]`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, m = 1, k = 0</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The only 0-even array is `[1, 1, 1, 1, 1]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 7, m = 7, k = 5</span>

**Output:** <span class="example-io">5832</span>

</div>

**Constraints:**

	- `1 <= n <= 750`

	- `0 <= k <= n - 1`

	- `1 <= m <= 1000`
