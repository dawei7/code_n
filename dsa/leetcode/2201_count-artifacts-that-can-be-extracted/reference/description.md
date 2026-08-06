## Description

There is an `n x n` **0-indexed** grid with some artifacts buried in it. You are given the integer `n` and a **0-indexed **2D integer array `artifacts` describing the positions of the rectangular artifacts where `artifacts[i] = [r1_i, c1_i, r2_i, c2_i]` denotes that the `i^th` artifact is buried in the subgrid where:

<ul>
	<li>`(r1_i, c1_i)` is the coordinate of the **top-left** cell of the `i^th` artifact and</li>
	<li>`(r2_i, c2_i)` is the coordinate of the **bottom-right** cell of the `i^th` artifact.</li>
</ul>

You will excavate some cells of the grid and remove all the mud from them. If the cell has a part of an artifact buried underneath, it will be uncovered. If all the parts of an artifact are uncovered, you can extract it.

Given a **0-indexed** 2D integer array `dig` where `dig[i] = [r_i, c_i]` indicates that you will excavate the cell `(r_i, c_i)`, return *the number of artifacts that you can extract*.

The test cases are generated such that:

<ul>
	<li>No two artifacts overlap.</li>
	<li>Each artifact only covers at most `4` cells.</li>
	<li>The entries of `dig` are unique.</li>
</ul>
