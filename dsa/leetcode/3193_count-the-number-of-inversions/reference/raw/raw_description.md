## Description

You are given an integer `n` and a 2D array `requirements`, where `requirements[i] = [end_i, cnt_i]` represents the end index and the **inversion** count of each requirement.

A pair of indices `(i, j)` from an integer array `nums` is called an **inversion** if:

	- `i < j` and `nums[i] > nums[j]`

Return the number of <span data-keyword="permutation">permutations</span> `perm` of `[0, 1, 2, ..., n - 1]` such that for **all** `requirements[i]`, `perm[0..end_i]` has exactly `cnt_i` inversions.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, requirements = [[2,2],[0,0]]</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

The two permutations are:

	- `[2, 0, 1]`

		<li>Prefix `[2, 0, 1]` has inversions `(0, 1)` and `(0, 2)`.

		- Prefix `[2]` has 0 inversions.

	</li>
	- `[1, 2, 0]`

		<li>Prefix `[1, 2, 0]` has inversions `(0, 2)` and `(1, 2)`.

		- Prefix `[1]` has 0 inversions.

	</li>

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 3, requirements = [[2,2],[1,1],[0,0]]</span>

**Output:** 1

**Explanation:**

The only satisfying permutation is `[2, 0, 1]`:

	- Prefix `[2, 0, 1]` has inversions `(0, 1)` and `(0, 2)`.

	- Prefix `[2, 0]` has an inversion `(0, 1)`.

	- Prefix `[2]` has 0 inversions.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">n = 2, requirements = [[0,0],[1,0]]</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

The only satisfying permutation is `[0, 1]`:

	- Prefix `[0]` has 0 inversions.

	- Prefix `[0, 1]` has no inversions.

</div>

**Constraints:**

	- `2 <= n <= 300`

	- `1 <= requirements.length <= n`

	- `requirements[i] = [end_i, cnt_i]`

	- `0 <= end_i <= n - 1`

	- `0 <= cnt_i <= 400`

	- The input is generated such that there is at least one `i` such that `end_i == n - 1`.

	- The input is generated such that all `end_i` are unique.
