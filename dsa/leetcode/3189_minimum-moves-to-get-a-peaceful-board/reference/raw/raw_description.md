## Description

Given a 2D array `rooks` of length `n`, where `rooks[i] = [x_i, y_i]` indicates the position of a rook on an `n x n` chess board. Your task is to move the rooks **1 cell **at a time vertically or horizontally (to an *adjacent* cell) such that the board becomes **peaceful**.

A board is **peaceful** if there is **exactly** one rook in each row and each column.

Return the **minimum** number of moves required to get a *peaceful board*.

**Note** that **at no point** can there be two rooks in the same cell.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">rooks = [[0,0],[1,0],[1,1]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

![](images/ex1-edited.gif)

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">rooks = [[0,0],[0,1],[0,2],[0,3]]</span>

**Output:** <span class="example-io">6</span>

**Explanation:**

![](images/ex2-edited.gif)

</div>

**Constraints:**

	- `1 <= n == rooks.length <= 500`

	- `0 <= x_i, y_i <= n - 1`

	- The input is generated such that there are no 2 rooks in the same cell.
