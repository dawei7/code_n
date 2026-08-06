## Description

There is an undirected tree with `n` nodes labeled from `0` to `n - 1`, and rooted at node `0`. You are given a 2D integer array `edges` of length `n - 1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

You are also given a **0-indexed** integer array `values` of length `n`, where `values[i]` is the **value** associated with the `i^th` node.

You start with a score of `0`. In one operation, you can:

<ul>
	<li>Pick any node `i`.</li>
	<li>Add `values[i]` to your score.</li>
	<li>Set `values[i]` to `0`.</li>
</ul>

A tree is **healthy** if the sum of values on the path from the root to any leaf node is different than zero.

Return *the **maximum score** you can obtain after performing these operations on the tree any number of times so that it remains **healthy**.*
