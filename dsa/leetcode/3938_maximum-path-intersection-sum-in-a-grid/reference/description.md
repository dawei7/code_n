## Description

<p data-end="139" data-start="64">You are given an `m x n` integer matrix `grid`.

Two players move across the grid:

<ul>
	<li>Player 1 starts at the top-left cell `(0, 0)` and can move only right or down. Their destination is the bottom-right cell `(m - 1, n - 1)`.</li>
	<li>Player 2 starts at the bottom-left cell `(m - 1, 0)` and can move only right or up. Their destination is the top-right cell `(0, n - 1)`.</li>
</ul>

Each player must choose a valid path from their respective starting cell to their destination.

A cell is called **shared** if it belongs to **both** chosen paths.

Return an integer denoting the **maximum** possible sum of values of all **shared** cells.
