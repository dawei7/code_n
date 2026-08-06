## Description

There is an **undirected** graph with `n` nodes, numbered from `0` to `n - 1`.

You are given a **0-indexed** integer array `scores` of length `n` where `scores[i]` denotes the score of node `i`. You are also given a 2D integer array `edges` where `edges[i] = [a_i, b_i]` denotes that there exists an **undirected** edge connecting nodes `a_i` and `b_i`.

A node sequence is **valid** if it meets the following conditions:

<ul>
	<li>There is an edge connecting every pair of **adjacent** nodes in the sequence.</li>
	<li>No node appears more than once in the sequence.</li>
</ul>

The score of a node sequence is defined as the **sum** of the scores of the nodes in the sequence.

Return *the **maximum score** of a valid node sequence with a length of *`4`*. *If no such sequence exists, return* *`-1`.
