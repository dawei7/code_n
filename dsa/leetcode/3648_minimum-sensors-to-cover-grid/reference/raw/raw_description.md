## Description

You are given `n × m` grid and an integer `k`.

A sensor placed on cell `(r, c)` covers all cells whose **Chebyshev distance** from `(r, c)` is **at most** `k`.

The **Chebyshev distance** between two cells `(r_1, c_1)` and `(r_2, c_2)` is `max(|r_1 − r_2|,|c_1 − c_2|)`.

Your task is to return the **minimum** number of sensors required to cover every cell of the grid.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">n = 5, m = 5, k = 1</span>

**Output:** <span class="example-io">4</span>

**Explanation:**

Placing sensors at positions `(0, 3)`, `(1, 0)`, `(3, 3)`, and `(4, 1)` ensures every cell in the grid is covered. Thus, the answer is 4.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">n = 2, m = 2, k = 2</span>

**Output:** <span class="example-io">1</span>

**Explanation:**

With `k = 2`, a single sensor can cover the entire `2 * 2` grid regardless of its position. Thus, the answer is 1.

</div>

**Constraints:**

	- `1 <= n <= 10^3`

	- `1 <= m <= 10^3`

	- `0 <= k <= 10^3`
