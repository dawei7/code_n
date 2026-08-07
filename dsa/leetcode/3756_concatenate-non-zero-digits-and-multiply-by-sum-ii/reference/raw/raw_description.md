## Description

You are given a string `s` of length `m` consisting of digits. You are also given a 2D integer array `queries`, where `queries[i] = [l_i, r_i]`.

For each `queries[i]`, extract the **<span data-keyword="substring-nonempty">substring</span>** `s[l_i..r_i]`. Then, perform the following:

	- Form a new integer `x` by concatenating all the **non-zero digits** from the substring in their original order. If there are no non-zero digits, `x = 0`.

	- Let `sum` be the **sum of digits** in `x`. The answer is `x * sum`.

Return an array of integers `answer` where `answer[i]` is the answer to the `i^th` query.

Since the answers may be very large, return them **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">s = "10203004", queries = [[0,7],[1,3],[4,6]]</span>

**Output:** <span class="example-io">[12340, 4, 9]</span>

**Explanation:**

	- `s[0..7] = "10203004"`

		<li>`x = 1234`

		- `sum = 1 + 2 + 3 + 4 = 10`

		- Therefore, answer is `1234 * 10 = 12340`.

	</li>
	- `s[1..3] = "020"`

		<li>`x = 2`

		- `sum = 2`

		- Therefore, the answer is `2 * 2 = 4`.

	</li>
	- `s[4..6] = "300"`

		<li>`x = 3`

		- `sum = 3`

		- Therefore, the answer is `3 * 3 = 9`.

	</li>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">s = "1000", queries = [[0,3],[1,1]]</span>

**Output:** <span class="example-io">[1, 0]</span>

**Explanation:**

	- `s[0..3] = "1000"`

		<li>`x = 1`

		- `sum = 1`

		- Therefore, the answer is `1 * 1 = 1`.

	</li>
	- `s[1..1] = "0"`

		<li>`x = 0`

		- `sum = 0`

		- Therefore, the answer is `0 * 0 = 0`.

	</li>

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">s = "9876543210", queries = [[0,9]]</span>

**Output:** <span class="example-io">[444444137]</span>

**Explanation:**

	- `s[0..9] = "9876543210"`

		<li>`x = 987654321`

		- `sum = 9 + 8 + 7 + 6 + 5 + 4 + 3 + 2 + 1 = 45`

		- Therefore, the answer is `987654321 * 45 = 44444444445`.

		- We return `44444444445 modulo (10^9 + 7) = 444444137`.

	</li>

</div>

**Constraints:**

	- `1 <= m == s.length <= 10^5`

	- `s` consists of digits only.

	- `1 <= queries.length <= 10^5`

	- `queries[i] = [l_i, r_i]`

	- `0 <= l_i <= r_i < m`
