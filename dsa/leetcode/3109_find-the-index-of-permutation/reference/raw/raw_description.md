## Description

Given an array `perm` of length `n` which is a permutation of `[1, 2, ..., n]`, return the index of `perm` in the <span data-keyword="lexicographically-sorted-array">lexicographically sorted</span> array of all of the permutations of `[1, 2, ..., n]`.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">perm = [1,2]</span>

**Output:** <span class="example-io">0</span>

**Explanation:**

There are only two permutations in the following order:

`[1,2]`, `[2,1]`

And `[1,2]` is at index 0.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">perm = [3,1,2]</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

There are only six permutations in the following order:

`[1,2,3]`, `[1,3,2]`, `[2,1,3]`, `[2,3,1]`, `[3,1,2]`, `[3,2,1]`

And `[3,1,2]` is at index 4.

</div>

**Constraints:**

	- `1 <= n == perm.length <= 10^5`

	- `perm` is a permutation of `[1, 2, ..., n]`.
