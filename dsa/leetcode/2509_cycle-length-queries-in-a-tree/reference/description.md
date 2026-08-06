## Description

You are given an integer `n`. There is a **complete binary tree** with `2^n - 1` nodes. The root of that tree is the node with the value `1`, and every node with a value `val` in the range `[1, 2^n - 1 - 1]` has two children where:

<ul>
	<li>The left node has the value `2 * val`, and</li>
	<li>The right node has the value `2 * val + 1`.</li>
</ul>

You are also given a 2D integer array `queries` of length `m`, where `queries[i] = [a_i, b_i]`. For each query, solve the following problem:

<ol>
	<li>Add an edge between the nodes with values `a_i` and `b_i`.</li>
	<li>Find the length of the cycle in the graph.</li>
	<li>Remove the added edge between nodes with values `a_i` and `b_i`.</li>
</ol>

**Note** that:

<ul>
	<li>A **cycle** is a path that starts and ends at the same node, and each edge in the path is visited only once.</li>
	<li>The length of a cycle is the number of edges visited in the cycle.</li>
	<li>There could be multiple edges between two nodes in the tree after adding the edge of the query.</li>
</ul>

Return *an array *`answer`* of length *`m`* where* `answer[i]` *is the answer to the* `i^th` *query.*
