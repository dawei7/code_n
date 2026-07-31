## Description

Given a 2D integer matrix `matrix`, support two kinds of operation: replace the value of one cell, and calculate the sum inside an inclusive axis-aligned rectangle whose upper-left corner is `(row1,col1)` and lower-right corner is `(row2,col2)`.

Implement the `NumMatrix` class:

- `NumMatrix(int[][] matrix)` initializes the object with `matrix`.
- `void update(int row, int col, int val)` assigns `val` to `matrix[row][col]`.
- `int sumRegion(int row1, int col1, int row2, int col2)` returns the sum of all cells in the rectangle bounded by those corners.
