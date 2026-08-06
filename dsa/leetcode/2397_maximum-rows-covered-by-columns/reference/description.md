## Description

You are given an `m x n` binary matrix `matrix` and an integer `numSelect`.

Your goal is to select exactly `numSelect` **distinct **columns from `matrix` such that you cover as many rows as possible.

A row is considered **covered** if all the `1`'s in that row are also part of a column that you have selected. If a row does not have any `1`s, it is also considered covered.

More formally, let us consider `selected = {c_1, c_2, ...., c_numSelect}` as the set of columns selected by you. A row `i` is **covered** by `selected` if:

<ul>
	<li>For each cell where `matrix[i][j] == 1`, the column `j` is in `selected`.</li>
	<li>Or, no cell in row `i` has a value of `1`.</li>
</ul>

Return the **maximum** number of rows that can be **covered** by a set of `numSelect` columns.
