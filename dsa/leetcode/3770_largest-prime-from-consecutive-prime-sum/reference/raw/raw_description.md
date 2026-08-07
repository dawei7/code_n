## Description

You are given an integer `n`.

Return the **largest <span data-keyword="prime-number">prime number</span>** less than or equal to `n` that can be expressed as the **sum** of one or more **consecutive prime numbers** starting from 2. If no such number exists, return 0.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 20</span>

**Output:** <span class="example-io">17</span>

**Explanation:**

The prime numbers less than or equal to `n = 20` which are consecutive prime sums are:

	- `2 = 2`

	- `5 = 2 + 3`

	- `17 = 2 + 3 + 5 + 7`

The largest is 17, so it is the answer.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 2</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The only consecutive prime sum less than or equal to 2 is 2 itself.

</div>

**Constraints:**

	- `1 <= n <= 5 * 10^5`
