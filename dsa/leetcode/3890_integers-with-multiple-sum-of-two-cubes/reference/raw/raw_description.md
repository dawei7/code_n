## Description

You are given an integer `n`.

An integer `x` is considered **good** if there exist **at least** two **distinct** pairs `(a, b)` such that:

	- `a` and `b` are positive integers.

	- `a <= b`

	- `x = a^3 + b^3`

Return an array containing all good integers **less than or equal to** `n`, sorted in ascending order.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4104</span>

**Output:** <span class="example-io">[1729,4104]</span>

**Explanation:**

Among integers less than or equal to 4104, the good integers are:

	- 1729: `1^3 + 12^3 = 1729` and `9^3 + 10^3 = 1729`.

	- 4104: `2^3 + 16^3 = 4104` and `9^3 + 15^3 = 4104`.

Thus, the answer is `[1729, 4104]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 578</span>

**Output:** <span class="example-io">[]</span>

**Explanation:**

There are no good integers less than or equal to 578, so the answer is an empty array.

</div>

**Constraints:**

	- `1 <= n <= 10^9`
