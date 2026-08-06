## Description

You are given an **undirected** tree with `n` nodes labeled from `0` to `n - 1`, and rooted at node `0`. You are given a 2D integer array `edges` of length `n - 1`, where `edges[i] = [a_i, b_i]` indicates that there is an edge between nodes `a_i` and `b_i` in the tree.

You are also given a **0-indexed** integer array `cost` of length `n`, where `cost[i]` is the **cost** assigned to the `i^th` node.

You need to place some coins on every node of the tree. The number of coins to be placed at node `i` can be calculated as:

<ul>
	<li>If size of the subtree of node `i` is less than `3`, place `1` coin.</li>
	<li>Otherwise, place an amount of coins equal to the **maximum** product of cost values assigned to `3` distinct nodes in the subtree of node `i`. If this product is **negative**, place `0` coins.</li>
</ul>

Return *an array *`coin`* of size *`n`* such that *`coin[i]`* is the number of coins placed at node *`i`*.*
