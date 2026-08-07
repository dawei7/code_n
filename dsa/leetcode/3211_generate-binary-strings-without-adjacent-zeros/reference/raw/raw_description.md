## Description

You are given a positive integer `n`.

A binary string `x` is **valid** if all <span data-keyword="substring-nonempty">substrings</span> of `x` of length 2 contain **at least** one `"1"`.

Return all **valid** strings with length `n`**, **in *any* order.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3</span>

**Output:** <span class="example-io">["010","011","101","110","111"]</span>

**Explanation:**

The valid strings of length 3 are: `"010"`, `"011"`, `"101"`, `"110"`, and `"111"`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 1</span>

**Output:** <span class="example-io">["0","1"]</span>

**Explanation:**

The valid strings of length 1 are: `"0"` and `"1"`.

</div>

**Constraints:**

	- `1 <= n <= 18`
