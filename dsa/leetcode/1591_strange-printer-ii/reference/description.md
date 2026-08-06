## Description

There is a strange printer with the following two special requirements:

<ul>
	<li>On each turn, the printer will print a solid rectangular pattern of a single color on the grid. This will cover up the existing colors in the rectangle.</li>
	<li>Once the printer has used a color for the above operation, **the same color cannot be used again**.</li>
</ul>

You are given a `m x n` matrix `targetGrid`, where `targetGrid[row][col]` is the color in the position `(row, col)` of the grid.

Return `true`* if it is possible to print the matrix *`targetGrid`*,** otherwise, return *`false`.
