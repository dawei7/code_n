## Description

You are given three integers `n`, `s`, and `m`.

A sequence `seq` of integers of length `n` is considered **valid** if:

	- `seq[0] = s`.

	- The sequence is **alternating**, meaning that either:

		<li>`seq[0] > seq[1] < seq[2] > ...`, or

		- `seq[0] < seq[1] > seq[2] < ...`.

	</li>
	- For every adjacent pair, `|seq[i] - seq[i - 1]| <= m`.

A sequence of length 1 is considered alternating.

Return the **maximum** possible element that can appear in any valid sequence.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 4, s = 3, m = 5</span>

**Output:** <span class="example-io">12</span>

**Explanation:**

	- One valid sequence is `[3, 8, 7, 12]`.

	- The maximum element in the sequence is 12.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 2, s = 4, m = 3</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

	- One valid sequence is `[4, 7]`.

	- The maximum element in the sequence is 7.

</div>

**Constraints:**

	- `1 <= n, s <= 10^9`

	- `1 <= m <= 10^5`
