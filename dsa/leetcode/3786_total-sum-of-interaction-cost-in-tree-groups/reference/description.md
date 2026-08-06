## Description

You are given an integer `n` and an undirected tree with `n` nodes numbered from 0 to `n - 1`. This is represented by a 2D array `edges` of length `n - 1`, where `edges[i] = [u_i, v_i]` indicates an undirected edge between nodes `u_i` and `v_i`.

You are also given an integer array `group` of length `n`, where `group[i]` denotes the group label assigned to node `i`.

<ul>
	<li>Two nodes `u` and `v` are considered part of the same group if `group[u] == group[v]`.</li>
	<li>The **interaction cost** between `u` and `v` is defined as the number of edges on the unique path connecting them in the tree.</li>
</ul>

Return an integer denoting the **sum** of interaction costs over all **unordered** pairs `(u, v)` with `u != v` such that `group[u] == group[v]`.
