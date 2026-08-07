## Description

You are given three integers `n`, `l`, and `r`.

A **ZigZag** array of length `n` is defined as follows:

	- Each element lies in the range `[l, r]`.

	- No **two** adjacent elements are equal.

	- No **three** consecutive elements form a **strictly increasing** or **strictly decreasing** sequence.

Return the total number of valid **ZigZag** arrays.

Since the answer may be large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, l = 4, r = 5</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

There are only 2 valid ZigZag arrays of length `n = 3` using values in the range `[4, 5]`:

	- `[4, 5, 4]`

	- `[5, 4, 5]`

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, l = 1, r = 3</span>

**Output:** <span class="example-io">10</span>

**Explanation:**

There are 10 valid ZigZag arrays of length `n = 3` using values in the range `[1, 3]`:

	- `[1, 2, 1]`, `[1, 3, 1]`, `[1, 3, 2]`

	- `[2, 1, 2]`, `[2, 1, 3]`, `[2, 3, 1]`, `[2, 3, 2]`

	- `[3, 1, 2]`, `[3, 1, 3]`, `[3, 2, 3]`

All arrays meet the ZigZag conditions.

</div>

**Constraints:**

	- `3 <= n <= 200`

	- `1 <= l < r <= 10^​​​​​​​9`
