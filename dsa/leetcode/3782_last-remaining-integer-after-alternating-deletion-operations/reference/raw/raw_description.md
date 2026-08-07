## Description

You are given an integer `n`.

We write the integers from 1 to `n` in a sequence from left to right. Then, **alternately** apply the following two operations until only one integer remains, starting with operation 1:

	- **Operation 1**: Starting from the left, delete every second number.

	- **Operation 2**: Starting from the right, delete every second number.

Return the last remaining integer.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 8</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

	- Write `[1, 2, 3, 4, 5, 6, 7, 8]` in a sequence.

	- Starting from the left, we delete every second number: `[1, <u>**2**</u>, 3, <u>**4**</u>, 5, <u>**6**</u>, 7, <u>**8**</u>]`. The remaining integers are `[1, 3, 5, 7]`.

	- Starting from the right, we delete every second number: `[<u>**1**</u>, 3, <u>**5**</u>, 7]`. The remaining integers are `[3, 7]`.

	- Starting from the left, we delete every second number: `[3, <u>**7**</u>]`. The remaining integer is `[3]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 5</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- Write `[1, 2, 3, 4, 5]` in a sequence.

	- Starting from the left, we delete every second number: `[1, <u>**2**</u>, 3, <u>**4**</u>, 5]`. The remaining integers are `[1, 3, 5]`.

	- Starting from the right, we delete every second number: `[1, <u>**3**</u>, 5]`. The remaining integers are `[1, 5]`.

	- Starting from the left, we delete every second number: `[1, <u>**5**</u>]`. The remaining integer is `[1]`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 1</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- Write `[1]` in a sequence.

	- The last remaining integer is 1.

</div>

**Constraints:**

	- `1 <= n <= 10^15`
