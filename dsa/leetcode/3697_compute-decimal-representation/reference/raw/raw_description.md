## Description

You are given a **positive** integer `n`.

A positive integer is a **base-10 component** if it is the product of a single digit from 1 to 9 and a non-negative power of 10. For example, 500, 30, and 7 are **base-10 components**, while 537, 102, and 11 are not.

Express `n` as a sum of **only** base-10 components, using the **fewest** base-10 components possible.

Return an array containing these **base-10 components** in **descending** order.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 537</span>

**Output:** <span class="example-io">[500,30,7]</span>

**Explanation:**

We can express 537 as `500 + 30 + 7`. It is impossible to express 537 as a sum using fewer than 3 base-10 components.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 102</span>

**Output:** <span class="example-io">[100,2]</span>

**Explanation:**

We can express 102 as `100 + 2`. 102 is not a base-10 component, which means 2 base-10 components are needed.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 6</span>

**Output:** <span class="example-io">[6]</span>

**Explanation:**

6 is a base-10 component.

</div>

**Constraints:**

	- `1 <= n <= 10^9`
