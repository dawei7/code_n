## Description

You are given an undirected graph with `n` nodes labeled from 0 to `n - 1`. Node `i` has a **value** of `nums[i]`, which is either 0 or 1. The edges of the graph are given by a 2D array `edges` where `edges[i] = [u_i, v_i]` represents an edge between node `u_i` and node `v_i`.

For a **non-empty subset** `s` of nodes in the graph, we consider the **induced subgraph** of `s` generated as follows:

<ul>
	<li>We keep only the nodes in `s`.</li>
	<li>We keep only the edges whose two endpoints are both in `s`.</li>
</ul>

Return an integer representing the number of **non-empty** subsets `s` of nodes in the graph such that:

<ul>
	<li>The **induced subgraph** of `s` is **connected**.</li>
	<li>The **sum** of node **values** in `s` is **even**.</li>
</ul>
