## Description

There exists an **undirected** tree with `n` nodes numbered `0` to `n - 1`. You are given a 2D integer array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates that there is an edge between nodes `u_i` and `v_i` in the tree.

Initially, **all** nodes are **unmarked**. For each node `i`:

<ul>
	<li>If `i` is odd, the node will get marked at time `x` if there is **at least** one node *adjacent* to it which was marked at time `x - 1`.</li>
	<li>If `i` is even, the node will get marked at time `x` if there is **at least** one node *adjacent* to it which was marked at time `x - 2`.</li>
</ul>

Return an array `times` where `times[i]` is the time when all nodes get marked in the tree, if you mark node `i` at time `t = 0`.

**Note** that the answer for each `times[i]` is **independent**, i.e. when you mark node `i` all other nodes are *unmarked*.
