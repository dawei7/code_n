## Description

Given the `root` of a binary tree, construct a **0-indexed** `m x n` string matrix `res` that represents a **formatted layout** of the tree. The formatted layout matrix should be constructed using the following rules:

<ul>
	<li>The **height** of the tree is `height` and the number of rows `m` should be equal to `height + 1`.</li>
	<li>The number of columns `n` should be equal to `2^height+1 - 1`.</li>
	<li>Place the **root node** in the **middle** of the **top row** (more formally, at location `res[0][(n-1)/2]`).</li>
	<li>For each node that has been placed in the matrix at position `res[r][c]`, place its **left child** at `res[r+1][c-2^height-r-1]` and its **right child** at `res[r+1][c+2^height-r-1]`.</li>
	<li>Continue this process until all the nodes in the tree have been placed.</li>
	<li>Any empty cells should contain the empty string `""`.</li>
</ul>

Return *the constructed matrix *`res`.
