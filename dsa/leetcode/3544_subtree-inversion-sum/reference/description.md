## Description

<p data-end="551" data-start="302">You are given an undirected tree rooted at node `0`, with `n` nodes numbered from 0 to `n - 1`. The tree is represented by a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an edge between nodes `u_i` and `v_i`.

<p data-end="670" data-start="553">You are also given an integer array `nums` of length `n`, where `nums[i]` represents the value at node `i`, and an integer `k`.

<p data-end="763" data-start="672">You may perform **inversion operations** on a subset of nodes subject to the following rules:

<ul data-end="1247" data-start="765">
	<li data-end="890" data-start="765">
	<p data-end="799" data-start="767"><strong data-end="799" data-start="767">Subtree Inversion Operation:</strong>

	<ul data-end="890" data-start="802">
		<li data-end="887" data-start="802">
		<p data-end="887" data-start="804">When you invert a node, every value in the <span data-keyword="subtree-of-node">subtree</span> rooted at that node is multiplied by -1.

		</li>
	</ul>
	</li>
	<li data-end="1247" data-start="891">
	<p data-end="931" data-start="893"><strong data-end="931" data-start="893">Distance Constraint on Inversions:</strong>

	<ul data-end="1247" data-start="934">
		<li data-end="1020" data-start="934">
		<p data-end="1020" data-start="936">You may only invert a node if it is "sufficiently far" from any other inverted node.

		</li>
		<li data-end="1247" data-start="1023">
		<p data-end="1247" data-start="1025">Specifically, if you invert two nodes `a` and `b` such that one is an ancestor of the other (i.e., if `LCA(a, b) = a` or `LCA(a, b) = b`), then the distance (the number of edges on the unique path between them) must be at least `k`.

		</li>
	</ul>
	</li>
</ul>

<p data-end="1358" data-start="1249">Return the **maximum** possible **sum** of the tree's node values after applying **inversion operations**.
