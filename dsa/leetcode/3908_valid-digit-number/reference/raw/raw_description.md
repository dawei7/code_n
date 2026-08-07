## Description

You are given an integer `n` and a digit `x`.

A number is considered **valid** if:

	- It contains **at least one** occurrence of digit `x`, and

	- It **does not start** with digit `x`.

Return `true` if `n` is **valid**, otherwise return `false`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 101, x = 0</span>

**Output:** <span class="example-io">true</span>

**Explanation:**

The number contains digit 0 at index 1. It does not start with 0, so it satisfies both conditions. Thus, the answer is `true`​​​​​​​.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 232, x = 2</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

The number starts with 2, which violates the condition. Thus, the answer is `false`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, x = 1</span>

**Output:** <span class="example-io">false</span>

**Explanation:**

The number does not contain digit 1. Thus, the answer is `false`.

</div>

**Constraints:**

	- `0 <= n <= 10^5​​​​​​​`

	- `0 <= x <= 9`
