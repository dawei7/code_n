## Description

You are given an `m x n` matrix `grid` consisting of characters and a string `pattern`.

A <strong data-end="264" data-start="240">horizontal substring</strong> is a contiguous sequence of characters read from left to right. If the end of a row is reached before the substring is complete, it wraps to the first column of the next row and continues as needed. You do **not** wrap from the bottom row back to the top.

A <strong data-end="484" data-start="462">vertical substring</strong> is a contiguous sequence of characters read from top to bottom. If the bottom of a column is reached before the substring is complete, it wraps to the first row of the next column and continues as needed. You do **not** wrap from the last column back to the first.

Count the number of cells in the matrix that satisfy the following condition:

<ul>
	<li>The cell must be part of **at least** one horizontal substring and **at least** one vertical substring, where **both** substrings are equal to the given `pattern`.</li>
</ul>

Return the count of these cells.
