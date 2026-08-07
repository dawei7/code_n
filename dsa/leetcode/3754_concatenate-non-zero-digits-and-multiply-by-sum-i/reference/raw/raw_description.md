## Description

You are given an integer `n`.

Form a new integer `x` by concatenating all the **non-zero digits** of `n` in their original order. If there are no **non-zero** digits, `x = 0`.

Let `sum` be the **sum of digits** in `x`.

Return an integer representing the value of `x * sum`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 10203004</span>

**Output:** <span class="example-io">12340</span>

**Explanation:**

	- The non-zero digits are 1, 2, 3, and 4. Thus, `x = 1234`.

	- The sum of digits is `sum = 1 + 2 + 3 + 4 = 10`.

	- Therefore, the answer is `x * sum = 1234 * 10 = 12340`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 1000</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

	- The non-zero digit is 1, so `x = 1` and `sum = 1`.

	- Therefore, the answer is `x * sum = 1 * 1 = 1`.

</div>

**Constraints:**

	- `0 <= n <= 10^9`
