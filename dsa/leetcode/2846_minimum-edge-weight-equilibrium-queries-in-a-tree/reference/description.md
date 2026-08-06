## Description

There is an undirected tree with `n` nodes labeled from `0` to `n - 1`. You are given the integer `n` and a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, w_i]` indicates that there is an edge between nodes `u_i` and `v_i` with weight `w_i` in the tree.

You are also given a 2D integer array `queries` of length `m`, where `queries[i] = [a_i, b_i]`. For each query, find the **minimum number of operations** required to make the weight of every edge on the path from `a_i` to `b_i` equal. In one operation, you can choose any edge of the tree and change its weight to any value.

**Note** that:

<ul>
	<li>Queries are **independent** of each other, meaning that the tree returns to its **initial state** on each new query.</li>
	<li>The path from `a_i` to `b_i` is a sequence of **distinct** nodes starting with node `a_i` and ending with node `b_i` such that every two adjacent nodes in the sequence share an edge in the tree.</li>
</ul>

Return *an array *`answer`* of length *`m`* where* `answer[i]` *is the answer to the* `i^th` *query.*
