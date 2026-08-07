## Description

You are given an integer `n`.

The **score** of `n` is defined as the **sum** of `d * freq(d)` over all **distinct** digits `d`, where `freq(d)` denotes the number of times the digit `d` appears in `n`.

Return an integer denoting the score of `n`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 122</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

	- The digit 1 appears 1 time, contributing `1 * 1 = 1`.

	- The digit 2 appears 2 times, contributing `2 * 2 = 4`.

	- Thus, the score of `n` is `1 + 4 = 5`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 101</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

	- The digit 0 appears 1 time, contributing `0 * 1 = 0`.

	- The digit 1 appears 2 times, contributing `1 * 2 = 2`.

	- Thus, the score of `n` is 2.

</div>

**Constraints:**

	- `1 <= n <= 10^9`
