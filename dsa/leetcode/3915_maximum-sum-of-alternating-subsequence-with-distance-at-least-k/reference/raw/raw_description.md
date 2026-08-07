## Description

You are given an integer array `nums` of length `n` and an integer `k`.

Pick a **<span data-keyword="subsequence-sequence">subsequence</span>** with indices `0 <= i_1 < i_2 < ... < i_m < n` such that:

	- For every `1 <= t < m`, `i_t+1 - i_t >= k`.

	- The selected values form a **strictly alternating** sequence. In other words, either:

		<li>`nums[i_1] < nums[i_2] > nums[i_3] < ...`, or

		- `nums[i_1] > nums[i_2] < nums[i_3] > ...`

	</li>

A **subsequence** of length 1 is also considered **strictly** alternating. The score of a **valid** subsequence is the **sum** of its selected values.

Return an integer denoting the **maximum** possible **score** of a valid subsequence.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5,4,2], k = 2</span>

**Output:** <span class="example-io">7</span>

**Explanation:**

An optimal choice is indices `[0, 2]`, which gives values `[5, 2]`.

	- The distance condition holds because `2 - 0 = 2 >= k`.

	- The values are strictly alternating because `5 > 2`.

The score is `5 + 2 = 7`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [3,5,4,2,4], k = 1</span>

**Output:** <span class="example-io">14</span>

**Explanation:**

An optimal choice is indices `[0, 1, 3, 4]`, which gives values `[3, 5, 2, 4]`.

	- The distance condition holds because each pair of consecutive chosen indices differs by at least `k = 1`.

	- The values are strictly alternating since `3 < 5 > 2 < 4`.

The score is `3 + 5 + 2 + 4 = 14`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums = [5], k = 1</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

The only valid subsequence is `[5]`. A subsequence with 1 element is always strictly alternating, so the score is 5.

</div>

**Constraints:**

	- `1 <= n == nums.length <= 10^5`

	- `1 <= nums[i] <= 10^5`

	- `1 <= k <= n`
