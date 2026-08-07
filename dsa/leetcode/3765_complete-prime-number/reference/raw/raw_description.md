## Description

You are given an integer `num`.

A number `num` is called a **Complete <span data-keyword="prime-number">Prime Number</span>** if every **prefix** and every **suffix** of `num` is **prime**.

Return `true` if `num` is a Complete Prime Number, otherwise return `false`.

**Note**:

	- A **prefix** of a number is formed by the **first** `k` digits of the number.

	- A **suffix** of a number is formed by the **last** `k` digits of the number.

	- Single-digit numbers are considered Complete Prime Numbers only if they are **prime**.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">num = 23</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

	- **​​​​​​​**Prefixes of `num = 23` are 2 and 23, both are prime.

	- Suffixes of `num = 23` are 3 and 23, both are prime.

	- All prefixes and suffixes are prime, so 23 is a Complete Prime Number and the answer is `true`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">num = 39</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

	- Prefixes of `num = 39` are 3 and 39. 3 is prime, but 39 is not prime.

	- Suffixes of `num = 39` are 9 and 39. Both 9 and 39 are not prime.

	- At least one prefix or suffix is not prime, so 39 is not a Complete Prime Number and the answer is `false`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">num = 7</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

	- 7 is prime, so all its prefixes and suffixes are prime and the answer is `true`.

</div>

**Constraints:**

	- `1 <= num <= 10^9`
