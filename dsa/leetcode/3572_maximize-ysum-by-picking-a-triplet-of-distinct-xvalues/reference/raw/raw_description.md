## Description

You are given two integer arrays `x` and `y`, each of length `n`. You must choose three **distinct** indices `i`, `j`, and `k` such that:

	- `x[i] != x[j]`

	- `x[j] != x[k]`

	- `x[k] != x[i]`

Your goal is to **maximize** the value of `y[i] + y[j] + y[k]` under these conditions. Return the **maximum** possible sum that can be obtained by choosing such a triplet of indices.

If no such triplet exists, return -1.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">x = [1,2,1,3,2], y = [5,3,4,6,2]</span>

**Output:** <span class="example-io">14</span>

**Explanation:**

	- Choose `i = 0` (`x[i] = 1`, `y[i] = 5`), `j = 1` (`x[j] = 2`, `y[j] = 3`), `k = 3` (`x[k] = 3`, `y[k] = 6`).

	- All three values chosen from `x` are distinct. `5 + 3 + 6 = 14` is the maximum we can obtain. Hence, the output is 14.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">x = [1,2,1,2], y = [4,5,6,7]</span>

**Output:** <span class="example-io">-1</span>

**Explanation:**

	- There are only two distinct values in `x`. Hence, the output is -1.

</div>

**Constraints:**

	- `n == x.length == y.length`

	- `3 <= n <= 10^5`

	- `1 <= x[i], y[i] <= 10^6`
