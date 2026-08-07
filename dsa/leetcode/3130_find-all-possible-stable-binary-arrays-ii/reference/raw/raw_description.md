## Description

You are given 3 positive integers `num_zeros`, `num_ones`, and `limit`.

A <span data-keyword="binary-array">binary array</span> `arr` is called **stable** if:

	- The number of occurrences of 0 in `arr` is **exactly **`num_zeros`.

	- The number of occurrences of 1 in `arr` is **exactly** `num_ones`.

	- Each <span data-keyword="subarray-nonempty">subarray</span> of `arr` with a size greater than `limit` must contain **at least** one occurrence of **both** 0 and 1.

Return an integer denoting the *total* number of **stable** binary arrays.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">zero = 1, one = 1, limit = 2</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The two possible stable binary arrays are `[1,0]` and `[0,1]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">zero = 1, one = 2, limit = 1</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The only possible stable binary array is `[1,0,1]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">zero = 3, one = 3, limit = 2</span>

**Output:** <span class="example-io">14</span>

**Explanation:**

All the possible stable binary arrays are `[0,0,1,0,1,1]`, `[0,0,1,1,0,1]`, `[0,1,0,0,1,1]`, `[0,1,0,1,0,1]`, `[0,1,0,1,1,0]`, `[0,1,1,0,0,1]`, `[0,1,1,0,1,0]`, `[1,0,0,1,0,1]`, `[1,0,0,1,1,0]`, `[1,0,1,0,0,1]`, `[1,0,1,0,1,0]`, `[1,0,1,1,0,0]`, `[1,1,0,0,1,0]`, and `[1,1,0,1,0,0]`.

</div>

**Constraints:**

	- `1 <= zero, one, limit <= 1000`
