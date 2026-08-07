## Description

You are given an `m x n` matrix `board` containing **letters** `'X'` and `'O'`, **capture regions** that are **surrounded**:

	- **Connect**: A cell is connected to adjacent cells horizontally or vertically.

	- **Region**: To form a region **connect every** `'O'` cell.

	- **Surround**: A region is surrounded if none of the `'O'` cells in that region are on the edge of the board. Such regions are **completely enclosed **by `'X'` cells.

To capture a **surrounded region**, replace all `'O'`s with `'X'`s **in-place** within the original board. You do not need to return anything.

**Example 1:**

<div class="example-block">
**Input:** <span class="example-io">board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]</span>

**Output:** <span class="example-io">[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]</span>

**Explanation:**

![](images/xogrid.jpg)

In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

</div>

**Example 2:**

<div class="example-block">
**Input:** <span class="example-io">board = [["X"]]</span>

**Output:** <span class="example-io">[["X"]]</span>

</div>

**Constraints:**

	- `m == board.length`

	- `n == board[i].length`

	- `1 <= m, n <= 200`

	- `board[i][j]` is `'X'` or `'O'`.
