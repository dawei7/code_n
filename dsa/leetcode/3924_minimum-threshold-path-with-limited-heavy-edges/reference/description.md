## Description

There is an undirected weighted graph with `n` nodes labeled from 0 to `n - 1`.

The graph is represented by a 2D integer array `edges`, where each edge `edges[i] = [u_i, v_i, w_​​​​​​​i]` indicates that there is an undirected edge between nodes `u_i` and `v_i` with weight `w_​​​​​​​i`.

You are also given integers `source`, `target` and `k`.

A `threshold` value determines whether an edge is considered **light** or **heavy**:

<ul>
	<li>
	An edge is **light** if its weight is **less than** or **equal** to `threshold`.

	</li>
	<li>
	An edge is **heavy** if its weight is **greater than** `threshold`.

	</li>
</ul>

A path from `source` to `target` is **valid** if it contains **at most** `k` heavy edges.

Return the **minimum integer **`threshold` such that **at least** one **valid** path exists from `source` to `target`. If no such path exists, return -1.
