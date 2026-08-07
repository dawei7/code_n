## Description

You are given a positive integer array `sides` of length 3.

Determine if there exists a triangle with **positive** area whose three side lengths are given by the elements of `sides`.

If such a triangle exists, return an array of three floating-point numbers representing its internal angles (in **degrees**), **sorted** in **non-decreasing** order. Otherwise, return an empty array.

Answers within `10^-5` of the actual answer will be accepted.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">sides = [3,4,5]</span>

**Output:** <span class="example-io">[36.86990,53.13010,90.00000]</span>

**Explanation:**

You can form a right-angled triangle with side lengths 3, 4, and 5. The internal angles of this triangle are approximately 36.869897646, 53.130102354, and 90 degrees respectively.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">sides = [2,4,2]</span>

**Output:** <span class="example-io">[]</span>

**Explanation:**

You cannot form a triangle with positive area using side lengths 2, 4, and 2.

</div>

**Constraints:**

	- `sides.length == 3`

	- `1 <= sides[i] <= 1000`
