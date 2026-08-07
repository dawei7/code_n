## Description

You are given a 2D array of integers `coordinates` of length `n` and an integer `k`, where `0 <= k < n`.

`coordinates[i] = [x_i, y_i]` indicates the point `(x_i, y_i)` in a 2D plane.

An **increasing path** of length `m` is defined as a list of points `(x_1, y_1)`, `(x_2, y_2)`, `(x_3, y_3)`, ..., `(x_m, y_m)` such that:

	- `x_i < x_i + 1` and `y_i < y_i + 1` for all `i` where `1 <= i < m`.

	- `(x_i, y_i)` is in the given coordinates for all `i` where `1 <= i <= m`.

Return the **maximum** length of an **increasing path** that contains `coordinates[k]`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">coordinates = [[3,1],[2,2],[4,1],[0,0],[5,3]], k = 1</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

`(0, 0)`, `(2, 2)`, `(5, 3)`<!-- notionvc: 082cee9e-4ce5-4ede-a09d-57001a72141d --> is the longest increasing path that contains `(2, 2)`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">coordinates = [[2,1],[7,0],[5,6]], k = 2</span>

**Output:** <span class="example-io">2</span>

**Explanation:**

`(2, 1)`, `(5, 6)` is the longest increasing path that contains `(5, 6)`.

</div>

**Constraints:**

	- `1 <= n == coordinates.length <= 10^5`

	- `coordinates[i].length == 2`

	- `0 <= coordinates[i][0], coordinates[i][1] <= 10^9`

	- All elements in `coordinates` are **distinct**.<!-- notionvc: 6e412fc2-f9dd-4ba2-b796-5e802a2b305a --><!-- notionvc: c2cf5618-fe99-4909-9b4c-e6b068be22a6 -->

	- `0 <= k <= n - 1`
