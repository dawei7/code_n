## Description

A **no-zero** integer is a **positive** integer that **does not contain the digit** 0 in its decimal representation.

Given an integer `n`, count the number of pairs `(a, b)` where:

	- `a` and `b` are **no-zero** integers.

	- `a + b = n`

Return an integer denoting the number of such pairs.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 2</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The only pair is `(1, 1)`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The pairs are `(1, 2)` and `(2, 1)`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 11</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

The pairs are `(2, 9)`, `(3, 8)`, `(4, 7)`, `(5, 6)`, `(6, 5)`, `(7, 4)`, `(8, 3)`, and `(9, 2)`. Note that `(1, 10)` and `(10, 1)` do not satisfy the conditions because 10 contains 0 in its decimal representation.

</div>

**Constraints:**

	- `2 <= n <= 10^15`
