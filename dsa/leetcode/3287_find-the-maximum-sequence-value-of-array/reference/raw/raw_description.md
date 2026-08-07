## Description

You are given an integer array `nums` and a **positive** integer `k`.

The **value** of a sequence `seq` of size `2 * x` is defined as:

	- `(seq[0] OR seq[1] OR ... OR seq[x - 1]) XOR (seq[x] OR seq[x + 1] OR ... OR seq[2 * x - 1])`.

Return the **maximum** **value** of any <span data-keyword="subsequence-array">subsequence</span> of `nums` having size `2 * k`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums = [2,6,7], k = 1</span>

**Output:** <span class="example-io">5</span>

**Explanation:**

The subsequence `[2, 7]` has the maximum value of `2 XOR 7 = 5`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums = [4,2,5,6,7], k = 2</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The subsequence `[4, 5, 6, 7]` has the maximum value of `(4 OR 5) XOR (6 OR 7) = 2`.

</div>

**Constraints:**

	- `2 <= nums.length <= 400`

	- `1 <= nums[i] < 2^7`

	- `1 <= k <= nums.length / 2`
