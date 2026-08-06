## Description

You are given an integer `n` and an undirected, weighted tree rooted at node 1 with `n` nodes numbered from 1 to `n`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i, w_i]` indicates an undirected edge from node `u_i` to `v_i` with weight `w_i`.

You are also given a 2D integer array `queries` of length `q`, where each `queries[i]` is either:

<ul>
	<li>`[1, u, v, w']` – **Update** the weight of the edge between nodes `u` and `v` to `w'`, where `(u, v)` is guaranteed to be an edge present in `edges`.</li>
	<li>`[2, x]` – **Compute** the **shortest** path distance from the root node 1 to node `x`.</li>
</ul>

Return an integer array `answer`, where `answer[i]` is the **shortest** path distance from node 1 to `x` for the `i^th` query of `[2, x]`.
