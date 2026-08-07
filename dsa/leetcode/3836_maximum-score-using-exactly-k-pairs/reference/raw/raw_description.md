## Description

You are given two integer arrays `nums1` and `nums2` of lengths `n` and `m` respectively, and an integer `k`.

You must choose **exactly** `k` pairs of indices `(i_1, j_1), (i_2, j_2), ..., (i_k, j_k)` such that:

	- `0 <= i_1 < i_2 < ... < i_k < n`

	- `0 <= j_1 < j_2 < ... < j_k < m`

For each chosen pair `(i, j)`, you gain a score of `nums1[i] * nums2[j]`.

The total **score** is the **sum** of the products of all selected pairs.

Return an integer representing the **maximum** achievable total score.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [1,3,2], nums2 = [4,5,1], k = 2</span>

**Output:** <span class="example-io">22</span>

**Explanation:**

One optimal choice of index pairs is:

	- `(i_1, j_1) = (1, 0)` which scores `3 * 4 = 12`

	- `(i_2, j_2) = (2, 1)` which scores `2 * 5 = 10`

This gives a total score of `12 + 10 = 22`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [-2,0,5], nums2 = [-3,4,-1,2], k = 2</span>

**Output:** <span class="example-io">26</span>

**Explanation:**

One optimal choice of index pairs is:

	- `(i_1, j_1) = (0, 0)` which scores `-2 * -3 = 6`

	- `(i_2, j_2) = (2, 1)` which scores `5 * 4 = 20`

The total score is `6 + 20 = 26`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">nums1 = [-3,-2], nums2 = [1,2], k = 2</span>

**Output:** <span class="example-io">-7</span>

**Explanation:**

The optimal choice of index pairs is:

	- `(i_1, j_1) = (0, 0)` which scores `-3 * 1 = -3`

	- `(i_2, j_2) = (1, 1)` which scores `-2 * 2 = -4`

The total score is `-3 + (-4) = -7`.

</div>

**Constraints:**

	- `1 <= n == nums1.length <= 100`

	- `1 <= m == nums2.length <= 100`

	- `-10^6 <= nums1[i], nums2[i] <= 10^6`

	- `1 <= k <= min(n, m)`
