## Description

You are given a positive integer `n` and an integer `target`.

Return the **<span data-keyword="lexicographically-smaller-array">lexicographically smallest</span>** array of integers of size `n` such that:

	- The **sum** of its elements equals `target`.

	- The **absolute values** of its elements form a **permutation** of size `n`.

If no such array exists, return an empty array.

A **permutation** of size `n` is a rearrangement of integers `1, 2, ..., n`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, target = 0</span>

**Output:** <span class="example-io">[-3,1,2]</span>

**Explanation:**

The arrays that sum to 0 and whose absolute values form a permutation of size 3 are:

	- `[-3, 1, 2]`

	- `[-3, 2, 1]`

	- `[-2, -1, 3]`

	- `[-2, 3, -1]`

	- `[-1, -2, 3]`

	- `[-1, 3, -2]`

	- `[1, -3, 2]`

	- `[1, 2, -3]`

	- `[2, -3, 1]`

	- `[2, 1, -3]`

	- `[3, -2, -1]`

	- `[3, -1, -2]`

The lexicographically smallest one is `[-3, 1, 2]`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 1, target = 10000000000</span>

**Output:** <span class="example-io">[]</span>

**Explanation:**

There are no arrays that sum to <span class="example-io">10000000000 and whose absolute values form a permutation of size 1. Therefore, the answer is `[]`.</span>

</div>

**Constraints:**

	- `1 <= n <= 10^5`

	- `-10^10 <= target <= 10^10`
