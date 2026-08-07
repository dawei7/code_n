## Description

Given an integer `n`, find the digit that occurs **least** frequently in its decimal representation. If multiple digits have the same frequency, choose the **smallest** digit.

Return the chosen digit as an integer.

The **frequency** of a digit `x` is the number of times it appears in the decimal representation of `n`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 1553322</span>

**Output:** 1

**Explanation:**

The least frequent digit in `n` is 1, which appears only once. All other digits appear twice.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 723344511</span>

**Output:** 2

**Explanation:**

The least frequent digits in `n` are 7, 2, and 5; each appears only once.

</div>

**Constraints:**

	- `1 <= n <= 2^31​​​​​​​ - 1`
