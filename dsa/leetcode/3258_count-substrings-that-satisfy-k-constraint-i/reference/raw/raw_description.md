## Description

You are given a **binary** string `s` and an integer `k`.

A **binary string** satisfies the **k-constraint** if **either** of the following conditions holds:

	- The number of `0`'s in the string is at most `k`.

	- The number of `1`'s in the string is at most `k`.

Return an integer denoting the number of <span data-keyword="substring-nonempty">substrings</span> of `s` that satisfy the **k-constraint**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "10101", k = 1</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

Every substring of `s` except the substrings `"1010"`, `"10101"`, and `"0101"` satisfies the k-constraint.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "1010101", k = 2</span>

**Output:** <span class="example-io">25</span>

**Explanation:**

Every substring of `s` except the substrings with a length greater than 5 satisfies the k-constraint.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "11111", k = 1</span>

**Output:** <span class="example-io">15</span>

**Explanation:**

All substrings of `s` satisfy the k-constraint.

</div>

**Constraints:**

	- `1 <= s.length <= 50 `

	- `1 <= k <= s.length`

	- `s[i]` is either `'0'` or `'1'`.
