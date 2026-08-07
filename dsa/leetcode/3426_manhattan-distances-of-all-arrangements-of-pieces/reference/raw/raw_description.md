## Description

You are given three integers `<font face="monospace">m</font>`, `<font face="monospace">n</font>`, and `k`.

There is a rectangular grid of size `m × n` containing `k` identical pieces. Return the sum of Manhattan distances between every pair of pieces over all **valid arrangements** of pieces.

A **valid arrangement** is a placement of all `k` pieces on the grid with **at most** one piece per cell.

Since the answer may be very large, return it **modulo** `10^9 + 7`.

The Manhattan Distance between two cells `(x_i, y_i)` and `(x_j, y_j)` is `|x_i - x_j| + |y_i - y_j|`.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">m = 2, n = 2, k = 2</span>

**Output:** <span class="example-io">8</span>

**Explanation:**

The valid arrangements of pieces on the board are:

![](images/4040example1.drawio)

![](images/untitled-diagramdrawio.png)

	- In the first 4 arrangements, the Manhattan distance between the two pieces is 1.

	- In the last 2 arrangements, the Manhattan distance between the two pieces is 2.

Thus, the total Manhattan distance across all valid arrangements is `1 + 1 + 1 + 1 + 2 + 2 = 8`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">m = 1, n = 4, k = 3</span>

**Output:** <span class="example-io">20</span>

**Explanation:**

The valid arrangements of pieces on the board are:

![](images/4040example2drawio.png)

	- The first and last arrangements have a total Manhattan distance of `1 + 1 + 2 = 4`.

	- The middle two arrangements have a total Manhattan distance of `1 + 2 + 3 = 6`.

The total Manhattan distance between all pairs of pieces across all arrangements is `4 + 6 + 6 + 4 = 20`.

</div>

**Constraints:**

	- `1 <= m, n <= 10^5`

	- `2 <= m * n <= 10^5`

	- `<font face="monospace">2 <= k <= m * n</font>`
