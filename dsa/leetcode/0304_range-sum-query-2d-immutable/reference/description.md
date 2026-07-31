## Description

Given a 2D integer matrix `matrix`, support repeated queries for the sum of all values inside an inclusive rectangle. The rectangle's upper-left corner is `(row1, col1)` and its lower-right corner is `(row2, col2)`.

Implement the `NumMatrix` class:

- `NumMatrix(int[][] matrix)` initializes the object with `matrix`.
- `int sumRegion(int row1, int col1, int row2, int col2)` returns the sum inside the rectangle bounded by those corners.

Each `sumRegion` call must run in $O(1)$ time.
