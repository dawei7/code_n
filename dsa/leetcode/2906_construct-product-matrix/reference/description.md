## Description

Given a **0-indexed** 2D integer matrix `<font face="monospace">grid</font>`<font face="monospace"> </font>of size `n * m`, we define a **0-indexed** 2D matrix `p` of size `n * m` as the **product** matrix of `grid` if the following condition is met:

<ul>
	<li>Each element `p[i][j]` is calculated as the product of all elements in `grid` except for the element `grid[i][j]`. This product is then taken modulo `<font face="monospace">12345</font>`.</li>
</ul>

Return *the product matrix of* `<font face="monospace">grid</font>`.
