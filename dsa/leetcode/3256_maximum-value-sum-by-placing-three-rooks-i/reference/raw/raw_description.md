## Description

You are given a `m x n` 2D array `board` representing a chessboard, where `board[i][j]` represents the **value** of the cell `(i, j)`.

Rooks in the **same** row or column **attack** each other. You need to place *three* rooks on the chessboard such that the rooks **do not** **attack** each other.

Return the **maximum** sum of the cell **values** on which the rooks are placed.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">board = </span>[[-3,1,1,1],[-3,1,-3,1],[-3,2,1,1]]

**Output:** 4

**Explanation:**

![](images/rooks2.png)

We can place the rooks in the cells `(0, 2)`, `(1, 3)`, and `(2, 1)` for a sum of `1 + 1 + 2 = 4`.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">board = [[1,2,3],[4,5,6],[7,8,9]]</span>

**Output:** <span class="example-io">15</span>

**Explanation:**

We can place the rooks in the cells `(0, 0)`, `(1, 1)`, and `(2, 2)` for a sum of `1 + 5 + 9 = 15`.

</div>

**Example 3:**

<div class="example-block">
**Input:** <span class="example-io">board = [[1,1,1],[1,1,1],[1,1,1]]</span>

**Output:** <span class="example-io">3</span>

**Explanation:**

We can place the rooks in the cells `(0, 2)`, `(1, 1)`, and `(2, 0)` for a sum of `1 + 1 + 1 = 3`.

</div>

**Constraints:**

	- `3 <= m == board.length <= 100`

	- `3 <= n == board[i].length <= 100`

	- `-10^9 <= board[i][j] <= 10^9`
