## Description

There is a 2D `grid` of size `n x n` where each cell of this grid has a lamp that is initially **turned off**.

You are given a 2D array of lamp positions `lamps`, where `lamps[i] = [row_i, col_i]` indicates that the lamp at `grid[row_i][col_i]` is **turned on**. Even if the same lamp is listed more than once, it is turned on.

When a lamp is turned on, it **illuminates its cell** and **all other cells** in the same **row, column, or diagonal**.

You are also given another 2D array `queries`, where `queries[j] = [row_j, col_j]`. For the `j^th` query, determine whether `grid[row_j][col_j]` is illuminated or not. After answering the `j^th` query, **turn off** the lamp at `grid[row_j][col_j]` and its **8 adjacent lamps** if they exist. A lamp is adjacent if its cell shares either a side or corner with `grid[row_j][col_j]`.

Return *an array of integers *`ans`*,** where *`ans[j]`* should be *`1`* if the cell in the *`j^th`* query was illuminated, or *`0`* if the lamp was not.*
